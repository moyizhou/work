import random
import day03.p05
if __name__ == '__main__':

    mlist = list()
    print(type(mlist))
    mlist = []
    print(type(mlist))
    mlist.append("东方龙")
    print(mlist)
    mlist.insert(0,"狗龙")
    print(mlist)
    val = mlist.pop()
    print("mlist.pop = {popvalkey}".format(popvalkey = val))
    print(mlist)

    mynum = [3,7,4,2]
    random.shuffle(mynum)
    print(mynum)

    mynum.sort(reverse=True)
    print(mynum)

    nnum = sorted(mynum,reverse=True)
    print(nnum)

    #倒着打印列表
    nnum.reverse()
    print(nnum)
    #遍历该非空列表
    for i in nnum:
        print(i)
    #改变列表中的数元祖不能改变
    nnum[0] = 10
    for i in nnum:
        print(i)
    print(nnum)

print(day03.p05.lx())
print(day03.p05.oo())






     






        
