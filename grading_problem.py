#!/bin/python3

def grading_students(grades):
    res = []
    for grade in grades:
        diff = grade%5
        if grade < 38:
            res.append(grade)
        elif diff > 2:
            res.append(grade + (5-diff))
        else:
            res.append(grade)
    return res

def grading_students2(grades):
    return [i if (i < 38 or i % 5 < 3) else (i + (5 - i % 5)) for i in grades]

if __name__ == "__main__":
    '''
    Every student receives a grade in the inclusive range from 0 to 100.
    Any grade less than 40 is a failing grade.

    If the difference between the grade and the next multiple of 5 is less than 3,
    round grade up to the next multiple of 5.
    If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
    '''

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)
    print(result)