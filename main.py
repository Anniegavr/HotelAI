import re
from rules import TOURIST_RULES, TOURIST_DATA
from production import forward_chain, backward_chaining
import questions


if __name__=='__main__':
    print('Backward chaining:')
    visitor_name = questions.get_name()
    questions.gather_tourist_data()
    print("One moment, please.")
    backward_chaining(TOURIST_RULES, TOURIST_DATA, visitor_name)
        # print('\n###############################################\nForward chaining: ')
    # conclusions = forward_chain(TOURIST_RULES, FORWARD_CHAIN_TOURIST_DATA)
    # print('Conclusion:')
    # for conclusion in conclusions:
    #     if re.search("Tourist", conclusion):
    #         print(conclusion)



