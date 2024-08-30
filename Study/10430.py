def function(A, B, C):
    try:
        if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
            result1 = (A+B)%C
            result2 = ((A%C) + (B%C))%C
            result3 = (A*B)%C
            result4 = ((A%C) * (B%C))%C
            print(result1)
            print(result2)
            print(result3)
            print(result4)
        else:
            print("범위를 초과했습니다.")
    except ValueError:
        print("정수를입력해주세요")

print("A, B, C 값을 공백을 두고 순서대로 입력해 주세요.")
a, b, c = map(int, input().split())

function(a,b,c)