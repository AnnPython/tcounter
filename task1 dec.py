def stend(n):

    def decorator(func):
      import time
      def wrapper(*args, **kwargs):
        
        for i in range(n):
          t1 = time.perf_counter()
          return_value = func(*args, **kwargs)
          t2 = time.perf_counter()
          delta = t2 - t1
        print(f'Время выполнения программы для N = {n}: {delta} ')
        return return_value
      return wrapper
    return decorator



@stend(n=40)

def cyc():
  k = 100
  f = open('1.txt', 'a')
  for i in range(k):
    for j in range(k):
      f.write('1')
  f.close()

cyc()
