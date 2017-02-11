#!/usr/bin/env python3

class XlReader:

    def __init__(self):
        """
        We want these to be private since they are mutable.
        """
        self.__headerColumns = []
        self.__rows = []

        """
        Let's keep a running count of the lines, it might come in handy.
        """
        self.line_counter = 0


    def read(self, path, hasHeaderColumns=True):

        """
        The test file I got was encoded in latin-1.
        """
        with open(path, encoding='latin-1') as file:

            """
            Since the file is a CSV (comma seperated values) we
            can read the file line by line and split each line by ','
            to get each column.
            """

            for line in file:

                row = tuple(line.split(','))

                if self.line_counter is 0 and hasHeaderColumns:
                    self.__headerColumns.append(row)
                else:
                    self.__rows.append(row)

                self.line_counter += 1

    @property
    def header(self):
        return tuple(self.__headerColumns)

    @property
    def rows(self):
        return tuple(self.__rows)
