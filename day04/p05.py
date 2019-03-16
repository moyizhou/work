import random

if __name__ == '__main__':
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 通过id来证明该列表和新列表是否相同
    olist = [o for o in mlist if o % 2 == 0]
    print("olist =", olist)
    plist = [1, 2, 3, 4]
    ilist = [100, 200, 300, 400]
    jlist = [m + n for m in plist for n in ilist]
    print("no if ->", jlist)
    jlist = [m + n for m in plist if m % 2 == 0 for n in ilist]
    print("with if ->", jlist)
    olist = [m for m in mlist if m % 2 == 0]
    print("olist=", olist)
    jlist = [m + n for m in plist for n in ilist]
    print("jlist == ", jlist)
    jlist = [m + n for m in plist if m % 2 == 0 for n in ilist]
    print("plist == ", jlist)
    mlist = [['a', 'b'], ['e', 'f'], ['g', 'h']]
    nlist = [[m, n] for m, n in mlist]
    print(mlist)
    nlist = [[m, n] for m, n in mlist]
    print(mlist)
    nlist = [[m, n] for m, n in mlist]
    print(mlist)
    # 随机生成整数 1-100  10个随机数
    mlist = [random.randint(0, 100) for i in range(0, 10)]
    print(mlist)
    mlist = [random.randint(0, 100) for i in range(0, 30)]
    print(mlist)
    mlist = [random.randint(0, 200) for i in range(0, 20)]
    print(mlist)
0
if __name__ == '__main__':
    # 创建一个非空列表使用中括号
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    nlist = mlist[-2:-4:-1]
    print("id -> mlist", id(mlist))
    print("id -< nlist", id(nlist))
    plist = [1, 2, 3, 4]
    olist = plist
    print("plist id is {plistid}".format(plistid=id(plist)))
    print("olist id is {olistid}".format(olistid=id(olist)))
    ulist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(id(ulist))
    del ulist[4]
    print(ulist)
    print(id(ulist))
    t = 2
    print("in ->", t in mlist)
    print("not in ->", t not in mlist)
    nist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nlist = [i for i in range(1, 10)]
    print("nlist =", nlist)
    nlist = [i for i in range(2, 5)]
    print(nlist)
    nlist = [i for i in range(3, 8)]
    print(nlist)
    # _index_()获取当前值在list中的下标
    nlist = [[7, 8, 9, ], [4, 5, 6], [1, 2, 3]]
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {0}".format(j, j.__index__()))
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {1}".format(j, j.__index__()))
    for sublist in nlist:
        for j in sublist:
            print("nlist[{1}] = {2}".format(j, j.__index__()))
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    olist = [o for o in mlist]
    print("olist = ", olist)
    print("olist id - >", id(olist))
    print("mlist id - >", id(mlist))
    klist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    olist = [o for o in klist if o % 2 == 0]
    print("olist=", olist)

if __name__ == '__main__':
    print("输入两个数字，计算除法")
    print("树入Q退出")
    while True:
        print("\t")
        fnum = input("first number")
        if fnum == "q":
            break

        snum = input("second number:")
        if snum == "q":
            break
try:
    f = open("good.text", "r")

    f.close()
except Exception as e:
    print(e)
else:
    print("excetion else")
finally:
    print("finally")


# 定义一个函数 如果参数是0 则手动抛出异常
def mfun(v):
    if v == 0:
        raise Exception("good")


try:
    mfun(0)
except Exception as e:
    print("excetp->{0}".format(e))
    pass
print("good")


class myException(ValueError):
    pass


try:
    print("brfor raise exception")
    raise myException
    print("after raise exception")
except MyException as me:
    print("catch myException")
except ValueError as ve:
    print("catch ValueError")
except Exception as e:
    print("exception")
    print(e)


class MyExcept(Exception):
    pass

    def show(self):
        print("hehe")


import random

if __name__ == '__main__':
    mynum = [5, 9, 3, 4]
    # 打乱包的顺序
    random.shuffle(mynum)
    print(mynum)
    # 进行排序
    mynum.sort(reverse=False)
    print(mynum)
    # 倒着打印字符
    mynum.reverse()
    print(mynum)
    # 求他的长度
    len = len(mynum)
    print(len)

if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up", ]
    # 创建新的集合mar  把klist进行去重
    mar = [v.strip() for v in klist]
    print("mar = 去空格的klist")
    print(mar)
    # 把mar进行去重
    olist = set(mar)
    print("olist = 去重后的mar")
    print(olist)
    # 编写Python程序判断字符串是否重复。（50分）
    # 通过 mar 和 olist 的长度来判断是否重复
    if (len(mar) != len(olist)):
        print("重复")
    else:
        print("不重复")
    # 创建一个新的字典
    plist = {}
    # 遍历去重后的olist
    for v in olist:
        # 通过olist键给plist进行赋值
        plist[v] = mar.count(v)
    # 输出统计结果
    print("结果为")
    print(plist)

if __name__ == '__main__':
    print("99乘法表+")
    me = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 循环
    for i in me:
        for j in me:
            print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
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

if __name__ == '__main__':

    mo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in mo:
        for j in mo:
            if j * i < 10:
                print(str(i) + "*" + str(j) + "=" + str(i * j).rjust(2, " "), end=" ")
            else:
                print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
                if i == j:
                    print()
                    break
if __name__ == '__main__':
    mo = [1, 2]
    print(mo.append("4"))
    print(type(mo))
    mi = list()
    print(mi.insert(0, "5"))
    print(type(mi))

if __name__ == '__main__':
    while True:
        hehe = input("你叫啥")
        if hehe == 'q':
            break
        else:
            print(hehe)
    print("gun")

    while True:
        haha = input("狗龙")
        if haha == 'yes':
            break
        else:
            print(haha)
    print("对就是")

    while True:
        enen = input("小莫")
        if enen == "no":
            break
        else:
            print(enen)
    print("666")
if __name__ == '__main__':
    mstr = "ximoxiaomo,ainiyouxi"

    print(mstr[4:4:2])

    mastr = "Gud Lak"
    # 将字符串转换成大写
    upperStr = mastr.upper()
    print(upperStr)
    # 将字符串转换成小写
    upperStr = mastr.lower()
    print(upperStr)
    # 将字符串转第一个字母换成大写（每个单词）
    upperStr = mastr.title()
    print(upperStr)
    # 获取字符串的类型
    print(type(upperStr))

name = "moyizhou"
age = 19
addr = "shanxi"
# 不添加  默认输出 默认用空格输出
print(name, age, addr)
print("**************")
# 输出不换行 end
print(name, age, addr, end="")
print("*************")
# 去除空格
print(name, age, addr, sep="")

if __name__ == '__main__':
    while True:
        a = input("输入第一个数")
        b = input("输入运算符")
        c = input("输入第二个数")
        d = input("结果是")
        if b == "+":
            break
        else:
            print(a, b, c)
    print(d)

if __name__ == '__main__':
    print("99乘法表+")
    me = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 循环
    for i in me:
        for j in me:
            print(str(i) + "*" + str(j) + "=" + str(i * j), end=" ")
            if i == j:
                print()
                break

# 菱形
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

mo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in mo:
    for j in mo:
        if i < j:
            print(" ", end=" ")

    for h in mo[0:i - 1]:
        print("+", end=" ")

    for m in mo:
        print("*", end=" ")
        if m == i:
            print()
            break

for i in mo:
    for j in mo:
        print(" ", end=" ")
        if i == j:
            break
    for h in mo:
        if i < h:
            print("*", end=" ")
        if i < h - 1:
            print("*", end=" ")
    print()

one = [1, 2, 3, 4, 5, 6]

for i in one:
    for j in one:
        if i < j:
            print(" ", end=" ")
    for h in one[0:i - 1]:
        print("*", end=" ")
    for m in one:
        print("*", end=" ")
        if m == i:
            print()
            break

for i in one:
    for j in one:
        print(" ", end=" ")
        if i == j:
            break
    for h in one:
        if i < h:
            print("*", end=" ")
        if i < h - 1:
            print("*", end=" ")
    print()

two = [1, 2, 3, 4, 5]

for i in two:
    for j in two:
        if i < j:
            print(" ", end=" ")
    for h in two[0:i - 1]:
        print("*", end=" ")
    for m in two:
        print("*", end=" ")
        if m == i:
            print()
            break

for i in two:
    for j in two:
        print()
