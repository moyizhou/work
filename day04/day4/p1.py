if __name__ == '__main__':
    def checkSex():
        name = input("请输入姓名")
        sex = input("请输入性别")
        mdict = {"男": True, "女": False}
        if (mdict[sex]):
            print(name, "先生你好", sep="")
        else:
            print(name, "女生你好", sep="")


    import random


    def checkList():
        mlist = [random.randint(0, 100) for i in range(11)]
        mlist1 = [random.randint(0, 100) for i in range(16)]

        print("原列表1={mlistkey}".format(mlistkey=mlist))
        print("原列表2={mlistkey}".format(mlistkey=mlist1))

        mset = set(mlist)
        mset1 = set(mlist1)

        mlist = list(mset | mset1)
        print("新列表={mlistkey}".format(mlistkey=mlist))


    def checkInformation():
        email = input("请注册一个邮箱")
        mlist = email.partition("@")
        if (len(mlist[0]) > 6):
            print("注册成功")


    def checkStr():
        mstr = input("请输入一个字符串")

        mstr1 = mstr[-1:-len(mstr) - 1:-1]

        print(mstr1)

        if (mstr == mstr1):
            print("是回文数")
        else:
            print("不是回文数")




