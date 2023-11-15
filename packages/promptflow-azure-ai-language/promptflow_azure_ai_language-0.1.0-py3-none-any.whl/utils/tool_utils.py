from utils.mode import Mode
from utils.formatter import Formatter
from utils.parser import Parser
from utils.language_client import LanguageClient

MAX_SYNC_TOKENS = 5120

# Runs a language skill given its config.
def run_language_skill(skill_config:dict):
    # Obtain connection info:
    api_key = skill_config["connection"].secrets["api_key"]
    endpoint = skill_config["connection"].configs["endpoint"]
    region = skill_config["connection"].configs.get("region", None)
    inter_path = skill_config["inter_path"]
    request_path = skill_config["request_path"]

    # Obtain parameters:
    inputs = skill_config["inputs"]
    parameters = skill_config["parameters"]
    skill = skill_config["skill"]
    mode = skill_config["mode"]

    # Check for dual support (sync & async) capabilities:
    if mode == Mode.SYNC and skill_config["async_support"]:
        if len(inputs[0]["text"]) > MAX_SYNC_TOKENS:
            mode = Mode.ASYNC
            inter_path = skill_config["async_inter_path"]

    # Create json input:
    formatter = Formatter(skill=skill, mode=mode)
    json_input = formatter.format(inputs=inputs, parameters=parameters)
    print(f"Input: {json_input}")

    # Create client and submit request:
    client = LanguageClient(endpoint=endpoint, inter_path=inter_path, api_key=api_key, region=region)
    response = client.run_endpoint(json_obj=json_input, request_path=request_path, mode=mode)
    json_response = response.json()
    print(f"Status code: {response.status_code}")
    print(f"Response: {json_response}")

    if skill_config["parse_response"]:
        # Parse response:
        parser = Parser(skill=skill, mode=mode)
        return parser.parse_response(response=response)
    
    return json_response

# Builds a request path from query parameters:
def build_request_path(query_parameters:dict) -> str:
    return "?" + "&".join([k + "=" + v for k, v in query_parameters.items()])
