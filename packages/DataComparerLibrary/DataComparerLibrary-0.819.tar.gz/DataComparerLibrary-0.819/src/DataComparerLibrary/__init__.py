#!/usr/bin/env python

from DataComparerLibrary.datacomparer import DataComparer
from DataComparerLibrary.datasorter import DataSorter
from DataComparerLibrary.fileconverter import FileConverter


class DataComparerLibrary(DataComparer, DataSorter, FileConverter):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'



