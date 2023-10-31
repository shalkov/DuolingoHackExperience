import duolingo_requests
import time
import threading


def send_requests():
    data = duolingo_requests.send_session_request()
    myId = data["id"]
    duolingo_requests.send_batch_request(myId)


def my_timer(interval):
    data = threading.local()
    data.counter = 1
    while True:
        time.sleep(interval)
        send_requests()
        data.counter += 1


if __name__ == '__main__':
    for x in range(1, 11):
        thread = threading.Thread(target=my_timer, name="Thread " + str(x), args=(x,), daemon=True)
        thread.start()

    input('Привет, это скрипт для накрутки рейтинга в Dualingo')
