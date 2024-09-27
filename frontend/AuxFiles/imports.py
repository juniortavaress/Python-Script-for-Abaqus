import os
import sys
import json
import time
import psutil
import shutil
import pickle
import inspect
import rc_Icons
import itertools
import subprocess
import numpy as np
import concurrent.futures
import matplotlib.pyplot as plt

from Simulation.managerThread import WorkerThread
from Geometry.facesGenerator import FacesGenerator

from PySide6.QtCore import QTimer, QThread
from PySide6.QtGui import QScreen, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

