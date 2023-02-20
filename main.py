import re
from rules import TOURIST_RULES, BACKWARD_CHAIN_TOURIST_DATA, FORWARD_CHAIN_TOURIST_DATA
from production import forward_chain, backward_chaining

if __name__=='__main__':
    print('Backward chaining:')
    backward_chaining(TOURIST_RULES, BACKWARD_CHAIN_TOURIST_DATA)
    print('\n###############################################\nForward chaining: ')
    conclusions = forward_chain(TOURIST_RULES, FORWARD_CHAIN_TOURIST_DATA)
    print('Conclusion:')
    for conclusion in conclusions:
        if re.search("Tourist", conclusion):
            print(conclusion)