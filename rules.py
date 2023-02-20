# from production import IF, AND, THEN, OR, DELETE, NOT, FAIL
# from production import IF, AND, THEN, FAIL, OR

# TOURIST_TYPES = (
#     'ADVENTURE_TOURIST',
#     'CULTURE_TOURIST',
#     'LUXURY_TOURIST',
#     'NATURE_TOURIST',
#     'BEACH_TOURIST'
# )

# ## TOURIST_RULES
# TOURIST_RULES = (
#     ###################################### Loonie ######################################
# #     IF( AND( 'You do not need a map',
# #         'You do not have lots of luggages' ), # R0
# #         THEN( 'You are a Loonie')),
# #     ###################################### Potential Tourist ############################
# #     IF( OR( 'You need a map of the city or one of its parts',
# #             'You need a specific place\'s info'), # R1
# #         THEN( 'You came to explore' )),
# #     IF( OR('You have a pro camera on you',
# #             'You want to borrow a pro camera'),                                       # R2
# #         THEN( 'You are photography fan tourist' )),

# #     IF( AND('You have lots of luggages',
# #             'You want a list of  shops and their info'),                              # R3
# #         THEN( 'You are prepared to spend $$' )),
# #     ###################################### Photo Fan Tourist ##############################
# #     IF( AND('You came to explore',
# #             'You need a list of local foods'), # R4
# #         THEN( 'You are interested in a list of restaurants' )),
# #     ###################################### Shopping Tourist ###############################
# #     IF( AND( 'You came to explore',
# #             'You are prepared to spend $$' ), # R5
# #         THEN( 'You are a Shopping Tourist' )),
# #     ###################################### Culture Enthusiast Tourist #####################
# #     IF( AND( 'You are interested in a list of restaurants', # R6
# #             'You came to explore',
# #             'You want a list of cultural sites and their info'),
# #         THEN( 'You are a Culture Enthusiast Tourist')),
# #     ###################################### Rich Tourist ###################################
# #     IF( AND( 'You are prepared to spend $$', # R7
# #             'You take the luxury room' ),
# #         THEN( 'You are a Rich Tourist' )),
# #     ###################################### Collectionist Tourist ##########################
# #     IF( AND( 'You are prepared to spend $$', # R8
# #             'You want a list of souvenirs and where to find them' ),
# #         THEN( 'You are a Collectionist Tourist' ))
# # # --------------------------------------------------------------------------------------------------

# ###################################### Loonie ######################################
#     IF( AND( '(?x) does not need a map',
#              '(?x) does not have lots of luggages' ),                                   # R0
#         THEN( '(?x) is a Loonie')),
# ###################################### Potential Tourist ############################
#     IF( OR( '(?x) needs a map of the city or one of its parts',
#              '(?x) needs a specific place\'s info'),                                    # R1
#         THEN( '(?x) came to explore' )),
   
#     IF( OR('(?x) has a pro camera on him',
#             '(?x) wants to borrow a pro camera'),                                       # R2
#         THEN( '(?x) is photography fan tourist' )),
    
#     IF( AND('(?x) has lots of luggages',
#             '(?x) wants a list of  shops and their info'),                              # R3
#         THEN( '(?x) is prepared to spend $$' )),
# ###################################### Photo Fan Tourist ##############################
#     IF( AND('(?x) came to explore',              
#             '(?x) needs a list of local foods'),                                        # R4
#         THEN( '(?x) is interested in a list of restaurants' )),
# ###################################### Shopping Tourist ###############################
#     IF( AND( '(?x) came to explore',        
#              '(?x) Prepared to spend $$' ),                                             # R5
#         THEN( '(?x) is a Shopping Tourist' )),
# ###################################### Culture Enthusiast Tourist #####################   
#     IF( AND( '(?x) is interested in a list of restaurants',                             # R6
#              '(?x) came to explore',
#              '(?x) wants a list of  cultural sites and their info'),
#         THEN( '(?x) is a Discover Culture Tourist')),
# ###################################### Rich Tourist ###################################
#     IF( AND( '(?x) is prepared to spend $$',                                            # R7
#              '(?x) takes the luxury room' ),
#         THEN( '(?x) is a Rich Tourist' )),
# ###################################### Collectionist Tourist ##########################
#     IF( AND( '(?x) is prepared to spend $$',                                            # R8
#              '(?x) wants a list of souvenirs and where to find them' ),
#         THEN( '(?x) is a Collectionist Tourist' )),
# )


# TOURIST_DATA = (
#     'tour is a Loonie',
#     'tour does not have lots of luggages',
#     'does not need a map',
#     'You are prepared to spend $$',
#     # 'You came to explore'
#     # 'touri is a Rich Tourist' #photo tourist
#     # 'tourette takes the luxury room', #luxury tourist
#     # 'tourette wants a list of  shops and their info',
#     # 'tourette has lots of luggages', #beach tourist
#     # 'tourist_4 wants or has swimwear',
#     # 'tourist_4 wants or has swimming gear',
#     # 'tourist_5 wants or has binoculars', #nature tourist
#     # 'tourist_5 cares about the environment',
#     # 'tourist_5 wants to explore the parks, the forest and the natural reservation',
#     )

from production import IF, AND, THEN, FAIL, OR

## ZOOKEEPER RULES
TOURIST_RULES = [
    
    IF( AND( '(?x) has hair' ),         # Z1
        THEN( '(?x) is a mammal' )),
   
    IF( AND( '(?x) gives milk' ),       # Z2
        THEN( '(?x) is a mammal' )),
    
    IF( AND( '(?x) has feathers' ),     # Z3
        THEN( '(?x) is a bird' )),
   
    IF( AND( '(?x) flies',              # Z4
             '(?x) lays eggs' ),
        THEN( '(?x) is a bird' )),
   
    IF( AND( '(?x) is a mammal',        # Z5
             '(?x) eats meat' ),
        THEN( '(?x) is a carnivore' )),
   
    IF( AND( '(?x) is a mammal',        # Z6
             '(?x) has pointed teeth',
             '(?x) has claws',
             '(?x) has forward-pointing eyes' ),
        THEN( '(?x) is a carnivore' )),
    
    IF( AND( '(?x) is a mammal',        # Z7
             '(?x) has hoofs' ),
        THEN( '(?x) is an ungulate' )),
    
    IF( AND( '(?x) is a mammal',        # Z8
             '(?x) chews cud' ),
        THEN( '(?x) is an ungulate' )),
    
    IF( AND( '(?x) is a carnivore',     # Z9
             '(?x) has tawny color',
             '(?x) has dark spots' ),
        THEN( '(?x) is a cheetah' )),
    
    IF( AND( '(?x) is a carnivore',     # Z10
             '(?x) has tawny color',
             '(?x) has black stripes' ),
        THEN( '(?x) is a tiger' )),
    
    IF( AND( '(?x) is an ungulate',     # Z11
             '(?x) has long legs',
             '(?x) has long neck',
             '(?x) has tawny color',
             '(?x) has dark spots' ),
        THEN( '(?x) is a giraffe' )),
    
    IF( AND( '(?x) is an ungulate',     # Z12
             '(?x) has white color',
             '(?x) has black stripes' ),
        THEN( '(?x) is a zebra' )),
    
    IF( AND( '(?x) is a bird',          # Z13
             '(?x) does not fly',
             '(?x) has long legs',
             '(?x) has long neck',
             '(?x) has black and white color' ),
        THEN( '(?x) is an ostrich' )),
    
    IF( AND( '(?x) is a bird',          # Z14
             '(?x) does not fly',
             '(?x) swims',
             '(?x) has black and white color' ),
        THEN( '(?x) is a penguin' )),
    
    IF( AND( '(?x) is a bird',        # Z15
             '(?x) is a good flyer' ),
        THEN( '(?x) is an albatross' )),
    
]


   
ZOO_DATA = (
    'tim has feathers',
    'tim is a good flyer',
    'mark flies',
    'mark does not fly',
    'mark lays eggs',
    'mark swims',
    'mark has black and white color',
    )

