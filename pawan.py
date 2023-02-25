import pandas as pd

marks_data = pd.DataFrame({'ID': {0: 23, 1: 43, 2:44, 3:22},
                          'Name': {0: 'Ram', 1: 'Deep',
                                   2: 'Yash', 3: 'Aman'},
                          'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                                    4: 56},
                          'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C'}})
file_name = 'details.xlsx'

marks_data.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
