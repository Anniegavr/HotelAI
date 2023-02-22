from rules import TOURIST_RULES, BACKWARD_CHAIN_TOURIST_DATA, TOURIST_DATA
def get_name():
    return input('What is your name? ')

def gather_tourist_data():
    tourist_answers = ask_questions()
    for rule in tourist_answers.keys():
        if tourist_answers[rule] == True:
            #rule example: map_needed
            TOURIST_DATA.append(rule)
    
    print("Obtained data: ")
    print(TOURIST_DATA)

def ask_questions():
    done_asking = False
    questions = {
        '(?x) needs a map of the city or one of its parts': 'Do you need a map of the city or one of its parts? (yes/no) ',
        '(?x) needs a specific places info': 'Do you need information about specific places? (yes/no) ',
        '(?x) has a pro camera on him': 'Do you have a professional camera with you? (yes/no) ',
        '(?x) wants to borrow a pro camera': 'or do you want to borrow one? (yes/no) ',
        '(?x) has lots of luggages': 'Do you have lots of luggage? (yes/no) ',
        '(?x) wants a list of  shops and their info': 'Do you want a list of shops and their information? (yes/no) ',
        '(?x) needs a list of local foods': 'Would you like to get a list of local foods to try? (yes/no) ',
        '(?x) is interested in a list of restaurants':'Do you want a list of local restaurants and their information? (yes/no) ',
        '(?x) wants a list of  cultural sites and their info': 'Do you want a list of cultural sites and their information? (yes/no) ',
        '(?x) wants a list of souvenirs and where to find them': 'Do you want a list of souvenirs and where to find them? (yes/no) ',
        '(?x) takes the luxury room': 'Do you prefer a luxury room? (yes/no) '
    }

    # Store the answers to questions in a dictionary
    answers = {}
    answer = input('Welcome to our hotel! Do you need help with anything? (yes/no) ')
    if answer.lower() == 'yes':
        help_needed = True

    if help_needed:
        answer = input(questions['(?x) wants a list of  cultural sites and their info'])
        if answer.lower() == 'yes':
            answers['(?x) wants a list of  cultural sites and their info'] = True
            ############################################################################
            answer = input(questions['(?x) needs a map of the city or one of its parts'])
            if answer.lower() == 'yes':
                # answers['(?x) needs a map of the city or one of its parts'] = True
                answers['(?x) came to explore'] = True
                answer = input(questions['(?x) needs a specific places info'])
                if answer.lower() == 'yes':
                    answers['(?x) needs a specific places info'] = True
                else:
                    answers['(?x) needs a specific places info'] = False
                ############################################################################
                answer = input(questions['(?x) is interested in a list of restaurants'])
                if answer.lower() == 'yes':
                    answers['(?x) is interested in a list of restaurants'] = True
                else:
                    answers['(?x) is interested in a list of restaurants'] = False
                    ############################################################################
                    answer = input(questions['(?x) wants a list of  shops and their info'])
                    if answer.lower() == 'yes':
                        answers['(?x) wants a list of  shops and their info'] = True
                        ############################################################################
                        answer = input(questions['(?x) has lots of luggages'])
                        if answer.lower() == 'yes':
                            answers['(?x) has lots of luggages'] = True
                            ############################################################################
                            answer = input(questions['(?x) wants a list of souvenirs and where to find them'])
                            if answer.lower() == 'yes':
                                answers['(?x) wants a list of souvenirs and where to find them'] = True
                            else:
                                answers['(?x) wants a list of souvenirs and where to find them'] = False
                        else:
                            answers['(?x) has lots of luggages'] = False
                    else:
                        answers['(?x) wants a list of  shops and their info'] = False
            else:
                answers['(?x) needs a map of the city or one of its parts'] = False
                ############################################################################
                answer = input(questions['(?x) has a pro camera on him'])
                if answer.lower() == 'yes':
                    answers['(?x) has a pro camera on him'] = True
                    answers['(?x) is Photography Fan Tourist'] = True
                else:
                    answers['(?x) has a pro camera on him'] = False
                    answer = input(questions['(?x) wants to borrow a pro camera'])
                    if answer.lower() == 'yes':
                        # answers['(?x) wants to borrow a pro camera'] = True
                        answers['(?x) is Photography Fan Tourist'] = True
                        
                    else:
                        answers['(?x) wants to borrow a pro camera'] = False
                        ############################################################################
                        answer = input(questions['(?x) wants a list of  shops and their info'])
                        if answer.lower() == 'yes':
                            answers['(?x) wants a list of  shops and their info'] = True
                            ############################################################################
                            answer = input(questions['(?x) has lots of luggages'])
                            if answer.lower() == 'yes':
                                # answers['(?x) has lots of luggages'] = True
                                answers['(?x) is prepared to spend money'] = True
                                ############################################################################
                                answer = input(questions['(?x) wants a list of souvenirs and where to find them'])
                                if answer.lower() == 'yes':
                                    # answers['(?x) wants a list of souvenirs and where to find them'] = True
                                    answers['(?x) is a Collectionist Tourist'] = True
                                else:
                                    answers['(?x) wants a list of souvenirs and where to find them'] = False
                            else:
                                answers['(?x) has lots of luggages'] = False
                        else:
                            answers['(?x) wants a list of  shops and their info'] = False

        else:
            answers['(?x) wants a list of  cultural sites and their info'] = False     
        # if (answers.get('(?x) has lots of luggages') and answers.get('(?x) wants a list of  shops and their info') 
        #     and answers.get('(?x) wants a list of  cultural sites and their info') and not answers.get('(?x) wants a list of souvenirs and where to find them')):
        #     answer = input(questions['(?x) wants a list of souvenirs and where to find them'])
        #     if answer.lower() == 'yes':
        #         answers['(?x) wants a list of souvenirs and where to find them'] = True
        #     else:
        #         answers['(?x) wants a list of souvenirs and where to find them'] = False
        print("Thank you for your time. One of our operators will provide you with everything you need in a few minutes.")
    return answers