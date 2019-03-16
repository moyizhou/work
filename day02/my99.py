if __name__ == '__main__':

    mo = [1,2,3,4,5,6,7,8,9]

    for i in mo:
        for j in mo:
            if j*i<10:
                print(str(i) + "*" + str(j) + "=" + str(i * j).rjust(2," "),end=" ")
            else:
                print(str(i) + "*" + str(j) + "=" + str(i * j),end=" ")
                if i == j:
                    print()
                    break