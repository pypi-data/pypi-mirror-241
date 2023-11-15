from promptflow import tool
from promptflow.connections import CustomConnection
from utils.skill import Skill
from utils.mode import Mode
from utils.tool_utils import run_language_skill, build_request_path

# Language Detection: sync only.
INTER_PATH = "/language/:analyze-text"
API_VERSION = "2023-04-15-preview"
SKILL = Skill.LANGUAGE_DETECTION
MODE = Mode.SYNC

# When `parse_response == True`, return string representing detected language's ISO 639-1 code.
# Else, return raw API json output.
@tool 
def get_language_detection(connection:CustomConnection, text:str, parse_response:bool=False): 
    # Create inputs:
    inputs = [ {"text": text} ]

    # Create query parameters and request path:
    query_parameters = {
        "api-version": API_VERSION,
    }
    request_path = build_request_path(query_parameters)
    
    # Create task parameters: 
    parameters = { }

    # Create skill config:
    skill_config = {
        "connection": connection,
        "inter_path": INTER_PATH,
        "request_path": request_path,
        "inputs": inputs, 
        "parameters": parameters,
        "skill": SKILL,
        "mode": MODE,
        "async_support": False,
        "parse_response": parse_response
    }

    # Run skill:
    return run_language_skill(skill_config=skill_config)
