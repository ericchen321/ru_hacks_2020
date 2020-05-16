import psutil

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
    checkZoomVideoStatus('zoom.us')
   
