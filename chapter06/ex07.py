# 올바른 데이터 (0 <= score <= 100)로
# 합계와 평균을 구하시오.

scores = [92, 86, 68, -1, 56, -30, 90, 140, 90]

total = 0
count = 0

for score in scores:
    if (score < 0 ) or (score > 100):
        continue

    total += score 
    count += 1

print("평균", round(total/count,2))
print("합계", int(total + count))
