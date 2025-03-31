# looping dataframes

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# #Loop through dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

# pandas inbuilt rows 
for (index, row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)