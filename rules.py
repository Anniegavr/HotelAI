from production import IF, AND, THEN, OR, DELETE, NOT, FAIL
from production import IF, AND, THEN, FAIL, OR

TOURIST_RULES = (
    IF('(?x) does not need a map', THEN('(?x) is a Loonie')),  # R0
    IF(OR('(?x) needs a map of the city or one of its parts',
          '(?x) needs a specific places info'),
       THEN('(?x) came to explore')),  # R1
    IF(OR('(?x) has a pro camera on them',
          '(?x) wants to borrow a pro camera'),
       THEN('(?x) is Photography Fan Tourist')),  # R2 (fixing implementation)
    IF(AND('(?x) has lots of luggages',
           '(?x) wants a list of  shops and their info'),
       THEN('(?x) is prepared to spend money')),  # R3
    IF(AND('(?x) came to explore',
           '(?x) needs a list of local foods'),
       THEN('(?x) is interested in a list of restaurants')),  # R4
    IF(AND('(?x) came to explore',
           '(?x) is prepared to spend money'),
       THEN('(?x) is a Shopping Tourist')),  # R5
    IF(AND('(?x) is interested in a list of restaurants',
           '(?x) came to explore',
           '(?x) wants a list of  cultural sites and their info'),
       THEN('(?x) is a Discover Culture Tourist')),  # R6
    IF(AND('(?x) is prepared to spend money',
           '(?x) takes the luxury room'),
       THEN('(?x) is a Rich Tourist')),  # R7
    IF(AND('(?x) is prepared to spend money',
           '(?x) wants a list of souvenirs and where to find them'),
       THEN('(?x) is a Collectionist Tourist')),  # R8
)


BACKWARD_CHAIN_TOURIST_DATA = [
    # 'touri is a Shopping Tourist', #photo tourist
]

FORWARD_CHAIN_TOURIST_DATA = (
    'mark needs a map of the city or one of its parts',
    'mark needs a specific places info', ###explore
    'mark is prepared to spend money',
    
    'tourette takes the luxury room', #luxury tourist
    'tourette wants a list of  shops and their info',
    'tourette has lots of luggages',
)

TOURIST_DATA = []
