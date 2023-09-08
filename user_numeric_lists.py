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


# TODO: Create some shared data lists if you like - or just create them in your functions

list1 = [7.2, 11, 9.4, 8.1, 15.8, 17, 11.6, 6.8, 9.5, 13.8, 21, 14.3, 12.5, 10.1, 19.6, 11.6, 10.1, 17.5, 13.4, 7.6, 6.7, 12.9, 10.4, 22.3 ,15]
logger.info(f"list1 is : {list1}")

listx = list(range(10))
logger.info(f"listx is : {listx}")

listy = [22, 23,  28, 29, 31, 33, 34, 37, 40, 41]
logger.info(f"listy is : {listy}")


# LIST STATISTICS: define mean, median, mode, variance, and standard deviation for list1..........
logger.info("LIST STATISTICS.......................................................................................................")

mean1 = statistics.mean(list1)
median1 = statistics.median(list1)
mode1 = statistics.mode(list1)
var1 = statistics.variance(list1)
stdev1 = statistics.stdev(list1)

logger.info(f"list1 mean: {mean1}")
logger.info(f"list1median: {median1}")
logger.info(f"list1 mode: {mode1}")
logger.info(f"list1 variance: {var1}")
logger.info(f"list1 standard deviation: {stdev1}")

meany = statistics.mean(listy)
mediany = statistics.median(listy)
modey = statistics.mode(listy)
vary = statistics.variance(listy)
stdevy = statistics.stdev(listy)

logger.info(f"listy mean: {meany}")
logger.info(f"listy median: {mediany}")
logger.info(f"listy mode: {modey}")
logger.info(f"listy variance: {vary}")
logger.info(f"listy standard deviation: {stdevy}")

#LISTS - CORRELATION AND PREDICTION....................
logger.info("LISTS - CORRELATION AND PREDICTION.....................................................................................")
'''Calculate the correlation between listx and listy
Calculate the slope and intercept of the best fit line. Hint: use statistics.linear_regression()
Set a future time = 15. 
Predict the y value at the future time  y = mx + b where m is the slope and b is the y intercept'''

logger.info(f"listx: {listx}")
logger.info(f"listy: {listy}")

# Descriptive: Measures of correlation

correlationxy = statistics.correlation(listx, listy)
logger.info(f"correlation between x and y: {correlationxy}")

slope, intercept = statistics.linear_regression(listx, listy)
logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")


newx = 15  # future x value

    # y = mx + b
newy = slope * newx + intercept
logger.info(f"We predict that when x = {newx}, y will be about {newy}")



def illustrate_list_built_in_functions():
    
 #LISTS - USING PYTHON BUILT-IN FUNCTIONS................
    logger.info("LISTS - USING PYTHON BUILT-IN FUNCTIONS..........................................................................")

    # Calcuate the max and min scores
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Given score list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {list1}")

    # Return a new list sorted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list sorted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}")



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )
    illustrate_list_built_in_functions()



#LIST METHODS...................................
logger.info("LIST METHODS.....................................................................................................")

#new list "lst"
lst = [4, 6, 2, 3, 10, 7]
logger.info(f"lst is: {lst}")

#append
lst.append(5)
logger.info(f"append 5 to lst: {lst}")

#extend
lst.extend([11,13])
logger.info(f"lst extended to inclued a new list: {lst}")

#insert
i = 0
newvalue = 15
lst.insert(i, newvalue)
logger.info(f"lst with value inserted (new value = 15): {lst}")

#remove the number 5
remove = 5
lst.remove(remove)
logger.info(f"lst wtih the number 5 removed: {lst}")

#count the times 2 appears
count_of_2 = lst.count(2)
logger.info(f"Number of times 2 appears in lst: {count_of_2}")

#sort
ascending_lst = lst.sort()
logger.info(f"lst sorted into ascending order: {lst}")

#sort with reverse=True to get them in descending order
descending_lst = lst.sort(reverse=True)
logger.info(f"lst sorted into descending order: {lst}")

#copy to a new list
new_lst = lst.copy()
logger.info(f"new_lst is (copy of lst): {new_lst}")

#pop first item
first = new_lst.pop(0)
logger.info(f"Popped the first (index=0): {first} and now, new_lst is: {new_lst}")

#pop last item
last = new_lst.pop(-1)
logger.info(f"Popped the last (index=-1): {last} and now, new_lst is: {new_lst}")


#LIST TRANSFORMATIONS - Using filter() and map()......................
logger.info("LIST TRANSFORMATIONS - Using filter() and map()...........................................................................")

scores_less_than_four = list(filter(lambda x: x < 4, new_lst))
logger.info(f"Scores less than 4: {scores_less_than_four}")

cbrt_scores = list(map(lambda x: math.cbrt(x), new_lst))
logger.info(f"cubed root of scores: {cbrt_scores}")

#Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. 
# Hint: Volume = side * side * side

volume_of_cube = list(map(lambda x: x * x * x, new_lst))
logger.info(f"the volume of a cube for each value is: {volume_of_cube}")


#LIST TRANSFORMATIONS - Using List Comprehension..........................
logger.info("LIST TRANSFORMATIONS - Using List Comprehension.......................................................................")

#Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 10 or some other cutoff. 

numbers_under_10 = [x for x in list1 if x < 10]
logger.info(f"Numbers under 10 (using list comprehensions!): {numbers_under_10}")

#Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 

tripled_numbers = [x * 3 for x in list1]
logger.info(f"Tripled numbers (using list comprehensions!): {tripled_numbers}")

#Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.

numbers_divided_by_two = [x / 2 for x in list1]
logger.info(f"Numbers divided in half (using list comprehensions): {numbers_divided_by_two}")



def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

show_log()