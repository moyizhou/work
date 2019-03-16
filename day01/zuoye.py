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


#菱形
m = [1,2,3,4,5,6,7,8]

for i in m:
    for h in m:
        if i < h:
            print(" ",end=" ")
    for k in m[0:i-1]:
        print("*",end=" ")

    for j in m:
        print("*",end=" ")
        if j == i:
            print()
            break

for i in m:
    for k in m:
        print(" ",end=" ")
        if i == k:
            break
    for h in m:
        if i < h:
            print("*",end=" ")
        if i <h-1:
            print("*",end=" ")
    print()

mo = [1,2,3,4,5,6,7,8,9]

for i in mo:
    for j in mo:
        if i<j:
            print(" ",end=" ")

    for h in mo[0:i-1]:
        print("+",end=" ")

    for m in mo:
        print("*",end=" ")
        if m==i:
            print()
            break

for i in mo:
    for j in mo:
        print(" ",end=" ")
        if i == j:
            break
    for h in mo:
        if i<h:
            print("*",end=" ")
        if i<h-1:
            print("*",end=" ")
    print()

one = [1,2,3,4,5,6]

for i in one:
    for j in one:
        if i < j:
            print(" ",end=" ")
    for h in one[0:i-1]:
        print("*",end=" ")
    for m in one:
        print("*",end=" ")
        if m==i:
            print()
            break

for i in one:
    for j in one:
        print(" ",end=" ")
        if i == j:
            break
    for h in one:
        if i<h:
            print("*",end=" ")
        if i<h-1:
            print("*",end=" ")
    print()

two = [1,2,3,4,5]

for i in two:
    for j in two:
        if i<j:
            print(" ", end=" ")
    for h in two[0:i-1]:
        print("*",end=" ")
    for m in two:
        print("*",end=" ")
        if m == i:
            print()
            break

for i in two:
    for j in two:
        print()

