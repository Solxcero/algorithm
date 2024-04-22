
import random

# 이름, 몸무게, 신장 랜덤 생성 
hg = list('가나다라마바사아자차카타파하')

with open('./Basic/test2.txt', 'w',encoding="UTF-8") as f : 
    f.write('name,weight,height\n')
    for i in range(1000):
        
        name = random.choice(hg) + random.choice(hg)
        weight = random.randrange(40,120)
        height = random.randrange(140,200)

        f.write(f'{name},{weight},{height}\n')
# print('{}, {}, {}'.format(name, weight, height))
# print(", ".join([name,str(weight),str(height)]))

with open('./Basic/test2.txt','r',encoding='utf-8') as f :
    for line in f :
        # print(line.strip())
        name, weight, height = line.strip().split(',')
        
        if not weight.isdigit():
            continue
        weight, height = int(weight), int(height)
    
        bmi = round(weight / (height / 100)**2,2)
        res = ''
        if bmi >= 25 :
            res = '과체중'
        elif bmi >= 18.5 :
            res = '정상체중'
        else :
            res = '저체중'
        
        print("\n".join([
            f'이름 : {name}',
            f'몸무게 : {weight}',
            f'키 : {height}',
            f'BMI : {bmi}',
            f'결과 : {res}',''
        ]))
        
        
        
        