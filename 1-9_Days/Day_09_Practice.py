student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades = {}

for key in student_scores:
    student_grades = student_scores[key]
    ''' One thing I notice, it can still be improve by lessening the words
    # example 
    if student_grades >91:
        do something
    elif student_grades > 81:
        do something
       ''' 
    if student_grades >= 91 and student_grades < 100: # no need to lengthing this
        print("Outstanding")
    elif student_grades >= 81 and student_grades < 91:
        print("Exceeds Expectation")
    elif student_grades >= 71 and student_grades < 81:
        print("Acceptable")
    else: 
        print("Fail")

