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
        " day ", "day", " up",]

    #把两个集合进行空格去除
    o = [i.strip() for i in klist]
    #进行去重
    vlist = set(o)
    mlist = {}

    for i in vlist:
        mlist[i] = i
    print(mlist)







