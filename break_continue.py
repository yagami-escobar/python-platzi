def run():
    for i in range(100):
        if(i % 3 == 0):
            continue
        elif(i % 2 == 0):
            print(i)
        elif(i % 79 == 0):
            break
        else:
            print("*")



if __name__ == '__main__':
    run()



def run():
    comand = "npm --version"
    for i in comand:
        print(i)
    
    print()
    j = 0
    while j < len(comand):
        print(comand[j])
        j = j + 1



if __name__ == '__main__':
    run()