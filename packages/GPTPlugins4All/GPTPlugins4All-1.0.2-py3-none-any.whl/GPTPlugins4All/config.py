import uuid
import json
import yaml
from enum import Enum
import requests
from openapi_spec_validator import openapi_v3_spec_validator  # You may need to install this package
from urllib.parse import urlencode
import logging
logging.basicConfig(level=logging.INFO)

class AuthMethod(Enum):
    OAUTH = 'OAUTH'
    QUERY = 'QUERY'
    BASIC = 'BASIC'
    HEADER = 'HEADER'
    NONE = 'NONE'

class Config:
    def __init__(self, spec_string):
        self.spec_string = spec_string
        self.spec_object = None
        self.auth_methods = {}
        self.id = str(uuid.uuid4())
        
        # Validate and parse the OpenAPI spec
        self.validate_and_parse_spec(spec_string)
    @classmethod
    def from_existing_config(cls, existing_config):
      """Create a Config object from an existing configuration dictionary."""
      required_fields = ['spec_string', 'spec_id', 'auth_methods']
      if not all(field in existing_config for field in required_fields):
          raise ValueError("Existing configuration is missing required fields")

      return cls(
          spec_string=existing_config['spec'],
          spec_id=existing_config['id'],
          auth_methods=existing_config['auth_methods']
      )
    def validate_and_parse_spec(self, spec_string):
      try:
          spec_object = yaml.safe_load(spec_string) if self.is_yaml(spec_string) else json.loads(spec_string)

          # Validate the spec object against OpenAPI 3.1.0 standards
          errors_iterator = openapi_v3_spec_validator.iter_errors(spec_object)
          errors = list(errors_iterator)
          if errors:
              raise ValueError(f"Spec validation errors: {errors}")

          self.spec_object = spec_object
      except Exception as e:
          raise ValueError(f"Error loading OpenAPI spec: {e}")

    @staticmethod
    def is_yaml(string):
        try:
            yaml.safe_load(string)
            return True
        except yaml.YAMLError:
            return False

    # Method to add authentication method
    def add_auth_method(self, method_name, method_details):
        if method_name not in AuthMethod.__members__:
            raise ValueError(f"Invalid authentication method: {method_name}")
        self.auth_methods['method'] = method_name
        self.auth_methods['details'] = method_details
        print(self.auth_methods)
    def start_oauth_flow(self):
      """Initiates the OAuth flow."""
      auth_config = self.auth_methods.get('details')
      if not auth_config:
          raise ValueError("OAuth configuration not found")

      params = {
          "response_type": "code",
          "client_id": auth_config["client_id"],
          "redirect_uri": auth_config["redirect_uri"],
          "scope": auth_config.get("scope", "")
      }
      auth_url = f"{auth_config['auth_url']}?{urlencode(params)}"
      return auth_url
    def handle_oauth_callback(self, code):
      """Handles the OAuth callback and exchanges the code for tokens."""
      auth_config = self.auth_methods.get('details')
      if not auth_config or not code:
          raise ValueError("OAuth configuration not found or no code provided")

      token_data = {
          "grant_type": "authorization_code",
          "code": code,
          "redirect_uri": auth_config["redirect_uri"],
          "client_id": auth_config["client_id"],
          "client_secret": auth_config["client_secret"]
      }
      response = requests.post(auth_config["token_url"], data=token_data)

      if response.status_code == 200:
          print(response.json())
          print('got token')
          return response.json()
      else:
          raise Exception(f"Failed to obtain tokens: {response.status_code}")
    #creates a simplified representation for the AI to understand
    def generate_simplified_api_representation(self):
      info = self.spec_object.get('info', {})
      simplified_api_representation = (
          f"Title: {info.get('title', 'No title')}\n"
          f"Version: {info.get('version', 'No version')}\n"
          f"Description: {info.get('description', 'No description')}\n\n"
      )
      for path, methods in self.spec_object.get("paths", {}).items():
          for method, details in methods.items():
              operation_id = details.get('operationId', 'Unnamed')
              simplified_api_representation += f"Name: {operation_id}\n"
              simplified_api_representation += f"Endpoint: {path} {method.upper()}\n"
              simplified_api_representation += f"   Description: {details.get('summary', details.get('description', 'No description'))}\n"
              simplified_api_representation += "   Parameters: "
              
              # Add parameters info
              for param in details.get("parameters", []):
                  simplified_api_representation += f"{param['name']} ({param['in']} parameter)"
                  if param.get('required'):
                      simplified_api_representation += " [required]"
                  simplified_api_representation += ", "
              
              if 'requestBody' in details:
                  simplified_api_representation += "Body parameters"

              simplified_api_representation = simplified_api_representation.strip(", ")
              simplified_api_representation += "\n   Response: ...\n\n"
        
      return simplified_api_representation
    # Method to get base url
    def get_base_url(self):
        # Fetch the first server URL from spec_object
        servers = self.spec_object.get('servers', [])
        if servers:
            return servers[0].get('url', '')
        return ''
    # Function to make API call
    def make_api_call_by_operation_id(self, operation_id, params, user_token=None, is_json=False):
        endpoint, method = self.find_endpoint_by_operation_id(operation_id)
        if not endpoint:
            raise ValueError(f"OperationId '{operation_id}' not found in API spec")
        base_url = self.get_base_url()
        url = f"{base_url}{endpoint}"
        
        headers, params = self.prepare_auth(user_token, params)
        
        if is_json:
            headers['Content-Type'] = 'application/json'
            response = getattr(requests, method.lower())(url, json=params, headers=headers)
        else:
            response = getattr(requests, method.lower())(url, params=params, headers=headers)
        
        return response
    
    def prepare_auth(self, user_token, params):
        headers = {}
        auth_method = self.auth_methods.get('method', AuthMethod.NONE.value)
        print(auth_method)
        auth_details = self.auth_methods.get('details', {})
        print(auth_details)
        if auth_method == AuthMethod.OAUTH.value and user_token:
            headers["Authorization"] = f"Bearer {user_token['access_token']}"
        elif auth_method == AuthMethod.BASIC.value:
            headers['Authorization'] = f"Basic {auth_details['key']}"
        elif auth_method == AuthMethod.HEADER.value:
            headers[auth_details['header_name']] = auth_details['key']
        elif auth_method == AuthMethod.QUERY.value:
            params[auth_details['param_name']] = auth_details['key']
        print(headers, params)
        return headers, params
    def make_api_call_by_path(self, path, method, params, user_token=None, is_json=False):
        base_url = self.get_base_url()
        url = f"{base_url}{path}"
        headers, params = self.prepare_auth(user_token, params)
        if is_json:
            headers['Content-Type'] = 'application/json'
            response = getattr(requests, method.lower())(url, json=params, headers=headers)
        else:
            response = getattr(requests, method.lower())(url, params=params, headers=headers)
        return response
    def find_endpoint_by_operation_id(self, operation_id):
        for path, methods in self.spec_object.get("paths", {}).items():
            for method, details in methods.items():
                if details.get('operationId') == operation_id:
                    return path, method
        return None, None
    def generate_tools_representation(self):
      tools = []

      for path, methods in self.spec_object.get("paths", {}).items():
          for method, details in methods.items():
              tool = {
                  "type": "function",
                  "function": {
                      "name": details.get('operationId', 'Unnamed'),
                      "description": details.get('description', 'No description'),
                      "parameters": self.extract_parameters(details.get("parameters", []))
                  }
              }
              if 'requestBody' in details:
                  tool["function"]["parameters"]["body"] = self.extract_request_body(details['requestBody'])
              tools.append(tool)
      
      return tools

    def extract_parameters(self, parameters):
      params = {
          "type": "object",
          "properties": {},
          "required": []
      }
      for param in parameters:
          param_name = param['name']
          param_details = param.get('schema', {})
          params["properties"][param_name] = {
              "type": param_details.get('type', 'unknown'),
              "description": param.get('description', 'No description')
          }
          if param.get('required', False):
              params["required"].append(param_name)
      return params
        
    
   
    def extract_request_body(self, request_body):
      # Extract and return the request body schema
      # You might need to modify this based on the structure of your request body
      return request_body.get("content", {}).get("application/json", {}).get("schema", {})

