import time

c=[]
def stend(f,n, *args):  
  for i in range(n):
    cyc(*args)    
    delta=t2-t1 
    c.append(delta)
    aver=sum(c)/len(c)
    
  print(f'Среднее время выполнения программы для N: {n}  {aver} ') 
t1 = time.perf_counter() 
def cyc(*args):
  f = open('1.txt', 'a')
  for i in range(*args):
    for j in range(*args):
      f.write('1')
  f.close()

t2 = time.perf_counter()
stend(cyc(4),30,100)
