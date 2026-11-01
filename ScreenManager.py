from GlobalEnum import Face_Enum


class ScreenManager:
    dog_face = {  # noqa: RUF012
        Face_Enum.HAPPY: ["＾   ＾", "▽"],
        Face_Enum.NORMAL: ["●   ●", "●"],
        Face_Enum.BORED: ["ー   ー", "ー"],
        Face_Enum.ANGRY: ["＞   ＜", "Ｏ"],
        Face_Enum.SAD: ["；   ；", "︵"],
    }

    @staticmethod
    def print_title():
        print("--------- 강아지 키우기 ---------")
        print("|(모든 입력은 숫자로만 해주세요)|")
        print("|         1. 게임 시작          |")
        print("|         2. 게임 계속하기      |")
        print("|         3. 게임 종료          |")
        print("---------------------------------")

    @classmethod
    def main_screen(cls, curdata, dog):
        print(
            f"--- 날짜 : {curdata.day:>2}일차 -- 시간 : {curdata.period} --- 행동 가능 횟수 : {curdata.try_chance} 회 ---"
        )
        # 기분에 따른 표정변화
        cls.print_dog_face(dog.state)
        print("--------------------------------------------------------------")
        # 상태와 행동 종류 안내 문구
        print(f"| 강아지 이름 : {dog.name} |")
        print(
            f"| 기분 : {dog.feel:>3}   지루함 : {dog.bored:>3}   상태 : {dog.state}                  |"
        )
        print("| 1. 밥주기   2. 산책가기   3. 간식주기                      |")
        print("| 4. 놀아주기   5. 가만히 있기   6. 게임종료                 |")
        print("--------------------------------------------------------------")
        print()

    @classmethod
    def print_dog_face(cls, Dog_mood):
        print("|    ／＼＿／＼        ミ〃ミ〃ミ                            |")
        print(
            f"|     ミ {cls.dog_face[Dog_mood][0]} ミ    ミ〃    〃ミ                          |"
        )
        print(
            f"|     ミ   {cls.dog_face[Dog_mood][1]}   ミミミミ〃    ミ                              |"
        )
        print("|      ミミミミミミミミミミ〃ミ                              |")
        print("|       ミミミミミミミミミミミ                               |")
        print("|       ⊂ノ ⊂ノ     (＿ノ (＿ノ                              |")

    @staticmethod
    def print_savefile(date, dog):
        print()
        print("--------- 저장된 게임 ---------")
        print(
            f"| 날짜 : {date.day} | 시간 : {date.period} | 행동 가능 횟수 : {date.try_chance} |"
        )
        print(
            f"| 강아지 이름 : {dog.name} | 기분 : {dog.feel} | 지루함 : {dog.bored} | 상태 : {dog.state} |"
        )
        print("-------------------------------")
