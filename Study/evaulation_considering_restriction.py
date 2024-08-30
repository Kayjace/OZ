def max_expression_value(expression):
    # 숫자와 연산자를 분리합니다.
    nums = []
    ops = []
    num = ''
    for char in expression:
        if char in '+-*':
            if num:
                nums.append(int(num))
                num = ''
            ops.append(char)
        else:
            num += char
    if num:
        nums.append(int(num))

    n = len(nums)
    
    # dp[i]는 i번째 연산자까지 계산했을 때의 최대값을 저장합니다.
    dp = [0] * n
    dp[0] = nums[0]
    
    for i in range(1, n):
        # 괄호를 추가하지 않는 경우
        dp[i] = calculate(dp[i-1], nums[i], ops[i-1])
        
        # 괄호를 추가하는 경우 (현재 연산자와 이전 숫자를 묶음)
        if i > 1:
            with_parenthesis = calculate(dp[i-2], calculate(nums[i-1], nums[i], ops[i-1]), ops[i-2])
            dp[i] = max(dp[i], with_parenthesis)
    
    return dp[n-1]

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# 입력 읽기
try:
    expression = input("Enter the expression: ").strip()
    print("Expression:", expression)
    result = max_expression_value(expression)
    print("Maximum value of the expression:", result)
except Exception as e:
    print("An error occurred:", e)