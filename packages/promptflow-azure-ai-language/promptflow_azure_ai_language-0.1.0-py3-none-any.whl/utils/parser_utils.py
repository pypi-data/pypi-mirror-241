from utils.skill import Skill
from utils.mode import Mode

# Obtains 'results' field from an async response with a single task.
def get_async_results(response):
    json_res = response.json()
    return json_res["tasks"]["items"][0]["results"]
    
# Obtains 'results' field from an sync response.
def get_sync_results(response):
    json_res = response.json()
    if "results" in json_res:
        return json_res["results"]
    else:
        return json_res

# Abstractive Summarization: async only.
# Return string of summary.
def parse_abstractive_summarization(doc_result:dict) -> str:
    return doc_result["summaries"][0]["text"]

# Extractive Summarization: async only.
# Return list of strings of extracted summaries.
def parse_extractive_summarization(doc_result:dict) -> list[str]:
    sentences = doc_result["sentences"]       
    return [s["text"] for s in sentences]

# Conversation Summarization: async only.
# Return string of summary of conversation.
def parse_conversation_summarization(conv_result:dict) -> str:
    return conv_result["summaries"][0]["text"]

# PII Entity Recognition: sync & async support.
# Return string of redacted text (removes all PII entities).
def parse_pii(doc_result:dict) -> str:
    return doc_result["redactedText"]

# Sentiment Analysis: sync & async support.
# Return sentiment as string: one of {positive, neutral, negative}.
def parse_sentiment_analysis(doc_result:dict) -> str:
    return doc_result["sentiment"]

# Language detection: sync only.
# Return code of language detected.
def parse_language_detection(doc_result:dict) -> str:
    return doc_result["detectedLanguage"]["iso6391Name"] 

# KeyPhrase Extraction: sync & async support.
# Return list of strings of extracted key-phrases.
def parse_keyphrase_extraction(doc_result:dict) -> list[str]:
    return doc_result["keyPhrases"]

# Entity Recognition: sync & async support.
# Return dictionary of recognized entities: key=<entity text>, value=<entity category>.
def parse_entity_recognition(doc_result:dict) -> dict[str, str]:
    entities = doc_result["entities"]
    recognized_entities = {}
    for entity in entities:
        recognized_entities[entity["text"]] = entity["category"]
    return recognized_entities

# Conversational Language Understanding: sync only.
# Return list of dictionaries with the user utterance and the associated intent.
def parse_conversational_language_understanding(clu_result:dict) -> dict[str, str]:
    utterance = clu_result["query"]
    top_intent = clu_result["prediction"]["topIntent"]
    return { "utterance": utterance, "intent": top_intent }

# Translation: sync only.
# Return dictionary of translations: key=<to-language>, value=<translated-text>
def parse_translate(translations:list[dict]) -> dict[str, str]:
    parsed_translations = {}
    for translation in translations:
        parsed_translations[translation["to"]] = translation["text"]
    return parsed_translations

# Checks for a bad response, e.g. status_code != 200.
def is_response_error(response) -> bool:
    return response.status_code != 200
        
# Generate results func based on mode.
def generate_results_func(mode:Mode):
    return get_sync_results if mode == Mode.SYNC else get_async_results

# Generate function to obtain single task result based on if input was a document or conversation.
# For Conversational Language Understanding the task result with query and prediction is under the "result" property
# https://learn.microsoft.com/en-us/rest/api/language/2023-04-01/conversation-analysis-runtime/analyze-conversation?tabs=HTTP#conversation-project-result
def generate_inter_func(skill:Skill):
    if Skill.is_conversational(skill):
        return lambda results: results["conversations"][0]
    elif skill == Skill.CONVERSATIONAL_LANGUAGE_UNDERSTANDING:
        return lambda results: results["result"]
    elif skill == Skill.TRANSLATE:
        return lambda results: results[0]["translations"]
    else:
        return lambda results: results["documents"][0]

skill_to_parser_func_dict = {
    Skill.ABSTRACTIVE_SUMMARIZATION: parse_abstractive_summarization,
    Skill.EXTRACTIVE_SUMMARIZATION: parse_extractive_summarization,
    Skill.CONVERSATION_SUMMARIZATION: parse_conversation_summarization,
    Skill.PII: parse_pii,
    Skill.SENTIMENT_ANALYSIS: parse_sentiment_analysis,
    Skill.ENTITY_RECOGNITION: parse_entity_recognition,
    Skill.KEY_PHRASE_EXTRACTION: parse_keyphrase_extraction,
    Skill.LANGUAGE_DETECTION: parse_language_detection,
    Skill.CONVERSATIONAL_LANGUAGE_UNDERSTANDING: parse_conversational_language_understanding,
    Skill.TRANSLATE: parse_translate
}

# Generate specific parsing function based on skill.
def generate_parser_func(skill:Skill):
    return skill_to_parser_func_dict.get(skill, lambda _: "Unrecognized skill")
        