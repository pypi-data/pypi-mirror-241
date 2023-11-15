from promptflow import tool
from promptflow.connections import CustomConnection
from utils.mode import Mode
from utils.skill import Skill
from utils.tool_utils import run_language_skill, build_request_path

# Conversation Summarization: async only.
INTER_PATH = "/language/analyze-conversations/jobs"
API_VERSION = "2023-04-15-preview"
SKILL = Skill.CONVERSATION_SUMMARIZATION
MODE = Mode.ASYNC

# When `parse_response == True`, return string representing aspect summary.
# Else, return raw API json output.
@tool
def get_conversation_summarization(connection:CustomConnection, language:str, text:str, summary_aspect:str, modality:str="text", parse_response:bool=False):
    # Create inputs
    inputs = [ {"text": text, "language": language, "modality": modality} ]

    # Create query parameters and request path:
    query_parameters = {
        "api-version": API_VERSION,
    }
    request_path = build_request_path(query_parameters)

    # Create task parameters:
    parameters = {
        "summaryAspects": [summary_aspect]
    }

    # Create skill config:
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

    # Run skill:
    return run_language_skill(skill_config=skill_config)
