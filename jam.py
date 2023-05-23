import time

def currentTime():
    now = time.localtime()
    return now.tm_hour, now.tm_min, now.tm_sec

def main():
    while True:
        hour, minute, second = currentTime()
        print(f"{hour}:{minute}:{second}")
        time.sleep(1)

if __name__ == "__main__":
    main()
