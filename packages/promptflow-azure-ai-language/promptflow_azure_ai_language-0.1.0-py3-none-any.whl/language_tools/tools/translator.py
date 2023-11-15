import uuid
from promptflow import tool
from promptflow.connections import CustomConnection
from utils.skill import Skill
from utils.mode import Mode
from utils.tool_utils import run_language_skill, build_request_path

# Translator: sync only.
INTER_PATH = "/translate"
API_VERSION = "3.0"
SKILL = Skill.TRANSLATE
MODE = Mode.SYNC

# When `parse_response == True`, return dictionary of translations: key=<to-language>, value=<translated-text>.
# Else, return raw API json output.
@tool 
def get_translation(connection:CustomConnection, text:str, to:list[str], source_language:str="", parse_response:bool=False):
    # Create inputs:
    inputs = [ {"Text": text} ]

    # Create query parameters and request path:
    query_parameters = {
        "api-version": API_VERSION,
        "ClientTraceId": str(uuid.uuid4()),
        "to": ",".join(to)
    }
    if len(source_language) != 0:
        query_parameters["from"] = source_language
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
    