from promptflow import tool
from promptflow.connections import CustomConnection
from utils.skill import Skill
from utils.mode import Mode
from utils.tool_utils import run_language_skill, build_request_path

# Key Phrase Extraction: sync & async support.
SYNC_INTER_PATH = "/language/:analyze-text"
ASYNC_INTER_PATH = "/language/analyze-text/jobs"
API_VERSION = "2023-04-15-preview"
SKILL = Skill.KEY_PHRASE_EXTRACTION
MODE = Mode.SYNC

# When `parse_response == True`, return list of strings representing extracted key phrases.
# Else, return raw API json output.
@tool 
def get_key_phrase_extraction(connection:CustomConnection, language:str, text:str, parse_response:bool=False): 
    # Create inputs:
    inputs = [ {"text": text, "language": language} ]

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
        "inter_path": SYNC_INTER_PATH,
        "request_path": request_path,
        "inputs": inputs, 
        "parameters": parameters,
        "skill": SKILL,
        "mode": MODE,
        "async_support": True,
        "async_inter_path": ASYNC_INTER_PATH,
        "parse_response": parse_response
    }

    # Run skill:
    return run_language_skill(skill_config=skill_config)
