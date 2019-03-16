if __name__ == '__main__':
#创建一个非空列表使用中括号
    mlist = [1,2,3,4,5,6,7,8,9,0]
    nlist = mlist[-2:-4:-1]
    print("id -> mlist",id(mlist))
    print("id -< nlist",id(nlist))
    plist =[1,2,3,4]
    olist = plist
    print("plist id is {plistid}".format(plistid=id(plist)))
    print("olist id is {olistid}".format(olistid=id(olist)))
    ulist = [1,2,3,4,5,6,7,8,9,0]
    print(id(ulist))
    del ulist[4]
    print(ulist)
    print(id(ulist))
    t = 2
    print("in ->",t in mlist)
    print("not in ->",t not in mlist)
    nist = [1,2,3,4,5,6,7,8,9]
    nlist = [i for i in range(1,10)]
    print("nlist =" , nlist)
    nlist = [i for i in range(2,5)]
    print(nlist)
    nlist = [i for i in range(3,8)]
    print(nlist)
#_index_()获取当前值在list中的下标
    nlist = [[7,8,9,],[4,5,6],[1,2,3]]
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {0}".format(j,j.__index__()))
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {1}".format(j,j.__index__()))
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {2}".format(j,j.__index__()))
    mlist = [1,2,3,4,5,6,7,8,9,0]
    olist = [o for o in mlist]
    print("olist = ",olist)
    print("olist id - >",id(olist))
    print("mlist id - >",id(mlist))
    klist = [1,2,3,4,5,6,7,8,9]
    olist=[o for o in klist if o%2 ==0]
    print("olist=",olist)

