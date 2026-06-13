from concurrent.futures import ThreadPoolExecutor
import time

# A mock function that simulates a time-consuming task
def process_data(item):
    print(f"Task {item} is starting...")
    time.sleep(2)  # Simulate some I/O operation like downloading or file reading
    print(f"Task {item} is finished!")
    return f"Result of {item}"

# Using ThreadPoolExecutor
if __name__ == "__main__":
    items_to_process = [1, 2, 3, 4, 5, 6]
    start_time = time.time()

    # Create a pool of 3 worker threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        print("--- Using map ---")
        # .map() applies the function to every item in the list automatically
        # It assigns the tasks to the available worker threads
        results = executor.map(process_data, items_to_process)
        
        # Iterating over the results
        for result in results:
            print(result)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")

        

### What is ThreadPoolExecutor?
# Manually creating and managing individual threads (using `threading.Thread(...)` over and over) can become difficult and inefficient when you have dozens or hundreds of tasks. 

# **ThreadPoolExecutor** (from Python's `concurrent.futures` module) solves this by managing a "pool" of worker threads. You simply throw tasks at the pool, and the executor automatically assigns them to available threads.

# **Benefits:**
# - **Reusability:** Threads in the pool are reused for new tasks, saving the overhead of constantly creating and destroying threads.
# - **Resource Control:** By setting `max_workers`, you strictly limit the maximum number of threads running at once, preventing your system from getting overwhelmed.
# - **Simpler Code:** It provides highly convenient methods like `.map()` and `.submit()` to easily handle tasks and their return values.

# ### The Example Explained

# In the code we added:
# 1. **`max_workers=3`**: We are telling the executor to keep a maximum of 3 threads alive in the pool.
# 2. **`executor.map(...)`**: This is just like Python's built-in `map()` function but runs concurrently. We gave it a list of 6 items. 
# 3. **Execution flow**: The executor immediately grabs the first 3 items and starts working on them using the 3 threads. As soon as any thread finishes its task, it will automatically pick up the 4th item, and so on, until all 6 are done.

# Because it automatically handles the joining and resource cleanup behind the scenes (thanks to the `with` context manager), it is the recommended, modern way to do multithreading in Python!