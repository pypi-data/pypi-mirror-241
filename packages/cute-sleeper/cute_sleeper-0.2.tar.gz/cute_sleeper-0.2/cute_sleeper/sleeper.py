import time
import random

def random_sleep(max_seconds):
    mean = max_seconds / 2
    std_dev = max_seconds / 4
    sleep_time = random.normalvariate(mean, std_dev)

    sleep_time = max(0, min(sleep_time, max_seconds))
    print(sleep_time)
    time.sleep(sleep_time)
    return f"Slept for {sleep_time:.2f} seconds."

if __name__ == '__main__':
    random_sleep(1)
