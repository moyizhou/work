if __name__ == '__main__':
    mstr = "ximoxiaomo,ainiyouxi"


    print(mstr[4:4:2])

    mastr = "Gud Lak"
    #将字符串转换成大写
    upperStr = mastr.upper()
    print(upperStr)
    # 将字符串转换成小写
    upperStr = mastr.lower()
    print(upperStr)
    # 将字符串转第一个字母换成大写（每个单词）
    upperStr = mastr.title()
    print(upperStr)
    #获取字符串的类型
    print(type(upperStr))

name = "moyizhou"
age = 19
addr =  "shanxi"
#不添加  默认输出 默认用空格输出
print(name,age,addr)
print("**************")
#输出不换行 end
print(name,age,addr,end="")
print("*************")
#去除空格
print(name,age,addr,sep="")
