import time
c=[]
def stend(f,n):  
  for i in range(n):
    cyc()
    
    delta=t2-t1 
    c.append(delta)
    aver=sum(c)/len(c)  

  print(f'Среднее время выполнения программы для N: {n}  {aver} ') 
t1 = time.perf_counter()
def cyc():
  k = 100
  f = open('1.txt', 'a')
  for i in range(k):
    for j in range(k):
      f.write('1\n')
  f.close()
t2 = time.perf_counter()

stend(cyc,30)
