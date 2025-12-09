print("----欢迎来到BIM频道----")
name=input("请输入姓名：")
height=eval(input('请输入身高(m):'))
weight=eval(input('请输入体重(kg):'))
sex=input('请输入性别(F/M):')
BIM=float(float(weight)/(float)(height)**2)
if BIM<=18.4:
    print(f'我要让全世界知道 {name} 是一个细狗,hahahhaha')
elif BIM<=23.9:
    print(f'不错嘛{name}')
else:
    print(f'{name}你是肥宅吗')


