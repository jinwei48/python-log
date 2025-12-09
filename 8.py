'''
处理大日志文件,统计IP
def log_ip_generator(log_file):
    with open(log_file,'r',encoding='utf-8') as f:
        for line in f:
            if 'IP:' in line:
                ip=line.split('IP')[1].split()[0]
                yield ip
from collections import defaultdict
ip_count=defaultdict(int)
for ip in log_ip_generator('access.log'):
    ip_count[ip]+=1
'''
def square_generator(n):
    current=0
    while current<=n:
        yield current**2
        current+=1
gen=square_generator(5)
for num in gen:
    print(num)


gen_expr=(x**2 for x in range(6))
for num in gen_expr:
    print(num)
sum_gen=sum(x**2 for x in range(6))
print(sum_gen)