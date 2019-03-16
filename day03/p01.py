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
    #创建新的集合mar  把klist进行去重
    mar = [v.strip() for v in klist]
    print("mar = 去空格的klist")
    print(mar)
    #把mar进行去重
    olist = set(mar)
    print("olist = 去重后的mar")
    print(olist)
    # 编写Python程序判断字符串是否重复。（50分）
    # 通过 mar 和 olist 的长度来判断是否重复
    if(len(mar) != len(olist)):
        print("重复")
    else:
        print("不重复")
    #创建一个新的字典
    plist = {}
    #遍历去重后的olist
    for v in olist:
    #通过olist键给plist进行赋值
        plist[v]=mar.count(v)
    #输出统计结果
    print("结果为")
    print(plist)

