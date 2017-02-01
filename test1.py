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
        return "description of the class with arg={}".format(self.arg)


class DataLoader:
    """docstring for DataLoader"""
    def __init__(self):
        wb = opx.load_workbook(filename = 'Data.xlsx')
        print(wb['BAU']['B6'].value)

if __name__ == "__main__":
    x = GenericModule()
    dl = DataLoader()
    print(x)