import time
import psutil
import logging
from voice_recognition import voice_rcog
from IMDB_Keras import sentimental_run
from queue import Queue
import threading

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

logging.basicConfig(level=logging.ERROR,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


# check tartget(app) status
def checkAppStatus(target):
    # return true if the process is running
    return "zoom.us" in (p.name() for p in psutil.process_iter())

# check target(app) thread number
def checkAppThreadNumber(target):
    for p in psutil.process_iter():
        if p.name() == target:
            return p.num_threads()
        else:
            continue 
        
# check zoom video is on or off
def checkZoomVideoStatus(target):
    while(True):
        if checkAppStatus(target) == True:
            thread_num = checkAppThreadNumber(target)
            print("{} is running, it has {} threads ".format(target, thread_num))
            if int(thread_num) > 32:
                print("Thread number bigger than threshold, the camera is on .....")
            else:
                print("Thread number is below the threshold")
        else:
            continue            


if __name__ == "__main__":
    #checkZoomVideoStatus('zoom.us')
    logging.info("Zoomate Device Starts Working ....")

    wordsQueue = Queue()
    wordProducer = threading.Thread(target=voice_rcog.process_voice_recognition, args=(wordsQueue,))
    wordConsumer = threading.Thread(target=sentimental_run.real_time_analysis, args=(wordsQueue,))
    wordProducer.start()
    wordConsumer.start()

    wordsQueue.join()

   
