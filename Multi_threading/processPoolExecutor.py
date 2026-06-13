# multi processing with pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(num):
    print("We are just starting taking squares")
    time.sleep(2)
    result = num * num
    print(f"We have finished taking square of {num}")
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
        for result in results:
            print(result)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")

# multi processing with pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(num):
    print("We are just starting taking squares")
    time.sleep(2)
    result = num * num
    print(f"We have finished taking square of {num}")
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
        for result in results:
            print(result)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
        