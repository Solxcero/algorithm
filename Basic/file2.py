
path = './Basic/test.txt'

while True:
    try : 
        with open(path,'r') as f:
            dt = f.read()
            if dt != '':
                print(dt.strip().split("\n"))
    except:
        pass

    string = input("> INPUT : ")
    with open(path,'a') as f:
        f.write(string.strip() + "\n")

         