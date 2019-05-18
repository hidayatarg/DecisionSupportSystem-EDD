# Data related to a job list for a CNC machine.
# Processing times and due dates of each jobs is given.
# Design a simple decision support system

# Task 1 : It sorts the jobs by “Earliest Due Date” (EDD) principle

import pandas as pd

# import the file
xls = pd.ExcelFile("MachineScheduling.xlsx")
# open sheet at first index
df = xls.parse(0)
# before sort
print("before sort")
print(df)

print("\n")
print("Sort By EDD Sequence")
# sort by earliest due date
sortedByEarliestDueDate = df.sort_values(by='Due Date')
# update the row indexes
sortedByEarliestDueDate = sortedByEarliestDueDate.reset_index(drop=True)
df = sortedByEarliestDueDate

print(df)

# setting a value
# df.at[0, 'Processing Time'] = 20

processTimeCol = sortedByEarliestDueDate['Processing Time']
# print(processTimeCol[0])

startCol = df['Start']
finishCol = df['Finish']
for x in range(0, len(startCol)):
    if x == 0:
        df.at[x, 'Start'] = 0
        df.at[x, 'Finish'] = df.at[x, 'Processing Time']
        df.at[x, 'Tardiness'] = df.at[x, 'Finish'] - df.at[x, 'Due Date']
    else:
        df.at[x, 'Start'] = df.at[x - 1, 'Finish']
        df.at[x, 'Finish'] = df.at[x, 'Start'] + df.at[x, 'Processing Time']
        df.at[x, 'Tardiness'] = df.at[x, 'Finish'] - df.at[x, 'Due Date']

print(df)

# writer = pd.ExcelWriter('output.xlsx')
# df.to_excel(writer, sheet_name='Sheet1', columns=["JobCode"], index=False)
# writer.save()


# Task 2:	computes start and finish times of each job if they are processed in the sequence determined by EDD rule


# Task 3:   It computes amount of earliness or tardiness of each job
# Task 4:   It creates the Gant chart of the jobs


# First Second work
# for x in range(0, len(column)):
#      print(x+1 + ". " + column[x])


# import pandas as pd
#
# xl = pd.ExcelFile("MachineScheduling.xlsx")
# df = xl.parse(0)
# df = df.sort(columns="Job Code")
#
# writer = pd.ExcelWriter('output.xlsx')
# df.to_excel(writer, sheet_name='Sheet1', columns=["JobCode"], index=False)
# writer.save()
