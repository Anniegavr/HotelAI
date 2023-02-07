# TODO: add your imports here:
# from rules import my_rules
from rules import TOURIST_RULES, TOURIST_DATA
from production import forward_chain, backward_chain

if __name__=='__main__':

    # print(forward_chain(TOURIST_RULES, TOURIST_DATA, verbose=True))
    print(backward_chain(TOURIST_RULES, TOURIST_DATA, verbose=True))