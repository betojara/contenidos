import threading
import time


def worker():
    print(f"{threading.current_thread().name} partiendo...")
    time.sleep(2)
    print(f"{threading.current_thread().name} saliendo...")


def service():
    print(f"{threading.current_thread().name} partiendo...")
    time.sleep(4)
    print(f"{threading.current_thread().name} saliendo...")


# Forma 1 de hacer un thread daemon
t1 = threading.Thread(name="Service", target=service, daemon=True)
# Forma 2 de hacer un thread daemon
w1 = threading.Thread(name="Worker", target=worker)
w1.daemon = True

# Prueba el código colocando daemon=True y daemon=False en ambos threads

# Se inicializan los threads
w1.start()
t1.start()
