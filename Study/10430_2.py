print("A, B, C 값을 공백을 두고 순서대로 입력해 주세요.")
A, B, C = map(int, input().split())
if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)

else:
    print("값이 범위를 초과합니다")