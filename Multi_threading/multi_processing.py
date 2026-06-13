# multi processing we use when there are mathematically heavy tasks where processes are running parallel and tasks which are heavy CPU usage 
# In this we can use multiple cores in our CPU so this is multi processing

import multiprocessing
import time

def square_number():
    for i in range(10):
        print(i * i)
        time.sleep(2)

def cube_number():
    for i in range(10):
        print(i * i * i)
        time.sleep(2)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    p1.start()
    p2.start()

    
    p1.join()
    p2.join()