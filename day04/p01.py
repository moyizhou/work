import random
if __name__ == '__main__':
    mynum = [5,9,3,4]
    #打乱包的顺序
    random.shuffle(mynum)
    print(mynum)
    #进行排序
    mynum.sort(reverse=False)
    print(mynum)
    #倒着打印字符
    mynum.reverse()
    print(mynum)
    #求他的长度
    len = len(mynum)
    print(len)
    
