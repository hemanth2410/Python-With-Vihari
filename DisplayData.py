import numpy as np
import pandas as pd
import collections as Counter
from random import shuffle
import cv2
import os

Files = os.listdir('E:\COde\MachineLearning\PyPlaysGta\PyPlaysGta');
for file in Files:
    if file.endswith('.npy'):
        print(file)
        train_data = np.load(file)
        for data in train_data:
            img = data[0]
            choice = data[1]
            cv2.imshow('test',img)
            print(choice)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

