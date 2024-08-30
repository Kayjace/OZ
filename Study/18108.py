def calculate_year(y):
    x = 2541 - 1998
    if 1000 <= y <= 3000:
        return y - x
    else:
        print("out of range")

user_input = input("연도를 입력하세요: ")

try:
    year = int(user_input)
    result = calculate_year(year)
    print(result)

except ValueError:
    print("유효한 숫자를 입력하세요.")