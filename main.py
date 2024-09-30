from queue import Queue
import random

queue = Queue()

def generate_request():
    request = random.randint(0, 10000)
    queue.put(request)

def process_request():
    while not queue.empty():
        request = queue.get()
        print(f'Request {request} is processing...') 
    else:
        print('The queue is empty')

if __name__ == '__main__':
    for i in range(10):
        generate_request()
    process_request()
