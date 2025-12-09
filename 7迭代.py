'''
list=[1,2,3,4]
it=iter(list)
for i in it:
    print(i,end=" ")

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=10:
          x=self.a
          self.a += 1
          return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
'''
def countdown(n):
    while n>0:
        yield n
        n-=1
generator=countdown(5)
for value in generator:
    print(value)

import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if (count>n):
           return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit() 

    