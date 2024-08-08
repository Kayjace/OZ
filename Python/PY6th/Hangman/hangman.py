# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

# 행맨 그림
hangman_pics= [
'''
''',
'''
  +---+
      |
      |
      |
      |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  |   |
      |
      |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  |   |
  |   |
      |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  |   |
  |   |
  O   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  |   |
  |   |
  O   |
 /    |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  |   |
  |   |
  O   |
 /|   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  |   |
  |   |
  O   |
 /|\  |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  |   |
  |   |
  O   |
 /|\  |
 /    |
      |
      |
=========''', 
'''
  +---+
  |   |
  |   |
  |   |
  O   |
 /|\  |
 / \  |
      |
      |
=========''']

class HangmanGame:
    def __init__(self):
        self.word = random.choice(words)  # 랜덤으로 단어 선택

        self.guesses = set()  # 추측된 글자 저장

        self.attempts = 10  # 시도 횟수

    def display(self):
        # 단어의 현재 상태 표시
        result = ""

        # 위에서 설정한 단어의 글자들을 하나씩 가져옵니다.
        for char in self.word:
            # 만약 추측된 글자가 설정한 단어에 포함되어 있다면
            if char in self.guesses:
                # 추측된 글자를 표시합니다.
                result += char
            else:
                # 추측된 글자가 아니라면 _를 표시합니다.
                result += "_"

        # 단어의 현재 상태를 반환합니다.
        return result

    def play(self):
        self.attempts=10
        # 게임을 시작합니다.
        # 시도 횟수가 0이 될 때까지 반복
        print(f"남은 시도 횟수 : {self.attempts}")
        while self.attempts > 0:

            # 현재 단어 상태 표시
            print(self.display())
            # 추측 했던 글자 보여주고 입력받기
            print(f"이미 추측한 글자 : {self.guesses}")
            #올바른 입력인지 체크
            while True:
                guess = input("글자를 추측해보세요: ").lower()
                    # 입력이 한 글자인지, 알파벳인지 확인
                if len(guess) == 1 and guess.isalpha() and guess.isascii():
                    break
                else:
                    print("잘못된 입력입니다. 알파벳 한 글자만 입력해주세요.")

            # 추측한 글자가 이미 추측한 글자라면
            if guess in self.guesses:
                print("이미 추측한 글자입니다.")

            # 새로이 추측한 글자가 설정한 단어를 맞췄다면
            elif guess in self.word:
                # 글자를 추측했던 글자 목록에 추가
                self.guesses.add(guess)
                # 단어를 맞추셨군요. 더 힘내봐요"라고 출력
                print(f"단어를 맞추셨군요. 더 힘내봐요.")
                # 설정한 단어가 추측했던 글자들에 포함된다면(정답을 모두 맞췄다면)
                if set(self.word).issubset(self.guesses):
                    print(f"축하합니다! 단어를 맞추셨습니다: {self.word}")
                    break
            # 추측한 글자가 설정한 단어를 맞추지 못했다면
            else:
                self.attempts -= 1
                print(f"틀렸습니다. 남은 시도 횟수: {self.attempts}")
                # 시도 횟수에 맞는 행맨 그림을 출력합니다.
                if self.attempts >= 0:
                    print(hangman_pics[10 - self.attempts])
            if self.attempts == 0:
                print(f"게임 오버. 정답은: {self.word}")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()