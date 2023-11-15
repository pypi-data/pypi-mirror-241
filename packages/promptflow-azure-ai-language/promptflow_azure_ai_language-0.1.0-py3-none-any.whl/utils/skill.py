from enum import Enum

# Supported skills:
class Skill(Enum):
    ABSTRACTIVE_SUMMARIZATION = 0
    EXTRACTIVE_SUMMARIZATION = 1
    CONVERSATION_SUMMARIZATION = 2
    PII = 4
    SENTIMENT_ANALYSIS = 5
    ENTITY_RECOGNITION = 6
    KEY_PHRASE_EXTRACTION = 7
    LANGUAGE_DETECTION = 8
    CONVERSATIONAL_LANGUAGE_UNDERSTANDING = 9
    TRANSLATE = 10

    @staticmethod
    def to_str(skill):
        return skill_to_str_dict.get(skill, "Unsupported")

    # Does skill deal with conversations rather than documents?
    @staticmethod
    def is_conversational(skill):
        return skill == Skill.CONVERSATION_SUMMARIZATION

skill_to_str_dict = {
    Skill.ABSTRACTIVE_SUMMARIZATION: "AbstractiveSummarization",
    Skill.EXTRACTIVE_SUMMARIZATION: "ExtractiveSummarization",
    Skill.CONVERSATION_SUMMARIZATION: "ConversationalSummarizationTask",
    Skill.PII: "PiiEntityRecognition",
    Skill.SENTIMENT_ANALYSIS: "SentimentAnalysis",
    Skill.ENTITY_RECOGNITION: "EntityRecognition",
    Skill.KEY_PHRASE_EXTRACTION: "KeyPhraseExtraction",
    Skill.LANGUAGE_DETECTION: "LanguageDetection",
    Skill.CONVERSATIONAL_LANGUAGE_UNDERSTANDING: "Conversation",
    Skill.TRANSLATE: "Translate"
}
