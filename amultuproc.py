import multiprocessing
import time

def compute_square(n, q):
    time.sleep(2) 
    q.put(n * n)

def main():
    numbers = [1, 2, 3, 4, 5]
    q = multiprocessing.Queue()

    processes = []
    for number in numbers:
        process = multiprocessing.Process(target=compute_square, args=(number, q))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not q.empty():
        print(q.get())

if __name__ == "__main__":
    main()
