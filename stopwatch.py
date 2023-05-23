import time

def start_stopwatch():
    global start_time
    start_time = time.time()

def stop_stopwatch():
    global end_time
    end_time = time.time()

def get_elapsed_time():
    return end_time - start_time

def main():
    start_time = None
    end_time = None

    print("Press Enter to start the stopwatch.")
    input()

    start_stopwatch()

    print("Press Enter to stop the stopwatch.")
    input()

    stop_stopwatch()

    elapsed_time = get_elapsed_time()

    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()

