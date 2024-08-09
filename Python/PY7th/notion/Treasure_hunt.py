import random
import math

# 게임 초기화
def initialize_game(n):
    """ 게임 보드 및 위치 초기화 """
    treasure_position = (random.randint(1, n), random.randint(1, n ))
    player_position = (random.randint(1, n), random.randint(1, n))
    
    # 플레이어와 보물이 같은 위치에 있을 수 없음
    while player_position == treasure_position:
        player_position = (random.randint(1, n), random.randint(1, n))
    
    return treasure_position, player_position

# 거리 계산
def calculate_distance(treasure_position, player_position):
    """ 두 위치 간의 유클리드 거리 계산 """
    return math.sqrt((treasure_position[0] - player_position[0]) ** 2 + (treasure_position[1] - player_position[1]) ** 2)

# 플레이어 이동
def move_player(board_size, player_position, direction):
    """ 방향에 따라 플레이어 이동 """
    x, y = player_position
    if direction == 'N':
        if y < board_size:
            y += 1
            return (x, y), True
        else:
            return player_position, False
    elif direction == 'S':
        if y > 1:
            y -= 1
            return (x, y), True
        else:
            return player_position, False
    elif direction == 'E':
        if x < board_size:
            x += 1
            return (x, y), True
        else:
            return player_position, False
    elif direction == 'W':
        if x > 1:
            x -= 1
            return (x, y), True
        else:
            return player_position, False
    return player_position, False

# 게임 실행
def play_game(board_size):
    """ 게임의 주요 로직 """
    treasure_position, player_position = initialize_game(board_size)
    move_count = 0

    print(f"게임이 시작되었습니다! 보드 크기는 {board_size}x{board_size}입니다.")
    print(f"보물은 (1,1) ~ ({board_size},{board_size})중 한 곳에 숨겨져 있습니다. 보물을 찾아주세요.")
    print(f"동쪽으로 이동 시, 앞자리가 1 증가합니다.")
    print(f"서쪽으로 이동 시, 앞자리가 1 감소합니다.")
    print(f"북쪽으로 이동 시, 뒷자리가 1 증가합니다.")
    print(f"남쪽으로 이동 시, 뒷자리가 1 감소가합니다.")
    print(f"-" * 50)
    
    while True:
        print(f"현재 위치: {player_position}")
        print(f"이동 횟수: {move_count}")
        
        direction = input("이동 (N/S/E/W): ").strip().upper()
        
        if direction not in {'N', 'S', 'E', 'W'}:
            print("잘못된 입력! N, S, E, W 중 하나를 입력하세요.")
            continue
        
        # 플레이어 이동
        new_position, can_move = move_player(board_size, player_position, direction)
        if can_move:
            player_position = new_position
            move_count += 1
        else:
            print("이동할 수 없습니다. 보드의 경계에 도달했습니다.")
            continue
        
        if player_position == treasure_position:
            print(f"축하합니다! {move_count}번의 이동 끝에 보물을 찾았습니다.")
            break
        
        distance = calculate_distance(treasure_position, player_position)
        print(f"힌트! 보물까지의 거리: {distance:.2f}")

# 메인 함수 정의 및 호출
def main():
    board_size = 5  # 보드 크기를 5x5로 설정
    play_game(board_size)

if __name__ == "__main__":
    main()