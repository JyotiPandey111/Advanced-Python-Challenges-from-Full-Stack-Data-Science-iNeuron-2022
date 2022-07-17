"""

 1.
 ineuron
 ineuron ineuron
 ineuron ineuron ineuron
 ineuron ineuron ineuron ineuron

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
import logging
import logg

class PatternCreator:
    def __init__(self, s):
        self.s = s

    def p1(self, n):
        try:
            logging.info("accessing p1 function")
            for i in range(n):
                for j in range(0, i + 1):
                    print(str(self.s), end=" ")
                print()
        except Exception as e:
            logging.exception(e)

    def p2(self, n):
        try:
            logging.info("accessing p2 function")
            for i in range(0, n):
                for j in range(n - i):
                    print('', end=' ' * len(self.s))

                for j in range(i):
                    print(self.s, end=' ' * len(self.s))
                print()

            for i in range(n - 2, 0, -1):  # row
                for j in range(n - i):
                    print('', end=' ' * len(self.s))
                for j in range(i):  # column
                    print(self.s, end=' ' * len(self.s))
                print()
        except Exception as e:
            logging.exception(e)
