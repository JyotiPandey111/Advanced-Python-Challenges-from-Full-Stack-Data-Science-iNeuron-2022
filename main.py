# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from StringsOperations import StringsOperations
from ListsOperations import ListOperations
from PatternCreator import PatternCreator
import logging

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    """

     s = "this is My First Python programming class and i am learNING python string and its function"
     1 . Try to extract data from index one to index 300 with a jump of 3-------------extract_jump()
     2. Try to reverse a string without using reverse function------------------------reverse()
     3. Try to split a string after conversion of entire string in uppercase----------split_up()
     4. try to convert the whole string into lower case-------------------------------lower()
     5 . Try to capitalize the whole string-------------------------------------------caps()
     6 . Give an example of strip , lstrip and rstrip---------------------------------stripp(self, x)   
     7. Replace a string character by another charactor by taking your own example----replace(self, old, new)
     8. Slicing the string with specified start and end indices ----------------------slice()

    """
    logging.info("\n\n")
    logging.info("Logging from Strings Operations Class")
    logging.info("\n\n")
    logging.info("creating a new string")
    name = StringsOperations("this is My First Python programming class and i am learNING python string and its function")
    logging.info("String operations")

    logging.info("String operations Question number 1 ")
    print("\n\nExtract data from index one to index 300 with a jump of 3")
    print(name.extract_jump(1,300,3))

    logging.info("String operations Question number 2 ")
    print("\n\nreversing the name")
    print(name.reverse())

    logging.info("String operations Question number 3 ")
    print("\n\nComponents in name ")
    print(name.split_up())

    logging.info("String operations Question number 4 ")
    print("\n\nconvert to lower case")
    print(name.lower())

    logging.info("String operations Question number 5 ")
    print("\n\nCapitalizing the name")
    print(name.caps())

    logging.info("String operations Question number 6 ")
    print("\n\nGive an example of strip , lstrip and rstrip")
    print(name.stripp('s'))

    logging.info("String operations Question number 7 ")
    print("\n\nslicing the name")
    print(name.slice(2, 5, 1))

    logging.info("String operations Question number 8 ")
    new_name = name.replace('S', 'P')
    print(new_name)

    """

        List Operations
         l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
         234:[23,45,656]}]
         1 . Try to reverse a list------------------------------------------------reverse_list()
         2.  Try to Extract numerics out of this list-----------------------------extract_numeric()
         3 . Try to access 456 in list--------------------------------------------access_num()
         4 . Try to extract only a list collection form list l--------------------extract_list()
         5 . Try to extract string------------------------------------------------extract_string()
         6 . Try to list all the key in dict element available in list------------extract_keys()
         7 . Try to extract all the value element form dict available in list-----extract_values()
         8 . Try to extract dictionary--------------------------------------------extract_dict()
         9 . Extract odd numbers from list----------------------------------------extract_list_odd()
         10. Extract tuples from the list-----------------------------------------extract_tuple()
         11. Try to calculate sum of numeric in list------------------------------sum_numeric()

        """


    l = ListOperations([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}])
    logging.info("\n\n")
    logging.info("Logging from Lists Operations Class")
    logging.info("\n\n")
    logging.info(f"created a list l {l}")
    logging.info("Lists Operations")

    logging.info("Lists operations Question number 1 ")
    print("\nReverse list")
    print(l.reverse_list())

    logging.info("Lists operations Question number 2 ")
    print("\nExtract Numeric")
    print(l.extract_numeric())

    logging.info("Lists operations Question number 3 ")
    print("\nAccess 456 in list")
    print(l.access_num())

    logging.info("Lists operations Question number 4 ")
    print("\nExtract List")
    print(l.extract_list())

    logging.info("Lists operations Question number 5 ")
    print("\nExtract string")
    print(l.extract_string("sudh"))

    logging.info("Lists operations Question number 6 ")
    print("\nExtract keys from dict")
    print(l.extract_keys())

    logging.info("Lists operations Question number 7 ")
    print("\nExtract values from dict")
    print(l.extract_values())

    logging.info("Lists operations Question number 8 ")
    print("\nExtract Dict")
    print(l.extract_dict())

    logging.info("Lists operations Question number 9 ")
    print("\nExtract odd numbers from list")
    print(l.extract_list_odd())

    logging.info("Lists operations Question number 10 ")
    print("\nExtract tuples")
    print(l.extract_tuple())

    logging.info("Lists operations Question number 11 ")
    print("\nSum of Numeric")
    print(l.sum_numeric())

    """

     1.
     iNeuron
     iNeuron iNeuron
     iNeuron iNeuron iNeuron
     iNeuron iNeuron iNeuron iNeuron

     2.
     .....*.....*ineuron.....*.....*
     .....*ineuron.....*ineuron.....*
     ineuron.....*ineuron.....*ineuron
     .....*ineuron.....*ineuron.....*
     .....*.....*ineuron.....*.....*

     3. Try to print this by using while loop
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
    * * * * * * *
    * * * * * * * *
    * * * * * * * * *

    """


    logging.info("\n\n")
    logging.info("Logging from Pattern Creator Class")
    logging.info("\n\n")

    logging.info("Pattern Creator Question number 1 ")
    s = PatternCreator("iNeuron")
    print(s.p1(4))

    logging.info("Pattern Creator Question number 2 ")
    s = PatternCreator("iNeuron")
    print(s.p2(4))

    logging.info("Pattern Creator Question number 3 ")
    s = PatternCreator("*")
    print(s.p1(9))




