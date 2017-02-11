#!usr/bin/env python3

class XlMutator:
    def __init__(self, header, rows):
        pass

    """
    We can store new columns in a dict with a 'formula' to generate value of
    the new column.
    """
    def addColumn(column, formula):
        pass

    """
    We can tell our mutator to ignore columns when building new rows to write.
    """
    def ignoreColumn(column):
        pass

    """
    We can tell our mutator to replace certain things.
    """
    def addMutation(old, new):
        pass

    def build():
        pass
