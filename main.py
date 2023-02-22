from rules import TOURIST_RULES, TOURIST_DATA
from production import forward_chain, both_chaining
import questions


if __name__=='__main__':
    visitor_name = questions.get_name()
    choice = input('Which approach would you like to see? Backward = B | Forward = F\n')
    if choice == 'B':
        DATA = []
        chosen = questions.select_tourist()
        DATA.append(chosen)
        print(DATA)
        both_chaining(TOURIST_RULES, DATA, visitor_name)
    elif choice == 'F':
        questions.gather_tourist_data()
    # ourist_data()
        both_chaining(TOURIST_RULES, TOURIST_DATA, visitor_name)


