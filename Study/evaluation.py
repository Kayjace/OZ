from itertools import permutations

def calculate(expression):
    """Evaluate the expression with standard left-to-right precedence."""
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in '+-*':
            tokens.append(expression[i])
        else:
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            tokens.append(num)
            continue
        i += 1

    # Perform multiplication first
    result_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            result_tokens[-1] *= tokens[i + 1]
        else:
            result_tokens.append(tokens[i])
        i += 1

    # Then perform addition and subtraction
    result = result_tokens[0]
    i = 1
    while i < len(result_tokens):
        if result_tokens[i] == '+':
            result += result_tokens[i + 1]
        elif result_tokens[i] == '-':
            result -= result_tokens[i + 1]
        i += 2
    
    return result


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
    
    # dp[i][j]는 i부터 j까지의 부분식의 최대값과 최소값을 저장합니다.
    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
    
    # 단일 숫자로 초기화합니다.
    for i in range(n):
        dp[i][i] = (nums[i], nums[i])
    
    # dp 테이블을 채웁니다.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            max_val, min_val = float('-inf'), float('inf')
            for k in range(i, j):
                op = ops[k]
                left_max, left_min = dp[i][k]
                right_max, right_min = dp[k+1][j]
                
                if op == '+':
                    max_val = max(max_val, left_max + right_max)
                    min_val = min(min_val, left_min + right_min)
                elif op == '-':
                    max_val = max(max_val, left_max - right_min)
                    min_val = min(min_val, left_min - right_max)
                elif op == '*':
                    values = [left_max * right_max, left_max * right_min,
                              left_min * right_max, left_min * right_min]
                    max_val = max(max_val, max(values))
                    min_val = min(min_val, min(values))
            
            dp[i][j] = (max_val, min_val)
    
    return dp[0][n-1][0]  # 최대값을 반환합니다.

# 입력 읽기
try:
    expression = input("Enter the expression: ").strip()
    print("Expression:", expression)
    result = max_expression_value(expression)
    print("Maximum value of the expression:", result)
except Exception as e:
    print("An error occurred:", e)