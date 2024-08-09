def info_and_calc_total(students):
    for name, scores in students.items():
        total = sum(scores.values())
        subjects = ', '.join(f"{subject}: {score}" for subject, score in scores.items())
        print(f"이름: {name}")
        print(subjects)
        print(f"총점: {total}")
        print()

students = {
    "min": {"국어": 80, "영어": 78, "수학": 92},
    "hun": {"국어": 90, "영어": 88, "수학": 72},
    "jung": {"국어": 69, "영어": 77, "수학": 79}
}

# 총점 계산 및 출력
info_and_calc_total(students)