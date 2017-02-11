#/usr/bin/env python3

from xlmutate import XlMutator
from xlread import XlReader
#from xlwrite import XlWriter

import xlsxwriter


reader = XlReader()
reader.read('gageTesting.csv')

workbook = xlsxwriter.Workbook('gageTesting_after.xlsx')
worksheet = workbook.add_worksheet()

for row in range(len(reader.rows)):
    if len(reader.rows[row]) > 1:

        for column in range(len(reader.rows[row])):
            print(reader.rows[row][column])

            new_data = (reader.rows[row][column]
                .replace('ò', 'o')
                .replace('ê', 'e'))

            print(new_data)
            worksheet.write(row, column, new_data)

workbook.close()


"""
mutator = XlMutator()

mutator.ignoreColumn('INDUSTRY')
mutator.ignoreColumn('LAST')

mutator.addMutation('á', 'a')
mutator.addMutation('blue', '')

#etc

mutator.addColumn('ZIP', )  #still need to think about how i'm going to do the 'formula'

mutator.build()

writer = XlWriter(mutator.header, mutator.rows)
writer.write()
"""
