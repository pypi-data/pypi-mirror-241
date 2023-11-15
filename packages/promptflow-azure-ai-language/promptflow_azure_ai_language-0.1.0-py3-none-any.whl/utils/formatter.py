from utils.skill import Skill 
from utils.mode import Mode
from utils.formatter_utils import generate_format_func

# 'Formatter' class deals with logic related to formatting API input for different skills. 
class Formatter():

    def __init__(self, skill:Skill, mode:Mode):
        self.skill = skill 
        self.mode = mode 
        # Function used to format input.
        self.format_func = generate_format_func(self.skill, self.mode)
    
    # Updates Formatter's skill.
    def set_skill(self, skill:Skill):
        self.skill = skill 
        self.format_func = generate_format_func(self.skill, self.mode)

    # Updates Formatter's mode.
    def set_mode(self, mode:Mode):
        self.mode = mode 
        self.format_func = generate_format_func(self.skill, self.mode)

    # Formats inputs.
    def format(self, inputs:list, parameters:dict) -> dict:
        return self.format_func(inputs, parameters)
    