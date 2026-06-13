# Formal Definition of Multithreading
# Multithreading is a CPU feature and programming model that allows a single process to spawn multiple independent execution threads that share the same memory space and resources, enabling them to run concurrently and execute different parts of the program simultaneously.

# In Simpler Terms
# It is the ability of a program to divide itself into multiple smaller tasks (threads) that can run at the same time independently, all while sharing the same memory.

# Process: An executing instance of a program.
# Thread: The smallest sequence of programmed instructions that can be managed independently by a scheduler. A thread is essentially a "lightweight process" that exists within a process.


import threading
import time


def print_number():
    for i in range(10):
        print(i)
        time.sleep(2)


def print_letter():
    for i in "ABCDEFGHIJ":
        print(i)
        time.sleep(2)

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)


t1.start()
t2.start()

t1.join()
t2.join()

print("Finished!")