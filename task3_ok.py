def stend(n):
    def decorator(func):
      import time
      def wrapper(*args, **kwargs):
        
        for i in range(n):
          t1 = time.perf_counter()
          return_value = func(*args, **kwargs)
          t2 = time.perf_counter()
          izm = {}
          delta = t2 - t1
          izm[n] = delta
        
        print(f'Время выполнения программы {delta} ')
        f = open('test.csv', 'a')
        for i in sorted(izm):
            c = str(izm[i]).replace('.',',')
            f.write(f'{i}; {c} \n')
        f.close()
        return return_value
      return wrapper
    return decorator



@stend(n=2)

def cyc(k):
  f = open('1.txt', 'a')
  for i in range(k):
    for j in range(k):
      f.write('1')
  f.close()

for i in range(2, 60, 3):
 print(f'Выполняем {i} раз')
 cyc(i)
