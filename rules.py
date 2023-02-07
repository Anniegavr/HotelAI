from production import IF, AND, THEN, OR, DELETE, NOT, FAIL
from production import IF, AND, THEN, FAIL, OR

TOURIST_TYPES = (
    'ADVENTURE_TOURIST',
    'CULTURE_TOURIST',
    'LUXURY_TOURIST',
    'NATURE_TOURIST',
    'BEACH_TOURIST'
)

## TOURIST_RULES
TOURIST_RULES = (
###################################### Loonie ######################################
    IF( AND( '(?x) does not need a map',
             '(?x) does not have lots of luggages' ),                                   # R0
        THEN( '(?x) is a Loonie')),
###################################### Potential Tourist ############################
    IF( OR( '(?x) needs a map of the city or one of its parts',
             '(?x) needs a specific place\'s info'),                                    # R1
        THEN( '(?x) came to explore' )),
   
    IF( OR('(?x) has a pro camera on him',
            '(?x) wants to borrow a pro camera'),                                       # R2
        THEN( '(?x) is photography fan tourist' )),
    
    IF( AND('(?x) has lots of luggages',
            '(?x) wants a list of  shops and their info'),                              # R3
        THEN( '(?x) is prepared to spend $$' )),
###################################### Photo Fan Tourist ##############################
    IF( AND('(?x) came to explore',              
            '(?x) Needs a list of local foods'),                                        # R4
        THEN( '(?x) is interested in a list of restaurants' )),
###################################### Shopping Tourist ###############################
    IF( AND( '(?x) came to explore',        
             '(?x) Prepared to spend $$' ),                                             # R5
        THEN( '(?x) is a Shopping Tourist' )),
###################################### Culture Enthusiast Tourist #####################   
    IF( AND( '(?x) is interested in a list of restaurants',                             # R6
             '(?x) came to explore',
             '(?x) wants a list of  cultural sites and their info'),
        THEN( '(?x) is a Discover Culture Tourist')),
###################################### Rich Tourist ###################################
    IF( AND( '(?x) is prepared to spend $$',                                            # R7
             '(?x) takes the luxury room' ),
        THEN( '(?x) is a Rich Tourist' )),
###################################### Collectionist Tourist ##########################
    IF( AND( '(?x) is prepared to spend $$',                                            # R8
             '(?x) wants a list of souvenirs and where to find them' ),
        THEN( '(?x) is a Collectionist Tourist' ))
)


TOURIST_DATA = (
    'tourist_1 collect souvenirs' # that are culturally significant', #culture tourist
    'tourist_1 knows about local culture',
    'tourist_1 wants view to the touristic site',
    'tourist_2 goes on adventures', #adventure tourist
    'tourist_2 wants to try local dishes',
    'tourist_2 carries adventure gear',
    'tourist_3 wants a luxury room', #luxury tourist
    'tourist_3 shops for luxury brands',
    'tourist_4 stays mostly at the beach', #beach tourist
    'tourist_4 wants or has swimwear',
    'tourist_4 wants or has swimming gear',
    'tourist_5 wants or has binoculars', #nature tourist
    'tourist_5 cares about the environment',
    'tourist_5 wants to explore the parks, the forest and the natural reservation'
    )