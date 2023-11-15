from promptflow import tool
from promptflow.connections import CustomConnection
from utils.skill import Skill
from utils.mode import Mode
from utils.tool_utils import run_language_skill, build_request_path

# Abstractive Summarization: async only.
INTER_PATH = "/language/analyze-text/jobs"
API_VERSION = "2023-04-15-preview"
SKILL = Skill.ABSTRACTIVE_SUMMARIZATION
MODE = Mode.ASYNC

# When `parse_response == True`, return string representing abstractive summary.
# Else, return raw API json output.
@tool 
def get_abstractive_summarization(connection:CustomConnection, language:str, text:str, query:str="", summary_length:str="", parse_response:bool=False):
    # Create inputs:
    inputs = [ {"text": text, "language": language} ]

    # Create query parameters and request path:
    query_parameters = {
        "api-version": API_VERSION,
    }
    request_path = build_request_path(query_parameters)
    
    # Create task parameters:
    parameters = { }
    if len(query) != 0:
        parameters["query"] = query
    if len(summary_length) != 0:
        parameters["summaryLength"] = summary_length

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
    