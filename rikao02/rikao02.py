if __name__ == '__main__':
    #编写Python程序判断字符串是否重复。（50分）
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
    mar = [i.strip() for i in klist]
#编写Python程序打印输出字符串中重复的所有字符。（50分）
    olist = set(mar)
    print(olist)
#编写Python程序判断字符串是否重复。（50分）
    if(len(mar) != len(olist)):
        print("you")
    else:
        print("no")
    plist = {}
    for j in olist:
        plist[j]= mar.count(j)
    print(plist)








