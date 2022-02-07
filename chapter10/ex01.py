dic = {
    'boy': '소년',
    'school': '학교',
}

print(dic)
print(dic.get('boy'))
print(dic.get('school'))
print(dic.get('girl', '사전에 없는 단어입니다'))