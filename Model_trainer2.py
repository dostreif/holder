import cv2
import numpy as np
from Classification_model2 import Classification_model as Cm


# Script for training different models


cm = Cm("conv_net_real_time")
cm.load_model()
cm.train_model()
