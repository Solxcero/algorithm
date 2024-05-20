#  Error
# - Syntax Error [Compiler error] : 프로그램 실행 전에 발생하는 오류 (구문오류)
# - Runtime Error [Exception] : 프로그램 실행 중 발생하는 오류(예외)

# def func():
#     print('you are in func()')
#     try :
#         print("you are in TRY")
#         return
#     except:
#         print("you are in EXCEPT")
#     finally:
#         print("you are in FINALLY")
#     print("func() is end")

# func()

# 사용자로부터 파일 이름을 입력 받고, 그 파일 내용을 int() 로 정수로 변환 뒤 출력
def func(file):
    try :
        with open(file,"r") as f:
            content = f.read()
            try:
                nums = int(content)
            except ValueError :
                print("Can not convert to integer.")
            # finally:
                # with open 안쓸경우 file.close() 
    except FileNotFoundError:
        print("File does not exist.")
    return content

file = input("File Name : ")
print(func(file))


#--- Exception as e 는 마지막에 써야 함!
# try :
#     #사용자로부터 어떤 입력을 받고, 네트워크로 전송하는 프로그램
# except ValueError as e:
#     print("값 다시 입력")
# except ConnectionError as e :
#     print("인터넷 연결 오류")
# except Exception as e:
#     i = input("오류 내용 전송? [Y/N]")
#     if i in ["Y","y"]:
#         메일보내기(type(e),str(e))