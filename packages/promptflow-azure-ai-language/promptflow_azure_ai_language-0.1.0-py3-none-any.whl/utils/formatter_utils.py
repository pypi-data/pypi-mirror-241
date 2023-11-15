import time
from utils.skill import Skill
from utils.mode import Mode

# Creates a simple task name given skill and id.
# e.g. "AbstractiveSummarization Task 1"
def create_task_name(skill:Skill, id:int) -> str:
    return Skill.to_str(skill) + " Task " + str(id)

# Formats a task with its kind, name, and id.
def format_task(task:dict, id:int) -> dict:
    skill = task["skill"]
    del task["skill"]
    task["kind"] = Skill.to_str(skill)
    task["taskName"] = create_task_name(skill, id)
    return task

# Formats a list of tasks given a list of {skill, parameters} dicts.
def format_tasks(tasks:list[dict]) -> list[dict]:
    formatted_tasks = [] 
    id = 1 
    for task in tasks:
        formatted_tasks.append(format_task(task, id))
        id += 1
    return formatted_tasks

# Formats a single document with its id given a {text, language} dict.
def format_document(doc:dict, id:int) -> dict:
    doc["id"] = id 
    return doc

# Formats a list of documents given a list of {text, language} dicts.
def format_documents(documents:list[dict]) -> list[dict]:
    formatted_documents = []
    id = 1
    for doc in documents:
        formatted_documents.append(format_document(doc, id))
        id += 1
    return formatted_documents 

# Creates a conversation item from a speaker's line and id.
def create_conversation_item(line:str, id:int) -> dict:
    name_and_text = line.split(":", maxsplit=1)
    name = name_and_text[0].strip()
    text = name_and_text[1].strip()
    return {
        "id": id, 
        "participantId": name,
        "role": "generic" if name.lower() != "customer" and name.lower() != "agent" else name,
        "text": text
    }

# Creates a list of conversation items from a conversation.
def create_conversation_items(text:str) -> list[dict]: 
    conversation_items = []
    id = 1
    lines = text.replace("  ", "\n").split("\n")
    lines = filter(lambda l: len(l.strip()) != 0, lines)
    for line in lines: 
        conversation_items.append(create_conversation_item(line, id))
        id += 1
    return conversation_items

# Formats a conversation from a {text, language, modality} dict and id.
def format_conversation(conv:dict, id:int) -> dict: 
    text = conv["text"]
    del conv["text"]
    conv["id"] = "input" + str(id)
    conv["conversationItems"] = create_conversation_items(text)
    return conv

# Formats a list of conversations from a list of {text, language, modality} dicts.
def format_conversations(convs:list[dict]) -> list[dict]:
    formatted_conversations = []
    id = 1 
    for conv in convs: 
        formatted_conversations.append(format_conversation(conv, id))
        id += 1 
    return formatted_conversations
    
# Function to obtain "analysisInput" field of API input based on skill.
def analysis_input_func(skill:Skill):
    if Skill.is_conversational(skill):
        return lambda inputs: { "conversations": format_conversations(inputs) }
    elif skill == Skill.CONVERSATIONAL_LANGUAGE_UNDERSTANDING:
        return lambda inputs: { "conversationItem" : get_clu_conversation_item(inputs[0]) }
    else: 
        return lambda inputs: { "documents": format_documents(inputs) }

# Function to format sync input based on skill.
def format_sync_func(skill:Skill):
    if skill == Skill.TRANSLATE:
        return lambda inputs, _: inputs
    return lambda inputs, parameters: {
        "kind": Skill.to_str(skill),
        "analysisInput": analysis_input_func(skill)(inputs),
        "parameters": parameters
    }

# Function to format async input based on skill.
def format_async_func(skill:Skill):
    return lambda inputs, parameters: {
        "displayName": Skill.to_str(skill) + " job: " + str(time.time()),
        "analysisInput": analysis_input_func(skill)(inputs),
        "tasks": format_tasks([{"skill": skill, "parameters": parameters}] * len(inputs))
    }

# Generate specific formatting function based on skill and mode.
def generate_format_func(skill:Skill, mode:Mode):
    return format_sync_func(skill) if mode == Mode.SYNC else format_async_func(skill) 

# Generate CLU Analysis Input
def get_clu_conversation_item(input):
    return {
        "id": "1",
        "participantId": "1",
        "modality": input["modality"],
        "language": input["language"],
        "text": input["text"]
    }
