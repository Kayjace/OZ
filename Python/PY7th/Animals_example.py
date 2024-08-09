#실행 프로그램
from animals.mammals import Dog
from animals.mammals import Cat
from animals.birds import Eagle

def main():
    # Dog 객체 생성 및 정보 출력
    dog = Dog(name="Neiro", breed="ShibaInu")
    print(dog)          # 출력: Dog(name=Neiro, breed=ShibaInu)
    print(dog.sound())   # 출력: Neiro says: Woof!

    # Cat 객체 생성 및 정보 출력
    cat = Cat(name="Nyaa", breed="Persian")
    print(cat)          # 출력: Cat(name=Nyaa, breed=Persian)
    print(cat.sound())   # 출력: Buddy says: Meow!

    # Eagle 객체 생성 및 정보 출력
    eagle = Eagle(name="Bald Eagle", wingspan=2.3)
    print(eagle)        # 출력: Eagle(name=Bald Eagle, wingspan=2.3 meters)
    print(eagle.soar()) # 출력: Bald Eagle is soaring high!

if __name__ == "__main__":
    main()