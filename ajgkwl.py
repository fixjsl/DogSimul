import random as r

#강아지 키우기 만들꺼임
day = 1 # 날짜
period = "아침" # 아침 점심 저녁
try_chance = 3 # 행동 가능 횟수
Dog_name = "" #강아지 이름
Dog_mood = "" # 강아지 상태
Dog_feel = 60 # 강아지 기분
Dog_bored = 0 # 강아지 지루함
F_rand = 0 #기분 난수
B_rand = 0# 지루함 난수

while True:
    print("--------- 강아지 키우기 ---------")
    print("|(모든 입력은 숫자로만 해주세요)|")
    print("|         1. 게임 시작          |")
    print("|         2. 게임 종료          |")
    print("---------------------------------")
    x = int(input("행동을 입력 : "))
    if x !=1 and x != 2: # 잘못된 입력 방지
        print("올바른 숫자를 입력해주세요")
        print();  print();   print();
        print("--------- 강아지 키우기 ---------")
        print("|(모든 입력은 숫자로만 해주세요)|")
        print("|         1. 게임 시작          |")
        print("|         2. 게임 종료          |")
        print("---------------------------------")
        continue
    #메인 루프
    if x ==1 :
        #시작시 변수 초기화
        day = 1 # 날짜
        period = "아침" # 아침 점심 저녁
        try_chance = 3 # 행동 가능 횟수
        Dog_feel = 60 # 강아지 기분
        Dog_bored = 0 # 강아지 지루함
        Dog_name = input("강아지의 이름을 입력해주세요 : ")
        while True:
            print(f"--- 날짜 : {day:>2}일차 -- 시간 : {period} --- 행동 가능 횟수 : {try_chance} 회 ---")
            #기분에 따른 표정변화
            if Dog_feel >=70 and Dog_bored <30 :
                Dog_mood = "신남  "
                print("|    ／＼＿／＼        ミ〃ミ〃ミ                            |")
                print("|     ミ ＾   ＾ ミ    ミ〃    〃ミ                          |")
                print("|     ミ   ▽   ミミミミ〃    ミ                              |")
                print("|      ミミミミミミミミミミ〃ミ                              |")
                print("|       ミミミミミミミミミミミ                               |")
                print("|       ⊂ノ ⊂ノ     (＿ノ (＿ノ                              |")

            elif  30<= Dog_feel <70:
                if Dog_bored <30:
                    Dog_mood = "보통  "
                    print("|    ／＼＿／＼        ミ〃ミ〃ミ                            |")
                    print("|     ミ ●   ● ミ    ミ〃    〃ミ                            |")
                    print("|     ミ   ●   ミミミミ〃    ミ                              |")
                    print("|      ミミミミミミミミミミ〃ミ                              |")
                    print("|       ミミミミミミミミミミミ                               |")
                    print("|       ⊂ノ ⊂ノ     (＿ノ (＿ノ                              |")

                elif 30<=Dog_bored <70:
                    Dog_mood = "심심함"
                    print("|    ／＼＿／＼        ・・・                                |")
                    print("|     ミ ー   ー ミ  ミ〃ミ〃ミ〃ミ                          |")
                    print("|     ミ   －   ミミミミミミ〃ミ                             |")
                    print("|      ミミミミミミミミミミ                                  |")
                    print("|       ミミミミミミミミミミミ                               |")
                    print("|       ⊂ノ ⊂ノ     (＿ノ (＿ノ                              |")

                else:
                    Dog_mood = "화남  "
                    print("|    ／＼＿／＼        ミ〃ミ〃ミ                            |")
                    print("|     ミ ＞   ＜ ミ    ミ〃    〃ミ                          |")
                    print("|     ミ   Ｏ   ミミミミ〃    ミ                             |")
                    print("|      ミミミミミミミミミミ〃ミ                              |")
                    print("|       ミミミミミミミミミミミ                               |")
                    print("|       ⊂ノ ⊂ノ     (＿ノ (＿ノ                              |")
            else:
                Dog_mood = "슬픔  "
                print("|    ／＼＿／＼                                              |")
                print("|     ミ ；   ； ミ    ミ〃ミ〃ミ〃                          |")
                print("|     ミ   ︵   ミミミミ〃ミ                                 |")
                print("|      ミミミミミミミミミミ〃〃ミ                            |")
                print("|       ミミミミミミミミミミミミ                             |")
                print("|       ⊂ノ ⊂ノ     (＿ノ (＿ノ                              |")
            print("--------------------------------------------------------------")
            #상태와 행동 종류 안내 문구
            print(f"| 강아지 이름 : {Dog_name}")
            print(f"| 기분 : {Dog_feel:>3}   지루함 : {Dog_bored:>3}   상태 : {Dog_mood}                  |")
            print("| 1. 밥주기   2. 산책가기   3. 간식주기                      |")
            print("| 4. 놀아주기   5. 가만히 있기   6. 게임종료                 |")
            print("--------------------------------------------------------------")
            print()
            action = int(input("할 행동을 선택해 주세요 : "))
            if action == 6: # 게임 종료 안내문구
                while True:
                    print("지금까지의 진행도는 전부 사라지고 타이틀로 돌아갑니다")
                    print(" 1. 타이틀로    2. 게임 계속하기")
                    action = int(input("행동 입력 : "))
                    if action != 1 and action != 2: # 비정상 입력 가드
                        print("다시 입력해주세요")
                    else:
                        break
                if action == 1: # 타이틀로
                    print()
                    break;
                elif action == 2: # 다시 게임으로
                    print()
                    continue;    
            
            if  1>action or action >5: #비정상 입력 가드
                print("행동을 정확히 입력해주세요")
                continue
            #행동 부분
            if action ==1:
                F_rand = r.randint(5,15)
                Dog_feel += F_rand
                print(f"강아지에게 밥을 주었다\n강아지의 기분이 {F_rand}만큼 증가했다!")
            elif action ==2:
                B_rand = r.randint(10,30)
                F_rand = r.randint(10,20)
                Dog_bored -= B_rand; Dog_feel += F_rand
                print(f"강아지와 산책을 다녀왔다\n강아지의 기분이 {F_rand}만큼 증가했다!\n강아지의 지루함이 {B_rand}만큼 감소했다!")
            elif action ==3:
                F_rand = r.randint(20,30)
                Dog_feel += F_rand
                print(f"강아지에게 간식을 주었다 \n강아지의 기분이 {F_rand}만큼 증가했다!")
            elif action ==4:
                F_rand = r.randint(5,20)
                B_rand = r.randint(20,30)
                Dog_feel += F_rand
                Dog_bored -= B_rand
                print(f"강아지와 함께 놀았다\n강아지의 기분이 {F_rand}만큼 증가했다!\n강아지의 지루함이 {B_rand}만큼 감소했다!")
            elif action ==5:
                F_rand = r.randint(10,40)
                B_rand = r.randint(20,50)
                Dog_feel -= F_rand
                Dog_bored += B_rand
                print(f"강아지를 방치했다\n강아지의 기분이 {F_rand}만큼 감소했다...\n강아지의 지루함이 {B_rand}만큼 증가했다...")

            if Dog_bored >= 100 and Dog_feel <=0: #게임오버 분기
                print("강아지가 쓸쓸해서 죽어버렸습니다")
                print("Game over")
                break
            try_chance -= 1
            if try_chance ==2:
                period = "점심"
            elif try_chance == 1:
                period = "저녁"
            elif try_chance == 0:
                day +=1
                try_chance = 3
                period ="아침"
                F_rand = r.randint(-20,20)
                B_rand = r.randint(-20,20)
                Dog_feel += F_rand
                Dog_bored += B_rand
            if Dog_feel <0:
                    Dog_feel = 0
            elif Dog_feel >100:
                    Dog_feel = 100
            if Dog_bored <0:
                Dog_bored  = 0
            elif Dog_bored >100:
                Dog_bored = 100
            print()
    elif x == 2: # 게임 종료
        break;
print("."); print("."); print(".");
print("게임 종료")