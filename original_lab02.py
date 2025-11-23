def grade_calc():
    total_students = int(input('Total number of students: '))

    scores = input(f'Enter {total_students} score(s): ').split()

    while len(scores) < total_students:
        scores = input(f'Enter {total_students} score(s): ').split()

    scores = [int(num) for num in scores]
    scores = scores[0:total_students]

    best = max(scores)

    for student, score in enumerate(scores, start=1):
        if score >= (best - 10):
            grade = 'A'
        elif score >= (best - 20):
            grade = 'B'
        elif score >= (best - 30):
            grade = 'C'
        elif score >= (best - 40):
            grade = 'D'
        else:
            grade = 'F'

        print(f'Student {student} score is {score} and grade is {grade}')

    return None

def main():
    grade_calc()

main()