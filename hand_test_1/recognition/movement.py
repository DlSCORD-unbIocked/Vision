from pynput.mouse import Button, Controller

mouse = Controller()


def move_to_segment(segment: int, landmarks: list):
    # Move the mouse to the center of the segment
    mouse.position = (int(landmarks[segment][0]), int(landmarks[segment][1]))


def click():
    mouse.click(Button.left, 1)


def mouse_up():
    mouse.release(Button.left)


def mouse_press():
    mouse.press(Button.left)
