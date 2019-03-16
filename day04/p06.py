if __name__ == '__main__':
    #进行切片
    mlist = [1,2,3,4]
    nlist = mlist[0:2]
    print(nlist)
    for ni in nlist:
        print("nlist[{0}] = {1}".format(ni.__index__(),ni))
    for ni in nlist:
        print("nlist[{0}] = {1}".format(ni.__index__(),ni))
    mlist = [1,2,3]
    nlist =mlist[:]
    nlist[0] = 3
    print("nlist = {0}".format(nlist))
    print("mlist = {0}".format(mlist))
    olist = nlist[:]
    print("olist = {0}".format(olist))
    #求最大值最小值 长度
    mlist = [1,2,8,6]
    print("len ==",len(mlist))
    print("max ==",max(mlist))
    print("min ==",min(mlist))
    mlist = [1,2,5,4]
    print(len(mlist))
    print(max(mlist))
    print(min(mlist))
    mlist = [1,2,5,4]
    print(len(mlist))
    print(max(mlist))
    print(min(mlist))
    #统计列表中指定数据的个数
    mlist = [1,2,3]
    nlist = ["hoho","hehe","hehe","hoho"]
    num = nlist.count("hehe")
    print("num=",num)
    mlist = ["hoho","hoho","hoho"]
    num = nlist.count("hoho")
    print(num)
    #列表的合并
    mlist = [1,2,3,4,5,6]
    nlist = [33,44,55]
    nlist.extend(mlist)
    print("list,extend=",nlist)
    mlist = [1, 2, 3, 4, 5, 6]
    nlist = [66, 44, 55]
    nlist.extend(mlist)
    print("list,extend=", nlist)
    mlist = [1, 2, 3, 4, 5, 6]
    nlist = [33, 88, 55]
    nlist.extend(mlist)
    print("list,extend=", nlist)
    #在列表末尾添数字
    mlist=[1,2,3,4]
    mlist.append(33)
    print(mlist)
    #在指定位置添加数字
    mlist.insert(0,44)
    print(mlist)
    v = mlist.pop(0)
    print(v)
    print(mlist)
    mlist.remove(1)
    print(mlist)
    mlist.insert(0, 44)
    print(mlist)
    v = mlist.pop(0)
    print(v)
    print(mlist)
    mlist.remove(1)
    print(mlist)
    mlist.insert(0, 44)
    print(mlist)
    v = mlist.pop(0)
    print(v)
    print(mlist)
    mlist.remove(1)
    print(mlist)
#判断这个值是否在列表中
    mlist = [1,2,3,4]
    if 4 in mlist:
        mlist.remove(4)
    try:
        mlist.remove(5)
    except Exception as e:
        print("5 is not exist")
        print(e)
    finally:
        print("finally")
        mlist = [1, 2, 3, 4]
        if 4 in mlist:
            mlist.remove(4)
        try:
            mlist.remove(5)
        except Exception as e:
            print("5 is not exist")
            print(e)
        finally:
            print("finally")
        mlist = [1, 2, 3, 4]
        if 4 in mlist:
            mlist.remove(4)
        try:
            mlist.remove(5)
        except Exception as e:
            print("5 is not exist")
            print(e)
        finally:
            print("finally")


















