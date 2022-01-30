# 리스트에 성적 데이터가 있음
# 평균을 구하세요 .
# 최저 성적을 구하세요

scores = [34, 78, 90, 35, 100, 88] #0~100

total = 0
count = 0

min_score = 101             #현재 알고 있는 최저 성적  뭐가 나오든 min_score 랑 비교해서 작게 나올 수 있도록
max_score = -1 

for score in scores:
    total += score
    count += 1
    if score < min_score:
        min_score = score
    elif score > max_score:
        max_score = score

average = total / count
print("평균 : ", round(average,2))
print("최고 성적 : ", max_score)
print("최저 성적 : ", min_score)
