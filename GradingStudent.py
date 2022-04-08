import math
import os
import random
import re
import sys
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            next_num = (grades[i] - (grades[i] % 5))+5
            dif = next_num - grades[i]

            if dif < 3:
                grades[i] = next_num

    return grades

def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
main()
