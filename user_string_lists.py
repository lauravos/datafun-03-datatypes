"""
Modify this docstring.

"""
#imports

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)


#Lists......................................................................................................................

cat_breed_list = ["Domestic", "Siamese", "Maine Coon", "Persian", "Ragdoll", "Bengal", "Sphynx"]

coat_colors_list = ["white", "black", "orange", "gray", "calico", "tortiseshell", "tabby", "black and white"]

adult_cat_weights = [7.2, 11, 9.4, 8.1, 15.8, 17, 11.6, 6.8, 9.5]

cat_ages = ["kitten", "junior", "adult", "senior", "super senior"]

acquisition = ["animal shelter", "stray", "breeder", "family/friend", "rescue", "existing household cat"]


#1. Using Python Built-in Functions ..................................................................................

#len(), set(), and zip() to combine 2 or more lists into tuples.
def combine_into_tuple():
    new_list = list(set(adult_cat_weights))
    tuple_a = list(zip(cat_breed_list, coat_colors_list, acquisition))
    logger.info(tuple_a)

    logger.info(f"length of tuple is: {len(tuple_a)}")



#2. Random Choice......................................................................................................

def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    # e.g. "The angry dog runs quickly."
    sentence = (f"The {random.choice(coat_colors_list)} cat weighs {random.choice(adult_cat_weights)} lbs")
    logger.info(sentence)

    sentence2 = (f"The {random.choice(cat_breed_list)} cat came from a/an {random.choice(acquisition)}")
    logger.info(sentence2)



#3. Get Unique Words................................................................................................

def unique_words():
    with open("text_names_in.txt") as file_object:
        word_list = list(set(file_object.read().split()))    
        word_list.sort()
        logger.info(word_list)

        # length of the list
        len_list = len(word_list)
        logger.info(f"The len() is {len_list}")



# call functions and execute code
# use if __name__ == "__main__":
if __name__ == "__main__":
    logger.info("Using Python Built-in Functions ..................................................................................")
    combine_into_tuple()
    logger.info("Random Choice......................................................................................................")
    create_random_sentence()
    logger.info("Get Unique Words...................................................................................................")
    unique_words()


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

show_log()