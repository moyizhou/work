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
    #创建kk集合 把klist的空格去除
    kk = [k.strip() for k in klist]
    #进行去重
    oo = set(kk)
    #用他们的长度进行判断
    if (len(list) != len(oo)):
        print()

