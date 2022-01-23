import time
import numpy as np
import pyvirtualcam

colors = [
    ('RED', np.array([255, 0, 0], np.uint8)),
    ('GREEN', np.array([0, 255, 0], np.uint8)),
    ('BLUE', np.array([0, 0, 255], np.uint8))
]

with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:
    print(f'Using virtual camera: {cam.device}')
    frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB
    while True:
        frame[:,:] = color
        print(frame[:,:])


        
        cam.send(frame)
        cam.sleep_until_next_frame()