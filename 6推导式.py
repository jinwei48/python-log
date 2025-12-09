names=['bob','alice','tom','ji']
new_names=[name.upper()for name in names if len(name)>3]
print(new_names)
listdemo=['Google','Runnoob']
newdic={key:len(key) for key in listdemo}
print(newdic)
number=[i for i in range(30) if i%3==0]
print(number)