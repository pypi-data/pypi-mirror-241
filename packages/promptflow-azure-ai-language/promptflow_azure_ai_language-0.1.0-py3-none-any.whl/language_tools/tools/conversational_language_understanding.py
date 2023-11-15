from promptflow import tool
from promptflow.connections import CustomConnection
from utils.mode import Mode
from utils.skill import Skill
from utils.tool_utils import run_language_skill, build_request_path
import json

# Conversational Language Understanding: sync only.
INTER_PATH = "/language/:analyze-conversations"
API_VERSION = "2023-04-15-preview"
SKILL = Skill.CONVERSATIONAL_LANGUAGE_UNDERSTANDING
MODE = Mode.SYNC

# Returns conversationaltaskresult as string.
@tool
def get_conversational_language_understanding(connection:CustomConnection, language:str, utterances:str, project_name:str, deployment_name: str, parse_response:bool=False) -> list:
    utteranceList = []
    try:
        utteranceList = json.loads(utterances)
    except:
        utteranceList.append(utterances)
    results = []
    for utterance in utteranceList:
        results.append(get_single_clu_result(
            connection,
            language,
            utterance,
            project_name,
            deployment_name,
            parse_response
        ))
    return results
    
def get_single_clu_result(connection:CustomConnection, language:str, text:str, project_name:str, deployment_name: str, parse_response:bool=False) -> str:
    # Create inputs
    inputs = [ {"text": text, "language": language, "modality": "text"} ]

    # Create query parameters and request path:
    query_parameters = {
        "api-version": API_VERSION,
    }
    request_path = build_request_path(query_parameters)

    # Create task parameters:
    parameters = {
        "projectName": project_name,
        "deploymentName": deployment_name,
        "verbose": True
    }

    # Create tool config:
    skill_config = {
        "connection": connection,
        "inter_path": INTER_PATH,
        "request_path": request_path,
        "inputs": inputs, 
        "parameters": parameters,
        "skill": SKILL,
        "mode": MODE,
        "async_support": True,
        "parse_response": parse_response
    }

    # Run tool:
    return run_language_skill(skill_config=skill_config)
