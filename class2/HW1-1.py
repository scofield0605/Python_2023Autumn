
numder=int(input('number'))


if numder > 1:
    #作出迴圈
    for i in range(2, int(numder / 2) + 1):
        #如果i的任何一個數字能整除number那他就不是質數
        if (numder % i) == 0:
            print("flase")
            break
    #如果不可以那他就是質數    
    else:
        print("true")

# big o 次數 O(n)


