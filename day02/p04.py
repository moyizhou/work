if __name__ == '__main__':
    print("99乘法表+")
    me = [1,2,3,4,5,6,7,8,9]
    #循环
    for i in me:
        for j in me:
            print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
            if i == j:
                print()
                break




def lx():
    m = [1, 2, 3, 4, 5, 6, 7, 8]

    for i in m:
        for h in m:
            if i < h:
                print(" ", end=" ")
        for k in m[0:i - 1]:
            print("*", end=" ")

        for j in m:
            print("*", end=" ")
            if j == i:
                print()
                break
    for i in m:
        for k in m:
            print(" ", end=" ")
            if i == k:
                break
        for h in m:
            if i < h:
                print("*", end=" ")
            if i < h - 1:
                print("*", end=" ")
        print()
print(lx())




def oo():
    print("99乘法表+")
    me = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 循环
    for i in me:
        for j in me:
            print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
            if i == j:
                print()
                break
print(oo())