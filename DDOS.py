import threading 
import requests
target_url = "http://127.0.0.1:5000"
def send_requests():
    while True: 
        try:
            response = requests.get(target_url) 
            print(f"Request sent: {response.status_code}") 
        except Exception as e:
            print(f"Error: {e}")

num_threads = 100
 
threads = []
for i in range(num_threads): 
    thread = threading.Thread(target=send_requests)
    thread.start() 
    threads.append(thread)