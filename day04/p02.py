import random
if __name__ == '__main__':
    mlist = [1,2,3,4,5,6,7,8,9,0]
    #通过id来证明该列表和新列表是否相同
    olist = [o for o in mlist if o % 2 == 0]
    print("olist =",olist)
    plist = [1,2,3,4]
    ilist = [100,200,300,400]
    jlist = [m + n for m in plist for n in ilist]
    print("no if ->",jlist)
    jlist = [m + n for m in plist if m%2 == 0 for n in ilist]
    print("with if ->",jlist)
    olist = [m for m in mlist if m % 2 == 0]
    print("olist=",olist)
    jlist = [m+n for m in plist for n in ilist]
    print("jlist == ",jlist)
    jlist = [m+n for m in plist if m%2 == 0 for n in ilist]
    print("plist == ",jlist)
    mlist = [['a','b'],['e','f'],['g','h']]
    nlist = [[m,n] for m,n in mlist]
    print(mlist)
    nlist = [[m,n] for m,n in mlist]
    print(mlist)
    nlist = [[m,n] for m,n in mlist]
    print(mlist)
    #随机生成整数 1-100  10个随机数
    mlist = [ random.randint(0,100) for i in range(0,10)]
    print(mlist)
    mlist = [ random.randint(0,100) for i in range(0,30)]
    print(mlist)
    mlist = [ random.randint(0,200) for i in range(0,20)]
    print(mlist)







