#키보드로 성적을 입력
#성적의 구간에 따라 학점 출력
#90~100 : A
#80~89 : B
#70~79 : C
#60~69 : D
#60미만 : F


score = int(input("성적을 입력하세요 : "))

def main():
    if score >= 90:
        print('A')
    
    elif score >= 80:
        print('B')
    
    elif score >= 70:
        print('C')

    elif score >= 60:
        print('D')

    else:
        print("F")

main()