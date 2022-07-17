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
import logging
import logg

class StringsOperations:
    def __init__(self, s):
        logging.info('StringOperation Class imported')
        self.string = s

    def extract_jump(self, n1, n2, n3):
        try:
            logging.info("success in extract_jump - %s", self.string[n1:n2:n3])
            return self.string[n1:n2:n3]
        except Exception as e:
            logging.exception(e)

    def reverse(self):
        """ Reversing the string"""
        try:
            logging.info("reversing the string")
            return self.string[-1::-1]
        except Exception as e:
            logging.exception(e)

    def split_up(self, ch=' '):
        """Split the string after converting to uppercase"""
        try:
            logging.info("Converting the string to upper case and then splitting")
            return self.string.upper().split(sep=ch)
        except Exception as e:
            logging.exception(e)

    def lower(self):
        """convert the string to lower case"""
        try:
            logging.info("Converting the string to lower case")
            return self.string.lower()
        except Exception as e:
            logging.exception(e)

    def caps(self):
        """Capitalize the whole string"""
        try:
            logging.info("Capitalizing the string")
            return self.string.capitalize()
        except Exception as e:
            logging.exception(e)

    def stripp(self, x):
        try:
            logging.info("trying stripp")
            if x == 'l':
                logging.info("x == 'l' found")
                return self.string.lstrip()
            elif x == 'r':
                logging.info("x == 'r' found")
                return self.string.rsrtip()
            elif x == 's':
                logging.info("x == 's' found")
                return self.string.strip()
            else:
                logging.info("incorrect input!")
        except Exception as e:
            logging.exception(e)

    def replace(self, old, new):
        """replacing old with new character"""
        try:
            logging.info(f"Replacing the character {old} with {new}")
            return self.string.replace(old, new)
        except Exception as e:
            logging.exception(e)

    def slice(self, start, end, step):
        """Slicing the string with specified start and end indices"""
        try:
            logging.info(f"Slicing the string from {start} to {end} with step size{step}")
            return self.string[start:end:step]
        except Exception as e:
            logging.exception(e)
