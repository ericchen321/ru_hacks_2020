import psutil

# target - process name / app name
def checkAppStatus(target):
    # return true if the process is running
    return "zoom.us" in (p.name() for p in psutil.process_iter())




if __name__ == "__main__":
    app_status = checkAppStatus('zoom.us')
    print(app_status)


