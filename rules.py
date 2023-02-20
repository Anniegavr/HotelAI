from production import IF, AND, THEN, OR, DELETE, NOT, FAIL
from production import IF, AND, THEN, FAIL, OR

TOURIST_RULES = (
###################################### Loonie ######################################
    IF( AND( '(?x) does not need a map',
             '(?x) does not have lots of luggages' ),                                   # R0
        THEN( '(?x) is a Loonie')),
###################################### Potential Tourist ############################
    IF( OR( '(?x) needs a map of the city or one of its parts',
             '(?x) needs a specific places info'),                                    # R1
        THEN( '(?x) came to explore' )),
   
    IF( OR('(?x) has a pro camera on him',
            '(?x) wants to borrow a pro camera'),                                       # R2
        THEN( '(?x) is Photography Fan Tourist' )),
    
    IF( AND('(?x) has lots of luggages',
            '(?x) wants a list of  shops and their info'),                              # R3
        THEN( '(?x) is prepared to spend money' )),
###################################### Photo Fan Tourist ##############################
    IF( AND('(?x) came to explore',              
            '(?x) needs a list of local foods'),                                        # R4
        THEN( '(?x) is interested in a list of restaurants' )),
###################################### Shopping Tourist ###############################
    IF( AND( '(?x) came to explore',        
             '(?x) is prepared to spend money' ),                                             # R5
        THEN( '(?x) is a Shopping Tourist' )),
###################################### Culture Enthusiast Tourist #####################   
    IF( AND( '(?x) is interested in a list of restaurants',                             # R6
             '(?x) came to explore',
             '(?x) wants a list of  cultural sites and their info'),
        THEN( '(?x) is a Discover Culture Tourist')),
###################################### Rich Tourist ###################################
    IF( AND( '(?x) is prepared to spend money',                                            # R7
             '(?x) takes the luxury room' ),
        THEN( '(?x) is a Rich Tourist' )),
###################################### Collectionist Tourist ##########################
    IF( AND( '(?x) is prepared to spend money',                                            # R8
             '(?x) wants a list of souvenirs and where to find them' ),
        THEN( '(?x) is a Collectionist Tourist' )),
)

BACKWARD_CHAIN_TOURIST_DATA = (
    'touri is a Rich Tourist', #photo tourist
)

FORWARD_CHAIN_TOURIST_DATA = (
    'mark needs a map of the city or one of its parts',
    'mark needs a specific places info', ###explore
    'mark is prepared to spend money',
    
    'tourette takes the luxury room', #luxury tourist
    'tourette wants a list of  shops and their info',
    'tourette has lots of luggages',
    )