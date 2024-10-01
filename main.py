import queue
import time
import threading
import random

# Клас для заявки
class Request:
    def __init__(self, request_id, description):
        self.request_id = request_id
        self.description = description
    
    def __str__(self):
        return f"Заявка {self.request_id}: {self.description}"

# Функція для автоматичної генерації заявок
def generate_request(queue, request_id_counter):
    while not stop_event.is_set():
        if stop_event.is_set():
            break
        # Створюємо нову заявку з унікальним ідентифікатором
        description = f"Опис заявки {request_id_counter}"
        new_request = Request(request_id_counter, description)
        queue.put(new_request)
        print(f"[Нова заявка] {new_request}")
        request_id_counter += 1
        
        # Затримка між генерацією нових заявок (імітація часу)
        time.sleep(random.uniform(1, 3))

# Функція для обробки заявок
def process_request(queue):
    while not stop_event.is_set() or not queue.empty():
        if stop_event.is_set():
            break
        # Чекаємо поки з'явиться заявка для обробки
        request = queue.get()
        print(f"[Обробка] {request}")
        
        # Імітуємо час на обробку
        time.sleep(random.uniform(2, 5))
        
        # Позначаємо, що обробка заявки завершена
        queue.task_done()
        print(f"[Завершено] {request}")

if __name__ == "__main__":
    try:
        # Створюємо чергу для зберігання заявок
        request_queue = queue.Queue()
        stop_event = threading.Event()  # Подія для зупинки потоків
        request_id_counter = 1

        # Запускаємо поток для генерації заявок
        generator_thread = threading.Thread(target=generate_request, args=(request_queue, request_id_counter))
        generator_thread.daemon = True
        generator_thread.start()

        # Запускаємо поток для обробки заявок
        processor_thread = threading.Thread(target=process_request, args=(request_queue,))
        processor_thread.daemon = True
        processor_thread.start()

        # Чекаємо завершення обробки всіх заявок (можна використовувати для завершення програми)
        request_queue.join()
    except KeyboardInterrupt:
        # Надсилаємо сигнал для зупинки потоків
        stop_event.set()
        print("Завершення програми...")
        request_queue.join()
