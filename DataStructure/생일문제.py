import random

TRIALS = 1000000
same_birthdays = 0

for _ in range(TRIALS):
    birthdays = []
    
    # 백만명 중 23명만 있어도 생일이 같은 경우가 50%를 넘는다.
    for i in range(23):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays/TRIALS*100} %')
# 50.6441 %