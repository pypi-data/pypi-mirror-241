# launcher.py

import threading
import webserv
import __main__

def launch_both():
    # Start module1 in a new thread
    thread = threading.Thread(target=webserv.run)
    thread.start()

    # Start module2 in the main thread
    __main__.run()
