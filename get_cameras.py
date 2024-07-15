import cv2
import time


def list_ports():
    """
    Script for listing available and working ports for cameras. source: stackoverflow
    """
    is_working = True
    dev_port = 0
    t = time.time()
    working_ports = []
    available_ports = []
    while is_working:
        # different api_preference depending on hardware
        # See https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ga023786be1ee68a9105bf2e48c700294d for more info
        camera = cv2.VideoCapture(dev_port, cv2.CAP_DSHOW)
        print(time.time() - t)
        if not camera.isOpened():
            is_working = False
            print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print(
                    "Port %s is working and reads images (%s x %s)" % (dev_port, h, w)
                )
                working_ports.append(dev_port)
            else:
                print(
                    "Port %s for camera ( %s x %s) is present but does not reads."
                    % (dev_port, h, w)
                )
                available_ports.append(dev_port)
        dev_port += 1
    return available_ports, working_ports


a, b = list_ports()
print(a, b)
