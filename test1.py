# Program written by Oleg N. Osychenko, Ph.D 
# e-mail: osychenko@gmail.com
# for the project MEDEAS
# Coding style definitions:
# (1) Follow PEP8 in style conventions, for example:
#       Class    | Camel case        | class StringManipulator():
#       Variable | Words joined by _ | joined_by_underscore = True
#       Function | Words joined by _ | def multi_word_name(words):
#       Constant | All uppercase     | SECRET_KEY = 42
# (2) No multiple statements on a single line, that is:
#      if this_is_bad_code: rewrite_code(); make_it_more_readable();
# (3) to be continued. 
#
################################################################ 
# The algorithmic base is the WoLim model based on "windows"
# that we call here "modules". Each "module" is a separate realm
# encompassing data and interactions logically bound. 
# Each module is an object inheriting from GenericModule class. 
# A module object has a set of internal variables (for its own use only)
# and exposed variables that it provides for the other objects.
################################################################
import sys
import numpy as np
import scipy as sc
import pylab as pl
import csv
import openpyxl as opx


class GenericModule:
    """Generic template class to inherit"""
    def __init__(self, arg="temp"):
        self.arg = arg

    def __str__(self):
        return "Description of GenericModule class with arg={}".format(self.arg)




class DataLoader:
    """Class for reading initial data.
    Currently we work directly with Excel files, later on this should 
    be deprecated in favor of CSVs. The corrections must be made in this class."""
    def __init__(self, filename='Data.xlsx'):
        self.wb = opx.load_workbook(filename=filename)

    def __str__(self):
        return "Description of DataLoader class"

    def load(self):
        self.loadgdp()
         
    def loadgdp(self):
        self.initialGDP = self.wb['Other parameters']['H118'].value

def main():
    import sys 
    x = GenericModule()
    dl = DataLoader()
    dl.load()
    
    print(x)
    print(dl.initialGDP)
    if not x:
        sys.exit(1)
    return 0

if __name__ == "__main__":
    sys.exit(main())

