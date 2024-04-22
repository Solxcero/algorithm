# 1. 스트림 연결
# w : 쓰기모드, a :  추가해서 쓰기 모드 , r :  읽기 모드
path = './Basic/test.txt'
my_file = open(path, "r")

# 2. 스트림을 통해 데이터 통신
my_str = my_file.read()
print(my_str)

# 3. 스트림 해제
my_file.close()


# 연결 해제 같이 
with open(path, "r") as f:
    my_str = f.read()
    print(my_str)
    
with open("./Basic/a.txt", "w") as f :
    f.write("Hi There\n")
    
with open("./Basic/a.txt", "a") as f :
    f.write("Hi Again")
    