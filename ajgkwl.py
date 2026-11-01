import random as r

from Date import Date
from Dog import Dog
from SaveLoadManager import FileManager as fm
from ScreenManager import ScreenManager as sm

# 강아지 키우기 만들꺼임


ACTIONS = {
    1: {
        "name": "밥주기",
        "feel": (5, 15),
        "bored": (0, 0),
        "msg": "강아지에게 밥을 주었다\n강아지의 기분이 {feel}만큼 증가했다!",
    },
    2: {
        "name": "산책가기",
        "feel": (10, 30),
        "bored": (-20, -10),
        "msg": "강아지와 산책을 다녀왔다\n강아지의 기분이 {feel}만큼 증가했다!\n강아지의 지루함이 {bored}만큼 감소했다!",
    },
    3: {
        "name": "간식주기",
        "feel": (20, 30),
        "bored": (0, 0),
        "msg": "강아지에게 간식을 주었다\n강아지의 기분이 {feel}만큼 증가했다!",
    },
    4: {
        "name": "놀아주기",
        "feel": (5, 20),
        "bored": (-30, -20),
        "msg": "강아지와 함께 놀았다\n강아지의 기분이 {feel}만큼 증가했다!\n강아지의 지루함이 {bored}만큼 감소했다!",
    },
    5: {
        "name": "가만히 있기",
        "feel": (-40, -10),
        "bored": (20, 50),
        "msg": "강아지를 방치했다\n강아지의 기분이 {feel}만큼 감소했다...\n강아지의 지루함이 {bored}만큼 증가했다...",
    },
}


def actionTo(action, dog):
    act = ACTIONS[action]
    feel = r.randint(*act["feel"])
    bored = r.randint(*act["bored"])
    dog.update_stat(feel, bored)
    print(act["msg"].format(feel=abs(feel), bored=abs(bored)))


def inputGuard(lo, hi):
    try:
        x = int(input("행동을 입력해주세요 : "))
        if lo <= x <= hi:
            return x
    except ValueError:
        pass
    print("행동을 정확히 입력해주세요.")
    print()
    print()
    print()
    return False


def main(date, dog):
    while True:
        dog.Dog_feel_check()
        sm.main_screen(date, dog)
        action = inputGuard(1, 6)
        if action == False:
            continue
        if action == 6:  # 게임 종료 안내문구
            while True:
                print()
                print("현재까지의 내용은 저장됩니다")
                print("게임을 종료하시겠습니까? 1. 타이틀로 2. 게임 계속하기")
                print()
                x = inputGuard(1, 2)
                if x == False:
                    continue
                else:
                    break
            if x == 1:  # 타이틀로
                print()
                return
            elif x == 2:  # 다시 게임으로
                print()
                continue
            # 행동 부분
        actionTo(action, dog)

        if date.update_time():  # 날짜 업데이트
            dog.update_daliy_stat()

        if dog.is_dead():  # 게임오버 분기
            print("강아지가 쓸쓸해서 죽어버렸습니다")
            print("Game over")
            return
        saveload.save(date, dog)
        print()


saveload = fm("savefile.txt")

while True:
    sm.print_title()

    x = inputGuard(1, 3)
    if x == False:
        continue
    # 메인 루프
    if x == 1:
        date = Date()
        # 시작시 변수 초기화
        name = input("강아지의 이름을 입력해주세요 : ")
        dog = Dog(name)
        main(date, dog)
    elif x == 2:  # 게임 계속하기
        result = saveload.load()
        if result is None:
            continue
        dog, date = result
        print()
        print()
        print("현재 저장되어있는 데이터")
        sm.print_savefile(date, dog)

        print("게임을 계속하시겠습니까? 1. 게임 계속하기 2. 타이틀로")
        x = inputGuard(1, 2)
        if x == False:
            continue
        if x == 1:  # 게임 계속하기
            main(date, dog)
        elif x == 2:  # 타이틀로
            print()
            continue
    elif x == 3:  # 게임 종료
        break
print(".")
print(".")
print(".")
print("게임 종료")
