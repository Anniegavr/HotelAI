# TODO: add your imports here:
# from rules import my_rules
from rules import TOURIST_RULES
from production import forward_chain, backward_chaining

if __name__=='__main__':

    # hypothesis = 'You are a Culture Enthusiast Tourist'
    goals = ["tim is a bird"]
    backward_chaining(TOURIST_RULES, goals);