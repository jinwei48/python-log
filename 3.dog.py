print("====欢迎来到人与狗比较系统====")
while True:
    try:
        age=int(input("请输入狗的年龄"))
        print(" ")
        age=float(age)
        if age<0:
            print("你在逗我i?")
        elif age==1:
            print("相当于人类14岁")
        elif age==2:
            print("相当于人类22岁")
        else:
            human=22+(age-2)*5
            if human>=200:
                print("你家狗真能活啊")
                print("狗的吉尼斯纪录才29岁5个月")
            else:
                print("相当于人类：",human)
            break;
    except ValueError:
        print("bushi,你是真的狗啊")
input("点击Enter键退出")