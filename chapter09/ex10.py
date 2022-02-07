score = [88, 95, 70, 100, 99, 88, 78, 50]

perfect = score.index(100)
print("만점 받은 학생은 %d번 입니다."%perfect)

pernum = score.count(100)
print("만점자 수는 %d명 입니다."%pernum)

print("학생수는 %d명 입니다." %len(score))
print("최고 점수는 %d점 입니다" %max(score))
print("최소 점수는 %d점 입니다." %min(score))