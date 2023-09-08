"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics 

# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)


def illustrate_tuples():
    """This function illustrates tuples in Python."""

#Practice with Tuples.........................................................................................................
# Create some tuples
    tuple_a = ("Domestic", "Siamese", "Maine Coon")
    tuple_b = ("Persian", "Ragdoll", "Bengal", "Sphynx")


    logger.info(f"tuple_a = {tuple_a}")
    logger.info(f"tuple_b = {tuple_b}")

#concacetation
    Concac_tuple = tuple_a + tuple_b

#repetition
    tuple_a_twice = tuple_a * 2


    logger.info(f"{tuple_a  = }")
    logger.info(f"{tuple_b  = }")
    logger.info(f"{Concac_tuple  = }")
    logger.info(f"{tuple_a_twice = }")

#other tuple practice
    # tuple membership testing

    memb_test_tuple = (3, 6, 9, 12, 15)
    has9 = 9 in memb_test_tuple  # True
    has13 = 13 in memb_test_tuple  # False

    logger.info(has9)
    logger.info(has13)

    # tuple indexing (0 is first, -1 is last, or 1 less than the length)

    my_tuple = (1, 2, 3)
    first = my_tuple[0]
    second = my_tuple[1]
    third = my_tuple[2]
    last = my_tuple[-1]

    # Use tuples to return multiple values from a function

    def divide_and_remainder(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        logger.info(f"Quotient: {quotient}, Remainder: {remainder}")

    divide_and_remainder(21, 6)
    divide_and_remainder(53, 9)



#Sets.......................................................................................................................

def illustrate_sets():
    
    male_cat_weights = {11.8, 19.2, 14.1, 17.9, 22.5, 14, 18.7, 12.3, 9.6, 10.2}
    female_cat_weights = {9.6, 8.4, 12, 10.5, 8.7, 15, 10.3, 11.5, 15.1, 7}

    logger.info(f"male_cat_weights = {male_cat_weights}")
    logger.info(f"female_cat_weights = {female_cat_weights}")

    # set intersection
    intersected_set = male_cat_weights & female_cat_weights
    logger.info(f"the intersection of the sets of data for male and female cat weights is: {intersected_set}")

    # set union
    union_set = male_cat_weights | female_cat_weights
    logger.info(f"the union of the sets of data for male and female cat weights is: {union_set}")


#Dictionaries....................................................................................................................

def illustrate_dictionaries():
    catA_dict = {"breed": "Domestic", "gender": "M", "weight(lbs)": 12.5}
    catB_dict = {"breed": "Siamese", "gender": "F", "weight(lbs)": 9.1}

    logger.info(f"catA_dict = {catA_dict}")
    logger.info(f"catB_dict = {catB_dict}")

     #membership testing
    if "gender" in catA_dict:
        logger.info("yes")

    assessment_dict = {"low": 0, "medium": 1, "high": 2}
    logger.info(f"assessment_dict = {assessment_dict}")

    
    data_dict = {"Cat breed": ["Siamese", "Domestic", "Maine Coon"], "Gender": ["M", "F", "M"], "weight": [10.5, 8.9, 19.8],}
    logger.info(f"data_dict = {data_dict}")


#Use a dictionary to create key-value pairs of each word and its count from a file. 
    #as loop
    with open("text_juliuscaesar.txt") as file_object:
        word_list = file_object.read().split()

    word_count_dict = {}
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    logger.info(f"In text_juliuscaesar.txt, the word count for each word is: {word_count_dict}")
    logger.info("...........................................................................................................................")
    #dictionary comprehension
    word_count_dict_comprehension = {word: word_list.count(word) for word in word_list}
    logger.info(f"using the dictionary comprehensions method, the word count for each word in text_juliuscaesar.txt is: {word_count_dict}")
   



def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

show_log()

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    logger.info(f"Practice with tuples......................................................................................................")
    illustrate_tuples()
    logger.info("practice with sets.........................................................................................................")
    illustrate_sets()
    logger.info("practice with dictionaries.................................................................................................")
    illustrate_dictionaries()


    show_log()

