from promptflow import tool
from promptflow.connections import CustomConnection
from utils.skill import Skill
from utils.mode import Mode
from utils.tool_utils import run_language_skill, build_request_path

# Sentiment Analysis: sync & async support.
SYNC_INTER_PATH = "/language/:analyze-text"
ASYNC_INTER_PATH = "/language/analyze-text/jobs"
API_VERSION = "2023-04-15-preview"
SKILL = Skill.SENTIMENT_ANALYSIS
MODE = Mode.SYNC

# When `parse_response == True`, return string representing analyzed sentiment: either "positive", "neutral", or "negative".
# Else, return raw API json output.
@tool 
def get_sentiment_analysis(connection:CustomConnection, language:str, text:str, opinion_mining:bool=False, parse_response:bool=False) -> str: 
    # Create inputs:
    inputs = [ {"text": text, "language": language} ]

    # Create query parameters and request path:
    query_parameters = {
        "api-version": API_VERSION,
    }
    request_path = build_request_path(query_parameters)

    # Create task parameters:
    parameters = {
        "opinionMining": opinion_mining
    }

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
