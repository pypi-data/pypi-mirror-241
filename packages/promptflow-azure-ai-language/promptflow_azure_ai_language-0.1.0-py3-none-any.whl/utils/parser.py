from utils.skill import Skill 
from utils.mode import Mode 
from utils.parser_utils import is_response_error, generate_results_func, generate_inter_func, generate_parser_func

# `Parser` class deals with logic related to parsing API responses for different skills.
class Parser():

    def __init__(self, skill:Skill, mode:Mode):
        self.set_mode(mode)
        self.set_skill(skill)

    # Updates Parser's mode.
    def set_mode(self, mode:Mode):
        self.mode = mode
        # Function to obtain 'results' field of response.
        self.results_func = generate_results_func(self.mode)
      
    # Updates Parser's skill.
    def set_skill(self, skill:Skill):
        self.skill = skill
        # Function to obtain single task result based on if input was a document or conversation.
        self.inter_func = generate_inter_func(self.skill)
        # Function to parse task result based on skill.
        self.parser_func = generate_parser_func(self.skill)
    
    # Parses API response according to skill and mode.
    def parse_response(self, response):
        if is_response_error(response):
            return "ERROR"
        
        # If parsing error occurs, full API output is still printed beforehand, so return error.
        try:
            results = self.results_func(response)
            task_result = self.inter_func(results)
            return self.parser_func(task_result)
        except:
            return "ERROR"
        