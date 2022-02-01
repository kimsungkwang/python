def calcscore(name, *score, **option):
    print(name)
    print(score)
    print(option)

    total = 0
    for s in score:
        total += s

    print("총점 : ", total)
        #if(option['avg'] == True):
    if option.get('avg'): #'avg' 키가 없으면 디볼트(none)가 false로 처리됨
        print("평균 : ", total/len(score))

def main():
        #calcscore("홍길동", 88, 99, 77, avg=True)
        #calcscore("고길동", 99, 88, 95, 85)

        hong_score = [88, 99, 77]
        go_score = [99, 88, 95, 85]
        option = {
            'avg' : True,
            'total' : True
        }
        calcscore("홍길동", *hong_score, avg=True)
        calcscore("고길동", 
                *go_score,      #리스트를 펼쳐서 가변인수로 전달 
                **option        #사전을 펼쳐서 키워드 가면인수로 전달    
                )

main()
        