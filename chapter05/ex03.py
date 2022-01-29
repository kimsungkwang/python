age = int(input("나이를 입력하세요 : "))

def main():

    if age < 19:
        print("애들은 가라")
        print("공부 열심히 해야지~")

    elif age == 19:
        print("1년만 지나고 오세요!")

    else:
        print("어서오세요!")

main()