if __name__ == '__main__':
    # 2.创建一个列表，存储公司10个名单，对这些名单进行排序，要求按姓名的字符多少来排。（30分
    mlist = ["李墉","王春旺","王越","史偏颇盘","网存亡","as","asdasdasd","来来来","as"]
    # for i in range(4):
    #     mlist.append(input("请输入名字："))
    print(mlist)
    nlist = [len(i) for i in mlist]
    print(nlist)
    glist = []
    a = 0
    i=0
    while i < len(nlist) :
        print("--"+mlist[i])
        if nlist[i] >= a :
            a = nlist[i]
            glist.insert(0,mlist[i])
        else :
            k=0
            b = len(glist)
            while k < b :
                print(k)
                if nlist[i] >=len(glist[k]) :

                    glist.insert(k,mlist[i])
                    break
                k+=1
        i+=1

    print(glist)
    myList = ['青海省', '内蒙古自治区', '西藏自治区', '新疆维吾尔自治区', '广西壮族自治区', '1', \
              '3']
    myList1 = sorted(myList, key=lambda i: len(i))
    print(myList1)
