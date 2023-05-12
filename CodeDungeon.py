import datetime
import json
from logging import exception
import os
import string
import time
from tkinter import ttk
import accounts_omac
import random
import tkinter
from PIL import Image, ImageTk, ImageEnhance
import math
import copy
from tkinter.messagebox import showerror, askyesno, showinfo


class System:

    version = {"name":"Version 1.3.5", "number":2}

    _sightFurthest = []

    #some default levels
    _defaultlevels = {"default":[
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 5, 5, 1, 0, 0, 0, 0, 0], [0, 1, 5, 5, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]],
    [[5, 1, 5, 0, 0, 0, 4, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 5, 1, 0], [0, 1, 1, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1, 1, 1, 0], [0, 0, 0, 4, 1, 0, 1, 4, 5, 0], [0, 0, 0, 0, 1, 0, 1, 5, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [4, 0, 1, 0, 1, 1, 1, 4, 0, 0], [4, 5, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 5, 4], [0, 0, 4, 0, 0, 1, 0, 1, 0, 4], [1, 1, 1, 1, 0, 1, 0, 1, 1, 1], [1, 0, 5, 1, 0, 1, 0, 0, 0, 0], [0, 5, 4, 1, 0, 1, 4, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 5, 1, 5]],
    [[0, 0, 1, 0, 4, 5, 1, 4, 1, 2], [4, 0, 0, 4, 0, 0, 0, 0, 1, 0], [5, 4, 1, 0, 5, 4, 1, 0, 1, 0], [4, 0, 1, 0, 4, 0, 1, 0, 1, 0], [1, 0, 1, 5, 0, 4, 1, 3, 1, 0], [0, 5, 4, 1, 1, 1, 1, 1, 1, 0], [4, 0, 0, 1, 4, 0, 0, 4, 0, 0], [0, 0, 4, 1, 0, 4, 5, 0, 0, 0], [5, 0, 0, 0, 0, 5, 0, 5, 1, 0], [4, 0, 0, 1, 4, 0, 0, 4, 1, 3]],
    [[4, 0, 4, 0, 1, 2, 1, 4, 5, 4], [4, 5, 0, 4, 1, 0, 1, 0, 4, 0], [0, 4, 0, 0, 0, 0, 1, 4, 5, 4], [0, 0, 4, 0, 1, 0, 1, 0, 4, 0], [4, 0, 5, 4, 1, 0, 0, 4, 5, 4], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 4, 0, 4, 1, 0, 1, 4, 0, 4], [4, 5, 4, 0, 1, 0, 1, 0, 5, 0], [0, 4, 0, 4, 0, 0, 1, 0, 4, 4], [4, 5, 4, 0, 1, 3, 1, 5, 0, 0]],
    [[3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 3], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 3, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 3, 1, 1, 1, 0, 0], [3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 3]],
    [[4, 0, 4, 1, 0, 2, 1, 4, 5, 4], [4, 5, 0, 1, 7, 0, 1, 0, 4, 0], [0, 4, 0, 0, 1, 0, 1, 4, 5, 4], [0, 0, 4, 0, 0, 0, 1, 0, 4, 0], [4, 0, 5, 0, 1, 0, 0, 4, 5, 4], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 4, 0, 4, 1, 0, 1, 4, 0, 4], [4, 5, 4, 0, 1, 0, 1, 0, 5, 0], [0, 4, 0, 4, 0, 0, 1, 0, 4, 4], [4, 5, 4, 0, 1, 3, 1, 5, 0, 7]],
    [[4, 5, 4, 0, 5, 0, 1, 4, 0, 0], [4, 8, 4, 0, 4, 8, 1, 5, 5, 4], [1, 0, 1, 1, 1, 6, 1, 4, 0, 0], [4, 0, 1, 0, 0, 1, 1, 1, 0, 1], [0, 5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 1, 0, 0, 4, 1, 1, 1, 5], [0, 1, 1, 1, 1, 1, 1, 0, 1, 0], [4, 0, 0, 1, 0, 0, 0, 4, 1, 0], [0, 5, 8, 1, 0, 5, 0, 0, 1, 0], [4, 0, 4, 1, 4, 0, 0, 5, 1, 0], [0, 1, 5, 1, 0, 1, 1, 1, 1, 4], [0, 1, 0, 0, 5, 0, 1, 5, 5, 0], [0, 1, 1, 1, 0, 0, 1, 0, 0, 4], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0], [5, 1, 1, 1, 4, 0, 0, 1, 4, 0], [0, 0, 0, 1, 0, 0, 0, 1, 5, 0], [1, 0, 1, 1, 0, 0, 0, 1, 0, 4], [0, 0, 4, 1, 0, 1, 1, 1, 1, 0], [4, 5, 5, 1, 5, 4, 1, 4, 4, 4], [0, 0, 4, 1, 0, 5, 0, 4, 5, 4]],
    [[1, 4, 0, 0, 5, 0, 4, 1, 0, 3], [0, 1, 1, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 5, 0, 0], [2, 0, 1, 5, 0, 1, 0, 0, 1, 0], [0, 0, 4, 1, 0, 5, 1, 1, 4, 1], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 5, 1, 4, 1, 5, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 5, 0, 0, 1, 1, 0, 1], [4, 0, 0, 1, 4, 0, 5, 0, 0, 5]],
    [[4, 0, 7, 0, 1, 4, 0, 0, 8, 4], [8, 5, 5, 4, 0, 0, 0, 4, 5, 0], [8, 0, 8, 0, 1, 8, 8, 0, 0, 8], [0, 8, 0, 4, 1, 4, 0, 0, 4, 0], [1, 0, 1, 1, 1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1], [5, 0, 0, 4, 1, 4, 0, 4, 0, 4], [0, 0, 5, 0, 1, 5, 8, 0, 8, 5], [0, 0, 0, 4, 0, 4, 0, 4, 0, 6]],
    [[0, 4, 0, 1, 0, 5, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 1, 4, 4], [0, 5, 0, 0, 0, 1, 0, 1, 1, 1, 0, 5, 0, 1, 4, 5, 0, 0, 8, 5], [4, 5, 4, 1, 0, 1, 6, 1, 0, 5, 4, 8, 0, 1, 1, 0, 1, 1, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 5, 0, 0, 0, 4, 1, 0, 5, 0, 4, 0, 0, 1, 0, 0, 0, 1, 4, 5], [5, 4, 1, 0, 0, 0, 0, 0, 0, 1, 0, 5, 0, 1, 4, 0, 1, 7, 8, 0], [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1], [4, 4, 1, 1, 1, 1, 1, 0, 5, 1, 5, 0, 4, 6, 1, 0, 1, 4, 5, 4], [5, 4, 1, 0, 5, 4, 1, 0, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 5, 0], [4, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 5, 0, 1, 0, 4, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 1, 6, 4, 1, 4, 7], [0, 1, 1, 5, 1, 0, 5, 1, 0, 0], [5, 1, 3, 0, 1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 5, 0, 0, 1, 0], [0, 0, 4, 1, 4, 0, 1, 5, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0, 6], [4, 1, 0, 0, 5, 0, 0, 1, 0, 1], [4, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 3, 0, 1, 4, 0, 1, 1, 5], [2, 1, 1, 0, 0, 0, 1, 3, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[4, 5, 4, 0, 5, 0, 1, 4, 0, 0], [4, 4, 4, 1, 4, 5, 1, 5, 5, 4], [1, 1, 1, 1, 1, 0, 1, 4, 0, 0], [4, 0, 1, 0, 0, 0, 1, 1, 0, 1], [0, 5, 1, 0, 2, 0, 0, 0, 0, 0], [0, 4, 1, 0, 0, 4, 1, 1, 1, 5], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [4, 0, 0, 1, 0, 0, 0, 4, 1, 0], [0, 5, 5, 0, 0, 5, 0, 0, 1, 0], [4, 0, 4, 1, 4, 0, 0, 5, 1, 3]],
    [[0, 1, 5, 0, 0, 4, 1, 4, 0, 4], [0, 1, 0, 0, 5, 0, 0, 5, 5, 0], [0, 1, 4, 0, 0, 0, 1, 0, 0, 4], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0], [5, 1, 1, 1, 4, 0, 0, 1, 4, 0], [0, 0, 0, 1, 0, 2, 0, 1, 5, 0], [1, 0, 1, 1, 0, 0, 0, 1, 0, 4], [0, 0, 4, 1, 0, 1, 1, 1, 1, 1], [4, 5, 5, 1, 5, 4, 1, 4, 4, 4], [0, 0, 4, 1, 0, 5, 0, 4, 5, 4]],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 0, 0, 0, 0, 1, 4, 0, 1], [1, 1, 0, 1, 1, 0, 0, 0, 0, 1], [1, 6, 0, 4, 1, 0, 1, 5, 4, 1], [1, 4, 0, 0, 1, 5, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 4, 0, 5, 1, 0, 0, 0, 4, 1], [1, 4, 0, 0, 1, 0, 1, 5, 0, 1], [1, 0, 0, 4, 1, 3, 1, 0, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [[4, 5, 4, 0, 5, 0, 1, 4, 0, 0], [4, 4, 4, 1, 4, 5, 1, 5, 5, 4], [1, 1, 1, 1, 1, 0, 1, 4, 0, 0], [4, 0, 1, 0, 0, 0, 1, 1, 0, 1], [0, 5, 1, 0, 2, 0, 0, 0, 0, 0], [0, 4, 1, 0, 0, 4, 1, 1, 1, 5], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [4, 0, 0, 1, 0, 0, 0, 4, 1, 0], [0, 5, 5, 1, 0, 5, 0, 0, 1, 0], [4, 0, 4, 1, 4, 0, 0, 5, 1, 3], [1, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 4, 0, 1], [1, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 7, 0, 4, 1, 0, 1, 5, 4, 1], [1, 4, 0, 0, 1, 5, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 4, 0, 5, 1, 0, 0, 0, 4, 1], [1, 4, 0, 0, 1, 0, 1, 5, 0, 1], [1, 0, 0, 4, 1, 3, 1, 0, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 4, 1, 1, 5, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 5, 1, 1, 4, 0, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, ['?', 6, 5, 7]], [0, 0, 1, 0, 1, 0, 0, 0, 4, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, [6, 'Somewhere in this room should be another sign that is more usefull'], 0, 5, 1, 1, 1, 1, 4, 4, 4, 5, 5, 1, 1, 0], [0, 5, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 5, 4, 0, 0], [0, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 4, 0, 0, 3, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 5, 1, 0, 5, 0, 0, 1, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 0, 0, 5, 0, 1, 0, 0, 0, 0, [6, "This should lead to a room with nice loot."]], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 4, 0, 0, 0, {"tile": "exit","entity": "NONE","loot": "NONE","lock": "NONE", "exit": {'exit': True, 'nextLevelList': "bonusRoom"}}]],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 4, 4, 0, 4, 0, 0, 4], [1, [{"tile": "floor", "entity": "NONE", "loot": {"type": "bandaid", "amount": 1}, "lock": {"Strength": 50, "item": {"type": "silver_key", "amount": 1}}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bandaid", "amount": 1}, "lock": {"Strength": 50, "item": {"type": "golden_key", "amount": 1}}}], 1, 1, 1, 1, 1, 1, 4, 3], [1, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 1, 7, 3], [0, 0, 0, 0, 1, 1, 1, 1, 0, 8], [0, 0, 1, 0, 0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 1], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3], [0, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}], 8, 1, 4, 0, 0, 0, 0, 0, 0], [0, 1, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}], 1, 1, 1, 0, 4, 0, 0, 0], [0, 1, 8, 8, 0, 1, 5, 0, 0, 0, 0], [0, 1, 8, 8, 8, 1, 4, 1, 1, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}], 1], [0, 1, [{"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 8, ["?", {"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 1, 5, 1, 8, 8, 1], [0, 1, 1, 1, 1, 1, 4, 1, 8, 8, 1], [0, 0, 0, [7, ["This levelfile is big boi", "This text was added without the creator knowing if it would work", "Are you spiderman?", "I think i saw iron man fly by 10 minutes ago, if you are fast you might catch him", "These rooms all have a high lock cost, some rooms have loot, others lead you to special bunkers, look from outside and see which one u want before unlocking"]], 0, 0, 0, 1, ["?", {"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 8, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0, 0, 4, 6], [0, 1, ["?", {"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, 
    {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 8, 8, 1, 0, 0, 0, 5, 0], [0, 1, 8, 8, 8, 1, 0, 0, 0, 0, 4], [0, 1, 6, 8, 0, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}], 0, 0, 4, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 4, 0, 0, 0, 0, 1, 1, 1, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}]], [0, 1, 1, 1, 1, 1, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}], 1, 8, 8, 8], [0, 1, ["?", {"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 8, 8, 1, 0, 1, 8, 8, 8], [0, 1, 8, 8, 8, 1, 0, 1, 8, 8, 8], [0, 1, 8, 8, 8, 1, 0, 1, 8, 8, 8], [2, 1, [{"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 8, 8, ["?", {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"HP": 200}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Strength": 50}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"Level": 20}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "golden_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_key", "amount": 1}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "gold_coin", "amount": 10}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "silver_coin", "amount": 50}}}, {"tile": "closedDoor", "entity": "NONE", "loot": "NONE", "lock": {"item": {"type": "bronze_coin", "amount": 250}}}, {"tile": "closedDoor", "entity": "true", "loot": "true", "lock": {"item": {"type": "stone_sword", "amount": 7}}}], 0, 1, ["?", {"tile": "floor", "entity": "true", "loot": {"type": "golden_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 25}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bread", "amount": 30}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bread", "amount": 35}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_key", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "floor_dice", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "butterfly_knife", "amount": 1}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "gold_coin", "amount": 11}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "gold_coin", "amount": 11}, "lock": {"item": "true"}}, {"tile": "floor", "entity": "NONE", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "silver_coin", "amount": 55}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "true", "loot": {"type": "bronze_coin", "amount": 274}, "lock": "NONE"}, {"tile": "floor", "entity": "NONE", "loot": {"type": "battle_axe", "amount": 1}, "lock": "NONE"}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": "NONE", "exit": {"exit": True, "nextLevelList": "bonusRoom"}}, {"tile": "exit", "entity": "NONE", "loot": "NONE", "lock": {"item": "true"}, "exit": {"exit": True, "nextLevelList": "bonusRoom"}}], 8, 8]]
    ],"bonusRoom": [
      [[4, 4, 4, 3, 1, 3, 4, 4, 4, 1], [4, 0, 0, 4, 1, 4, 0, 0, 4, 1], [4, ['?', 4, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'butterfly_knife', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'gold_coin', 'amount': 11}, 'lock': 'NONE'}], 0, 4, 1, 4, 0, ['?', 4, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'golden_key', 'amount': 1}, 'lock': 'NONE'}], 4, 1], [4, 4, 4, 4, 1, 4, 4, 4, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 4, 4, 4, 1, 4, 4, 4, 4, 1], [4, ['?', 4, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'floor_dice', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'butterfly_knife', 'amount': 1}, 'lock': 'NONE'}], 0, 4, 1, 4, 0, ['?', 4, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'golden_key', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'bread', 'amount': 25}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'bread', 'amount': 30}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'bread', 'amount': 35}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'silver_key', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'silver_key', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'floor_dice', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'butterfly_knife', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'gold_coin', 'amount': 11}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'gold_coin', 'amount': 11}, 'lock': {'item': 'true'}}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'silver_coin', 'amount': 55}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'silver_coin', 'amount': 55}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'bronze_coin', 'amount': 274}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'bronze_coin', 'amount': 274}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'battle_axe', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'exit', 'entity': 'NONE', 'loot': 'NONE', 'lock': 'NONE', 'exit': {'exit': True, 'nextLevelList': 'bonusRoom'}}, {'tile': 'exit', 'entity': 'NONE', 'loot': 'NONE', 'lock': {'item': 'true'}, 'exit': {'exit': True, 'nextLevelList': 'bonusRoom'}}], 4, 1], [4, 0, 0, 4, 1, 4, 0, 0, 4, 1], [4, 4, 4, 3, 1, 3, 4, 4, 4, 1]],
      [[1, 5, 5, 5, 0, 0, 5, 5, 5, 1], [4, 1, ['?', {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'floor_dice', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'butterfly_knife', 'amount': 1}, 'lock': 'NONE'}], 5, 0, 0, 5, ['?', {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'butterfly_knife', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'gold_coin', 'amount': 11}, 'lock': 'NONE'}], 1, 4], [4, 4, 1, 5, 0, 0, 5, 1, 4, 4], [4, 4, 4, 1, 3, 3, 1, 4, 4, 4], [4, 0, 4, 3, 1, 1, 3, 4, 0, 4], [4, 4, 4, 1, 3, 3, 1, 4, 4, 4], [4, 4, 1, 5, 0, 0, 5, 1, 4, 4], [4, 1, ['?', {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'golden_key', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'bread', 'amount': 25}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'bread', 'amount': 30}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'bread', 'amount': 35}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'silver_key', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'silver_key', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'floor_dice', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'butterfly_knife', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'gold_coin', 'amount': 11}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'gold_coin', 'amount': 11}, 'lock': {'item': 'true'}}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'silver_coin', 'amount': 55}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'silver_coin', 'amount': 55}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'bronze_coin', 'amount': 274}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'bronze_coin', 'amount': 274}, 'lock': 'NONE'}, {'tile': 'floor', 'entity': 'NONE', 'loot': {'type': 'battle_axe', 'amount': 1}, 'lock': 'NONE'}, {'tile': 'exit', 'entity': 'NONE', 'loot': 'NONE', 'lock': 'NONE', 'exit': {'exit': True, 'nextLevelList': 'bonusRoom'}}, {'tile': 'exit', 'entity': 'NONE', 'loot': 'NONE', 'lock': {'item': 'true'}, 'exit': {'exit': True, 'nextLevelList': 'bonusRoom'}}], 5, 0, 0, 5, ['?', {'tile': 'floor', 'entity': 'true', 'loot': {'type': 'golden_key', 'amount': 1}, 'lock': 'NONE'}], 1, 4], [1, 5, 5, 5, 0, 0, 5, 5, 5, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
      [[2], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [3]],

    ]}
    
    bugmessage = []
    _buttonsList = []
    #melee, throwables, magic
    _enemies = []
    _loot = []
    _itemRarety = {}
    _items = []
    _rarityChance= {}
    _images = {}

    defaultNPCText = ["I am the great Cackletta's most best pupil, who is named Fawful! I am here, laughing at you! If you are giving us the chase, just to get your silly princess's voice, then you are idiots of foolishness! Princess Peach's sweet voice will soon be the bread that makes the sandwich of Cackletta's desires! And this battle shall be the delicious mustard on that bread! The mustard of your doom!",
      "Fink-rat!", "Have you readiness for this?!?", "Now is when I ram you!", "O Great Cackletta, unleash the voice of Princess Peach on the Beanstar when you are wanting to!", "Now is the time where my true might shines like many angry sunbeams of rage!", "Hah! Now taste the finale, when carelessness opens the door to a comeback not expected by you! Your lives that I spit on are now but a caricature of a cartoon drawn by a kid who is stupid! You shall all fall and vanish with your precious Beanbean Kingdom as I laugh heartily at you!",
      "In the last moments of the finale of the finale, when relief leads to negligence that begets rashness... That is when the comeback that faltered comes back and beats your pathetic comeback that I scoff at!", "O Great Bowletta! The Mario Bros. who I hate are coming this way!", "Yes...Moustache...", "At last, my entrance with drama!","Stop it...such mumbling...", "ONE FELL SWOOP IS HOW I WILL DEAL WITH YOU FINK-RATS!!!",
      "Next it is the turn of you!", "You! You are the fink-rats that came with the Bowser that I hate!", "I HAVE FURY!","Ouch! Hotness! It is the overheat!", "I have boredom...Guests? Now I have... FURY!", "I say to you WELCOME! Welcome to Fawful's Bean 'n' Badge!", "In this place, beans are like precious treasure milked from a famous cow made of jewels!", "All who come with beans leave with badges so rare they make mustaches droop with disbelief!",
      "What? The story of Fawful? Your words are not beans. I am not wanting them.", "You are like brainless cats that are too dumb to know they are stupid! You have curiosity... ...But my tale is long, so long it makes babies old and hairy lips grow grey with aging. Do you dare hear?", "I am here, merchant of badges, only sometimes with fury, but I once had fury at all times.", "I drizzled rage dressing on the country next door. Rage dressing on a salad of evil!",
      "Red and green puts the fog of rage in my eyes, and my mind goes crazy.","P-Please... I will be fine. No worrying for Fawful. We talk of beans.","Beans and badges... We begin trading!","The beans hide in the dirts of this country like dirt-fish who like to eat dirt for dinner. Bean symbols like this are marking all bean spots.","You are digging in dirt, right? You are digging under symbols. And you are finding much bean!","Bean symbols have sneakiness! When the beans are gone, the symbols flee like babies!",
      "You are wanting much beans? Then you are hunting symbols. And digging and popping.","There are even places to win beans in games, maybe...","If you get many beans, you get many badges at this place, Fawful's Bean 'n' Badge!","I HAVE FURY!"]
    
    defaultSignText = ['I am probably older than you are; my friendly traveler reading this.','This text took 49 bytes to store on your computer','I was a tree', 'I was Groot','Don\'t listen to the NPCs, They only speak nonsense','I am empty, wait did i just create a paradox?','Go left and then right','Danger ahead', 'Greetings traveler, be aware of Fawful.']
      

    #load Json
    try:
        os.mkdir('gameData/')
    except:
        pass
    if os.path.exists(f'gameData/gameData.json'):
        with open(f'gameData/gameData.json') as json_file:
            dataString = json.load(json_file)
            if type(dataString) != dict:
                dataDict = json.loads(dataString)
            else:
                dataDict= dataString

    else:
        dataDict = {}
        dataDict['template'] = {"tile": "NONE", "entity": "NONE", "loot": "NONE", "lock": "NONE", 'exit': {'exit': False}}
        dataDict['version'] = version
        dataDict['preference'] = {'autoEquipBetter': True, 'sleepTime':0.1}
        dataDict['startingLoot'] = {'wooden_sword': {'amount': 1}}
        dataDict['equippedWeapon'] = {'weapon': 'wooden_sword', 'weight': 1}
        dataDict['playerStats'] = {'statsPerLevel':{'HP':10, 'strength':4}, 'beginStats':{'HP':5, 'strength':5}, 'startLevel': 3, 'XPneeded': {'multiplyByLevel':50, 'startingNumber':10}}
        dataDict['dungeon'] = {'startLevel': 3, "defaultLevelList": "default", "startingFloor" : 1}
        dataDict['balancing'] = {'doStrengthDamage': True, 'strengthDevidedBy': 3, 'killMultiplierXP': 2, 'XPperDamageDevidedBy' : 1, 'entetyLootDroppingChance': 50}
        dataDict['rarities'] = {'common': {'chance': 88},'uncommon': {'chance': 69},'rare': {'chance': 40},'epic': {'chance': 25},'legendary': {'chance': 11},'impossible': {'chance': 1}}
        dataDict['chance'] = {'enemyAir' : 5, 'enemySpawn': 40, 'lootAir' : 3, 'lootSpawn' : 40, 'defaultEntitySpawningWeight': 8}
        dataDict['appSettings'] = {'offset': 18,'size': 32, 'maxTypes': 9, 'colors': ['white','black','green', 'blue', 'pink', 'red', 'brown', 'orange', 'white', 'purple'], 'unknown': {'color': 'white', 'text': 'Modified'}}
        dataDict['playerImages'] = {'L': 'player left', 'R': 'player right'}
        dataDict['debug']= {'logging' : False, 'combat' : True, 'enemyAI' : True, 'sleep': True, 'enemyLoop': 2, 'enemyLoopPerEnemy':2, 'replayMode': False, 'allowDebugTeleport': False}
        dataDict['Gamma'] = {'distance': 2, 'darknessFull' : 0.2, 'darknessFade' : 0.5}
        dataDict['text'] = {'signText': defaultSignText, 'npcText': defaultNPCText}

        dataDict['defaultTiles'] = {'floor': ['floor'], 'wall': ['wall'], 'exit': ['exit'], 'sign': ['sign'], 'npc': ['npc']}

        dataDict['tiles'] = {}
        dataDict['tiles']['missingTile'] = {'ShowOutsideAs': 'missingTile', 'Walkable': True,'Image': 'textureMissing', 'isEnemy': False, 'isInteractable': False,'isLoot': False}

        dataDict['tiles']['exit'] = {'ShowOutsideAs': 'floor', 'Walkable': True,'Image': 'exit', 'isEnemy': False, 'isInteractable': False,'isLoot': False}
        dataDict['tiles']['npc'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'npc', 'isEnemy': False, 'isInteractable': True, 'isLoot': False, 'text': 'npcText'}
        dataDict['tiles']['wall'] = {'ShowOutsideAs': 'wall','Walkable': False, 'Image': 'wall', 'isEnemy': False, 'isInteractable': False,'isLoot': False}
        dataDict['tiles']['sign'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'sign', 'isEnemy': False, 'isInteractable': True,'isLoot': False, 'text': 'signText'}
        dataDict['tiles']['floor'] = {'ShowOutsideAs': 'floor','Walkable': True, 'Image': 'floor', 'isEnemy': False, 'isInteractable': False,'isLoot': False}
        dataDict['tiles']['openDoor'] = {'ShowOutsideAs': 'openDoor','Walkable': True, 'Image': 'openDoor', 'isEnemy': False, 'isInteractable': False,'isLoot': False}
        dataDict['tiles']['closedDoor'] = {'ShowOutsideAs': 'closedDoor','Walkable': False, 'Image': 'closedDoor', 'isEnemy': False, 'isInteractable': True,'isLoot': False, 'transform': {'TransformInto': 'openDoor'}}
        dataDict['tiles']['lockedDoor'] = {'ShowOutsideAs': 'closedDoor','Walkable': False, 'Image': 'lockedDoor', 'isEnemy': False, 'isInteractable': True,'isLoot': False, 'transform': {'TransformInto': 'openDoor'}}
        
        dataDict['tiles']['rat'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'rat', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':4,'ATK':2, 'deathXP' : 5},'lessATKpointsPercentage': 20, 'hitChance': 80, "movementRules": {"attackRule" : "insteadOf", "movement": 1, "attack": 1}, "spawnWeight": 10}, 'spawning': {'toFloor': 15}}
        dataDict['tiles']['lost rat'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'rat', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':4,'ATK':2, 'deathXP' : 5},'lessATKpointsPercentage': 20, 'hitChance': 80, "movementRules": {"attackRule" : "insteadOf", "movement": 1, "attack": 1}, "spawnWeight": 1}, 'spawning': {'fromFloor': 19, 'toFloor': 30}}
        dataDict['tiles']['white rat'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'white_rat', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':3,'ATK':2, 'deathXP' : 4},'lessATKpointsPercentage': 20, 'hitChance': 70, "movementRules": {"attackRule" : "insteadOf", "movement": 2, "attack": 0.9}, "spawnWeight": 5}, 'spawning': {'fromFloor': 10, 'toFloor': 20}}
        dataDict['tiles']['crab'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'crab', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':5,'ATK':2, 'deathXP' : 10},'lessATKpointsPercentage': 30, 'hitChance': 75, "movementRules": {"attackRule" : "and", "movement": 1, "attack": 1}, "spawnWeight": 8}, 'spawning': {'fromFloor': 12, 'toFloor': 30}}
        dataDict['tiles']['raveing crab'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'crab', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':6,'ATK':3, 'deathXP' : 50},'lessATKpointsPercentage': 40, 'hitChance': 85, "movementRules": {"attackRule" : "and", "movement": 1.4, "attack": 1}, "spawnWeight": 1}, 'spawning': {'fromFloor': 16, 'toFloor': 32}}
        dataDict['tiles']['mimic'] = {'ShowOutsideAs': 'mimic', 'Walkable': False, 'Image': 'mimic', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':2,'ATK':4, 'deathXP' : 12},'lessATKpointsPercentage': 20, 'hitChance': 70, "movementRules": {"attackRule" : "and", "movement": 0, "attack": 1}, "spawnWeight": 5}, 'spawning': {'fromFloor': 15}}
        dataDict['tiles']['skeleton'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'skeleton', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':2,'ATK':6, 'deathXP' : 25},'lessATKpointsPercentage': 20, 'hitChance': 80, "movementRules": {"attackRule" : "insteadOf", "movement": 1, "attack": 1}, "spawnWeight": 10}, 'spawning': {'fromFloor': 20}}
        dataDict['tiles']['thief'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'thief', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':4,'ATK':3, 'deathXP' : 30},'lessATKpointsPercentage': 10, 'hitChance': 90, "movementRules": {"attackRule" : "and", "movement": 1, "attack": 1}, "spawnWeight": 10}, 'spawning': {'fromFloor': 23}}
        dataDict['tiles']['sneaky thief'] = {'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'thief2', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'enemy':{'statsPerLevel': {'HP':4,'ATK':3, 'deathXP' : 44},'lessATKpointsPercentage': 20, 'hitChance': 80, "movementRules": {"attackRule" : "insteadOf", "movement": 1, "attack": 2}, "spawnWeight": 10}, 'spawning': {'fromFloor': 25}}
        
        dataDict['tiles']['wooden_sword'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1}, "isWeapon": True,"isConsumable": False,'rarity': 'NONE', 'weapon': {'minStrength': 17, 'attack': 8, 'type': 'stab', 'weaponWeight' : 1}}}
        dataDict['tiles']['sharp_rock'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'common', 'weapon': {'minStrength': 21, 'attack': 5, 'type': 'slice', 'weaponWeight' : 3}, "mergable": {"mergeAmount": 5, "mergeIntoAndAmount": {"sharpened_sharp_rock":1}}}, 'spawning': {'toLevel': 6, 'spawning': {'toFloor': 7}}}
        dataDict['tiles']['sharpened_sharp_rock'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'NONE', 'weapon': {'minStrength': 31, 'attack': 10, 'type': 'slice', 'weaponWeight' : 5}}}
        dataDict['tiles']['moldy_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':6},"isWeapon": False,"isConsumable": True,'rarity': 'common', 'consumable': {'HPAmount': 5, 'type': '+'}, "mergable": {"mergeAmount": 5, "mergeIntoAndAmount": {"old_bread":3}}}, 'spawning': {'toFloor': 8}}
        dataDict['tiles']['silver_coin'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':16},"isWeapon": False,"isConsumable": False,'rarity': 'common', "mergable": {"mergeAmount": 10, "mergeIntoAndAmount": {"golden_coin":1}}}}
        dataDict['tiles']['bronze_coin'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':45},"isWeapon": False,"isConsumable": False,'rarity': 'common', "mergable": {"mergeAmount": 10, "mergeIntoAndAmount": {"silver_coin":1}}}, 'spawning': {'toFloor': 14}}
        dataDict['tiles']['old_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':4},"isWeapon": False,"isConsumable": True,'rarity': 'common', 'consumable': {'HPAmount': 10, 'type': '+'}, "mergable": {"mergeAmount": 5, "mergeIntoAndAmount": {"bread":3}}}, 'spawning': {'toFloor': 16}}
        dataDict['tiles']['dusty_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':4},"isWeapon": False,"isConsumable": True,'rarity': 'common', 'consumable': {'HPAmount': 20, 'type': '+'}, "mergable": {"mergeAmount": 5, "mergeIntoAndAmount": {"fresh_bread":2}}}, 'spawning': {'fromFloor': 16, 'toFloor': 32}}
        dataDict['tiles']['bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':4},"isWeapon": False,"isConsumable": True,'rarity': 'uncommon', 'consumable': {'HPAmount': 20, 'type': '+'}, "mergable": {"mergeAmount": 10, "mergeIntoAndAmount": {"fresh_bread":6}}}, 'spawning': {'toFloor': 22}}
        dataDict['tiles']['fresh_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':4},"isWeapon": False,"isConsumable": True,'rarity': 'uncommon', 'consumable': {'HPAmount': 60, 'type': '+'}}, 'spawning': {'fromFloor': 22}}
        dataDict['tiles']['soggy_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':4},"isWeapon": False,"isConsumable": True,'rarity': 'uncommon', 'consumable': {'HPAmount': 20, 'type': '+'}}, 'spawning': {'fromFloor': 16, 'toFloor': 32}}
        dataDict['tiles']['stone_sword'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'uncommon', 'weapon': {'minStrength': 25, 'attack': 15, 'type': 'stab', 'weaponWeight' : 3}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"sharpened_stone_sword":1}}}}
        dataDict['tiles']['sharpened_stone_sword'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'NONE', 'weapon': {'minStrength': 35, 'attack': 22, 'type': 'stab', 'weaponWeight' : 5}}}
        dataDict['tiles']['bandaid'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'uncommon', 'consumable': {'HPAmount': 10, 'type': '%'}}}
        dataDict['tiles']['gold_coin'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':3},"isWeapon": False,"isConsumable": False,'rarity': 'uncommon'}}
        dataDict['tiles']['strength_potion'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'rare', 'consumable': {'HPAmount': 0, 'type': '+', 'strengthLevels': 1}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"big_strength_potion":1}}}, 'spawning': {'fromFloor': 15}}
        dataDict['tiles']['big_strength_potion'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'rare', 'consumable': {'HPAmount': 10, 'type': '+', 'strengthLevels': 4}}}
        dataDict['tiles']['iron_dagger'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'rare', 'weapon': {'minStrength': 20, 'attack': 15, 'type': 'stab', 'weaponWeight' : 4}}}
        dataDict['tiles']['hema_tompoes'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'rare', 'consumable': {'HPAmount': 50, 'type': '+'}}}
        dataDict['tiles']['hoe'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'rare', 'weapon': {'minStrength': 25, 'attack': 10, 'type': 'slice', 'weaponWeight' : 6}}}
        dataDict['tiles']['nameless_pill'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'epic', 'consumable': {'HPAmount': 37, 'type': 'set'}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"enchanted_nameless_pill":1}}}}
        dataDict['tiles']['enchanted_nameless_pill'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'NONE', 'consumable': {'HPAmount': 93, 'type': 'set'}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"overdose_enchanted_nameless_pills":1}}}}
        dataDict['tiles']['overdose_enchanted_nameless_pills'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'NONE', 'consumable': {'HPAmount': 234, 'type': 'set'}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"nameless_drugs":1}}}}
        dataDict['tiles']['nameless_drugs'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'NONE', 'consumable': {'HPAmount': 700, 'type': 'set'}}}
        dataDict['tiles']['paracetamol'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'epic', 'consumable': {'HPAmount': 35, 'type': '%'}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"suppository":3}}}}
        dataDict['tiles']['zetpil'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'NONE', 'consumable': {'HPAmount': 100, 'type': '%'}}}
        dataDict['tiles']['battle_axe'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'epic', 'weapon': {'minStrength': 45, 'attack': 25, 'type': 'stab', 'weaponWeight' : 6}, "mergable": {"mergeAmount": 3, "mergeIntoAndAmount": {"sharpened_battle_axe":1, 'bronze_coin': 25}}}}
        dataDict['tiles']['sharpened_battle_axe'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'NONE', 'weapon': {'minStrength': 45, 'attack': 30, 'type': 'slice', 'weaponWeight' : 8}}}
        dataDict['tiles']['butterfly_knife'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'legendary', 'weapon': {'minStrength': 50, 'attack': 15, 'type': 'slice', 'weaponWeight' : 7}}}
        dataDict['tiles']['sword_of_deception'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'legendary', 'weapon': {'minStrength': 80, 'attack': 44, 'type': 'stab', 'weaponWeight' : 9}}}
        dataDict['tiles']['healing_pod'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':4},"isWeapon": False,"isConsumable": True,'rarity': 'legendary', 'consumable': {'HPAmount': 100, 'type': '%'}}}
        dataDict['tiles']['floor_dice'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": False,'rarity': 'legendary', 'special': {'nextFloor': "default"}}, 'text': {'fromList': False, 'text': 'You suddenly wake up on another floor'}}
        dataDict['tiles']['vault_floor_dice'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": True,'rarity': 'legendary', 'special': {'nextFloor': "bonusRoom"}, 'consumable': {'HPAmount': 1, 'type': 'set'}}, 'text': {'fromList': False, 'text': 'You suddenly wake up on another floor with an immense headache'}}
        dataDict['tiles']['silver_key'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": False,'rarity': 'legendary'}}
        dataDict['tiles']['golden_key'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": False,'rarity': 'legendary'}, 'spawning': {'fromFloor': 7}}
        dataDict['tiles']['mjolnir'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'legendary', 'weapon': {'minStrength': 111, 'attack': 69, 'type': 'slice', 'weaponWeight' : 11}}, 'spawning': {'fromLevel': 15}}
        dataDict['tiles']['diamond_battle_axe'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'impossible', 'weapon': {'minStrength': 100, 'attack': 69, 'type': 'stab', 'weaponWeight' : 10}}}


        with open(f'gameData/gameData.json', 'w') as outfile:
            json.dump(dataDict, outfile, indent=2)

    #map data
    if os.path.exists(f'gameData/levelData.json'):
        with open(f'gameData/levelData.json') as level_json_file:
            levelDataString = json.load(level_json_file)
            if type(levelDataString) != dict and type(levelDataString) != list:
                levelDataDict = json.loads(levelDataString)
            else:
                levelDataDict = levelDataString
    else:
        with open(f'gameData/levelData.json', 'w') as outfile:
            json.dump(_defaultlevels, outfile)
        levelDataDict = _defaultlevels



    #change json into usable data part1
    try:
        colors =dataDict['appSettings']['colors']
        _viewDistance = dataDict['Gamma']['distance']
        maxTypes = dataDict['appSettings']['maxTypes']
        chanceEnemyAir = dataDict['chance']['enemyAir']
        chanceLootAir = dataDict['chance']['lootAir']
        chanceEnemySpawn = dataDict['chance']['enemySpawn']
        chanceLootSpawn = dataDict['chance']['lootSpawn']
        pixelOffset = dataDict['appSettings']['offset']
        pixelSize = dataDict['appSettings']['size']
        darknessFull = dataDict['Gamma']['darknessFull']
        darknessFade = dataDict['Gamma']['darknessFade']
        doLogging = dataDict['debug']['logging']
        doCombat = dataDict['debug']['combat']
        doEnemyMovement = dataDict['debug']['enemyAI']
        _enemyLevel = dataDict['dungeon']['startLevel']
        defaultPlayerStats = dataDict['playerStats']
        autoEquip = dataDict['preference']['autoEquipBetter']
        hasWeaponWeight = dataDict['equippedWeapon']['weight']
        equippedWeapon = dataDict['equippedWeapon']['weapon']
        doReplayMode = dataDict['debug']['replayMode']
    except Exception as e:
        print(e)
        print('something is wrong with the gameData/gameData.json, delete it or fix it.')
        bugmessage.append([e,'something is wrong with the gameData/gameData.json, delete it or fix it.'])

    try:
        _defaultlevels = levelDataDict
    except Exception as e:
        print(e)
        print('something is wrong with the gameData/levelData.json, delete it or fix it.')
        bugmessage.append([e,'something is wrong with the gameData/levelData.json, delete it or fix it.'])
    if 'version' in dataDict:
        if 'name' not in dataDict['version'] and 'number' not in dataDict['version']:
            dataDict['version']['name'] = f'unknown'
            dataDict['version']['number'] = -1
        elif 'name' not in dataDict['version']:
            dataDict['version']['name'] = f'unknown'
        elif 'number' not in dataDict['version']:
            dataDict['version']['number'] = -1
    else:
        dataDict['version'] = {'name': f'unknown', 'number': -1}

    now = datetime.datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    try:
        os.mkdir('logs/')
    except:
        pass
    try:
        os.mkdir('logs/logFiles/')
        os.mkdir('logs/replayFiles/')
    except:
        pass
    if doLogging:
        log = open(f'logs/logFiles/log{dt_string}.txt', "w")
        log.close()  
    if doReplayMode:
        replay = open(f'logs/replayFiles/replay{dt_string}.txt', "w")
        replay.close() 


    def __init__(self, seed : int = 0):
        self.logging('__init__()')
        try:
            self._dungeonLevel = self.dataDict['dungeon']['startingFloor'] - 1
        except:
            self._dungeonLevel = 0

        self._startingFloor = self._dungeonLevel
        random.seed(seed)
        self.seed = seed
        self.logging(seed,'seed')
        self.replayWrite(f'seed: {seed}')
        self.accountConfigSettings = accounts_omac.configFileTkinter()
        self.accountDataDict = accounts_omac.defaultConfigurations.defaultLoadingTkinter(self.accountConfigSettings)
        random.randint(1,10)
        self._nextStates = []
        self.newState()
        self.newState()
        self.checkStates()
        self._createdBefore = False
        self._playerX = 0
        self._playerY = 0
        self._facingDirectionTexture = 'R'
        self._facing = 'R'
        self.gameWindow = tkinter.Tk()
        self.gameWindow.configure(bg='black')
        self.gameWindow.title(f"CodeDungeon {self.version['name']}")
        self.gameWindow.attributes('-topmost', True)
        self.inventory = self.dataDict['startingLoot']
        self.gameWindow.protocol("WM_DELETE_WINDOW", self.exit)
        self.loadedLevel = []
        self.mode = 'Play'
        

        self.rarityList = []
        for rar in self.dataDict['rarities'].keys():
            self.rarityList.append(rar)

        #if no account has been logged into
        if self.accountDataDict == False:
            self.exit(False)

        if len(self.bugmessage) > 0:
            for x in range(len(self.bugmessage)):
                self.logging(self.bugmessage[x], 'function = __init__')

        #change json into usable data part2
        for player in self.dataDict['playerImages'].keys():
            self._images[f'darknessFull-{self.dataDict["playerImages"][player]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['playerImages'][player]}.png").convert('RGB')).enhance(self.darknessFull))
            self._images[f'darknessFade-{self.dataDict["playerImages"][player]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['playerImages'][player]}.png").convert('RGB')).enhance(self.darknessFade))
            self._images[f'normal-{self.dataDict["playerImages"][player]}'] = ImageTk.PhotoImage(Image.open(f"sprites/{self.dataDict['playerImages'][player]}.png"))
        for rarety in self.dataDict['rarities'].keys():
            self._itemRarety[rarety] = []
            self._rarityChance[rarety] = self.dataDict['rarities'][rarety]['chance']
        for data in self.dataDict['tiles'].keys():
            if self.dataDict['tiles'][data]['isEnemy']:
                self._enemies.append(data)
            if self.dataDict['tiles'][data]['isLoot']:
                if self.dataDict['tiles'][data]['loot']['rarity'] != 'NONE':
                    self._itemRarety[self.dataDict['tiles'][data]['loot']['rarity']].append(data)
                    self._items.append(data)
            try:
              self._images[f'darknessFull-{self.dataDict["tiles"][data]["Image"]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png").convert('RGB')).enhance(self.darknessFull))
              self._images[f'darknessFade-{self.dataDict["tiles"][data]["Image"]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png").convert('RGB')).enhance(self.darknessFade))
              self._images[f'normal-{self.dataDict["tiles"][data]["Image"]}'] = ImageTk.PhotoImage(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png"))
            except Exception as e:
              self.logging(e, 'probably texture isn\'t named correctly or doesn\'t exist')
              try:
                self._images[f'darknessFull-{self.dataDict["tiles"][data]["Image"]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/textureMissing.png").convert('RGB')).enhance(self.darknessFull))
                self._images[f'darknessFade-{self.dataDict["tiles"][data]["Image"]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/textureMissing.png").convert('RGB')).enhance(self.darknessFade))
                self._images[f'normal-{self.dataDict["tiles"][data]["Image"]}'] = ImageTk.PhotoImage(Image.open(f"sprites/textureMissing.png"))
              except Exception as e:
                self.logging(e, 'since we already had an texture error we tried to load, but now we have again, high chance that u deleted the "sprites/textureMissing.png", whyyyy, \nThe other possebility why you are getting this is an error with PILLOW or PIL, \nbut the first option is more likely if you changed the gameData.json or downloaded a version of the game that isn\'t made by the creator: oldmartijntje')
                showerror('error',f'{e}, look in the logfile')
                self.exit(False)
            
    
    def getCurrentVersion(self):
        print(f"The version of the game is {self.version['name']}, ID: {self.version['number']}")
        print(f"The version of the gameData.json is {self.dataDict['version']['name']}, ID: {self.dataDict['version']['number']}")
        return {'game':self.version['name'],'gameID':self.version['number'],'gameData':self.dataDict['version']['name'],'gameDataID':self.dataDict['version']['number']}

    #for when something is missign from the json
    def jsonError(self,error):
        self.logging('jsonError()')
        showerror('error', f'{error}\nerror code 0002')
        self.logging([error,'something is wrong with the gameData/gameData.json, delete it or fix it.'])
        self.exit(False)

    #generate a new state
    def newState(self, modifier = 0):
        self.logging('newState()')
        for x in range(random.randint(1,10)+ modifier):
            random.randint(1,10)
        self._nextStates.append(random.getstate())
        for x in range(random.randint(1,10)+ modifier):
            random.randint(1,10)
    
    #check if states are valid
    def checkStates(self):
        self.logging('checkStates()')
        x = 0
        while len(self._nextStates) < 2:
            self.newState()
        while self._nextStates[0] == self._nextStates[1]:
            x += 1
            self._nextStates.pop(0)
            self.newState(x)

    #load a state for the dungeon generation
    def loadState(self):
        self.logging(f'states len: {len(self._nextStates)}, LoadState()')
        random.setstate(self._nextStates[0])
        self._nextStates.pop(0)
        self.checkStates()

    #change tile type in the creator app
    def changeEditorButton(self,location, chosenLevel = 'non'):
        self.logging('changeEditorButton()')
        x, y = location
        self.loadedLevel[x][y]+= 1
        if self.loadedLevel[x][y] > self.maxTypes:
            self.loadedLevel[x][y] = 0
        self._buttonsList[x][y].configure(text=self.loadedLevel[x][y], bg = self.colors[self.loadedLevel[x][y]])

    #get a random rarity
    def itemRarity(self, modifier : int = 0):
        self.logging(f'itemRarity({modifier})')
        randomNumber = random.randint(0,100)
        randomNumber -= modifier
        chanceList = []
        for rarety in self.rarityList:
            chanceList.append(self._rarityChance[rarety] + modifier)
        return random.choices(self.rarityList, weights = chanceList, k = 1)[0]
    
    def randomEntity(self, listOfEntities):
        self.logging(f'randomEntity({listOfEntities})')
        chanceList = []
        for entity in listOfEntities:
            if 'spawnWeight' in self.dataDict['tiles'][entity]['enemy']:
                chanceList.append(self.dataDict['tiles'][entity]['enemy']['spawnWeight'])
            else:
                chanceList.append(self.dataDict['chance']['defaultEntitySpawningWeight'])
        return random.choices(listOfEntities, weights = chanceList)[0]

    def updateGameDataDict(self):
      with open(f'gameData/gameData.json', 'w') as outfile:
          json.dump(self.dataDict, outfile, indent=2)

    def updateLevelDataDict(self):
      with open(f'gameData/levelData.json', 'w') as outfile:
            json.dump(self._defaultlevels, outfile)


    #generate loot
    def getLoot(self, modifier: int = 0, chanceOfNothing: int = 100):
        self.logging(f'getLoot({modifier}, {chanceOfNothing}')
        if random.randint(1,99) < chanceOfNothing:
            while True:
                itemType = self.itemRarity(modifier)
                if len(self._itemRarety[itemType]) != 0:
                    itemList = list(self._itemRarety[itemType])
                    itemList = self.filterSpawning(itemList)
                    if len(itemList) != 0:
                        break
            item = itemList[random.randint(0,len(itemList)-1)]
            amount = random.randint(self.dataDict['tiles'][item]['loot']['amount']['min'], self.dataDict['tiles'][item]['loot']['amount']['max'])
            if type(amount) == list:
                amount = random.randint(amount[0], amount[1])
            loot = {'type':item, 'amount':amount}
            return loot
        else:
            return 'NONE'
        
    def filterSpawning(self, itemList):
        loop = 0
        for x in range(len(itemList)):
            passing = False
            if 'spawning' in self.dataDict['tiles'][itemList[loop]]:
                if not passing and 'fromLevel' in self.dataDict['tiles'][itemList[loop]]['spawning'] and self.dataDict['tiles'][itemList[loop]]['spawning']['fromLevel'] > self.playerStats['level']:
                    itemList.pop(loop)
                    loop -= 1
                    passing = True
                if not passing and 'toLevel' in self.dataDict['tiles'][itemList[loop]]['spawning'] and self.dataDict['tiles'][itemList[loop]]['spawning']['toLevel'] < self.playerStats['level']:
                    itemList.pop(loop)
                    loop -= 1
                    passing = True
                if not passing and 'fromFloor' in self.dataDict['tiles'][itemList[loop]]['spawning'] and self.dataDict['tiles'][itemList[loop]]['spawning']['fromFloor'] > self._dungeonLevel +1:
                    itemList.pop(loop)
                    loop -= 1
                    passing = True
                if not passing and 'toFloor' in self.dataDict['tiles'][itemList[loop]]['spawning'] and self.dataDict['tiles'][itemList[loop]]['spawning']['toFloor'] < self._dungeonLevel +1:
                    itemList.pop(loop)
                    loop -= 1
                    passing = True
            loop += 1
        return itemList

    #read tile of 2D erray and convert into map
    def readTile(self, tile, x, y, extra, levelNumber):
        #all numbers are different type of tile:
        #0 air
        #1 wall
        #2 start
        #3 next level
        #4 high chance of loot
        #5 high chance of enemy
        #6 sign
        #7 npc
        #8 nothing able to spawn
        #9 bossfight
        findTile = 'missingTile'
        if tile == 0:
            modifier = 0
            if extra != 'NONE':
                modifier = extra[0]
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceEnemyAir:
                entityLoot = self.getLoot(modifier, self.dataDict['balancing']['entetyLootDroppingChance'])
                enemyList = self.filterSpawning(list(self._enemies))
                if len(enemyList) != 0:
                    entity = {'type': self.randomEntity(enemyList), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
                else:
                    entity = 'NONE'
            if random.randint(1,100) <= self.chanceLootAir:
                loot = self.getLoot(modifier)

            if 'floor' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['floor'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': entity, 'loot': loot, 'text': 'NONE'} 
        elif tile == 1:
            if 'wall' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['wall'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': 'NONE', 'loot': 'NONE', 'text': 'NONE'} 
        elif tile == 2:
          if 'floor' in self.dataDict['defaultTiles']:
            findTile = random.choice(self.dataDict['defaultTiles']['floor'])
          else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
          self._currentLevel[x][y] = {'tile': findTile, 'entity': 'NONE', 'loot': 'NONE', 'text': 'NONE'} 
          self._playerX = x
          self._playerY = y
        elif tile == 3:
          if 'exit' in self.dataDict['defaultTiles']:
            findTile = random.choice(self.dataDict['defaultTiles']['exit'])
          else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
          self._currentLevel[x][y] = {'tile': findTile, 'entity': 'NONE', 'loot': 'NONE', 'text': 'NONE', 'exit': {'exit': True, 'nextLevelList': self.dataDict['dungeon']['defaultLevelList']}} 
        elif tile == 4:
            modifier = 0
            if extra != 'NONE':
                modifier = extra[0]
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceLootSpawn:
                loot = self.getLoot(modifier)
            if random.randint(1,100) <= self.chanceEnemyAir:
                entityLoot = self.getLoot(modifier, self.dataDict['balancing']['entetyLootDroppingChance'])
                enemyList = self.filterSpawning(list(self._enemies))
                if len(enemyList) != 0:
                    entity = {'type': self.randomEntity(enemyList), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
                else:
                    entity = 'NONE'
            if 'floor' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['floor'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': entity, 'loot': loot, 'text': 'NONE'}  
        elif tile == 5:
            modifier = 0
            if extra != 'NONE':
                modifier = extra[0]
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceLootAir:
                loot = self.getLoot(modifier)
            if random.randint(1,100) <= self.chanceEnemySpawn:
                entityLoot = self.getLoot(modifier, self.dataDict['balancing']['entetyLootDroppingChance'])
                enemyList = self.filterSpawning(list(self._enemies))
                if len(enemyList) != 0:
                    entity = {'type': self.randomEntity(enemyList), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
                else:
                    entity = 'NONE'
            if 'floor' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['floor'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': entity, 'loot': loot, 'text': 'NONE'} 
        elif tile == 6:
            if extra != 'NONE':
                text = extra[0]
            else:
                text = self.dataDict['text']['signText'][random.randint(0,len(self.dataDict['text']['signText'])-1)]
            if 'sign' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['sign'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': 'NONE', 'loot': 'NONE', 'text': text} 
        elif tile == 7:
            if extra != 'NONE':
                text = extra[0]
            else:
                text = self.dataDict['text']['npcText'][random.randint(0,len(self.dataDict['text']['npcText'])-1)]
            if 'npc' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['npc'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': 'NONE', 'loot': 'NONE', 'text': text} 
        elif tile == 8:
            if 'floor' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['floor'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': 'NONE', 'loot': 'NONE', 'text': 'NONE'}
        elif tile == 9:
            modifier1 = 0
            modifier2 = 10
            modifier3 = [1,4]
            if extra != 'NONE':
                if extra[0].lower() != 'none':
                    modifier1 = extra[0]
                if len(extra)> 1:
                    if extra[1].lower() != 'none':
                        modifier2 = extra[1]
                if len(extra)> 2:
                    modifier3 = extra[2]
                    if type(modifier3) != list:
                        modifier3 = [extra[2],extra[2]]
            entity = 'NONE'
            loot = self.getLoot(modifier1)
            entityLoot = self.getLoot(modifier2)
            enemyList = self.filterSpawning(list(self._enemies))
            if len(enemyList) != 0:
                entity = {'type': self.randomEntity(enemyList), 'level': random.randint(modifier3[0],modifier3[1])+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            else:
                entity = 'NONE'
            if 'floor' in self.dataDict['defaultTiles']:
              findTile = random.choice(self.dataDict['defaultTiles']['floor'])
            else:
              self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')
            self._currentLevel[x][y] = {'tile': findTile, 'entity': entity, 'loot': loot, 'text': 'NONE'}  
        elif type(tile) == dict:
            tileTile = 'NONE'
            tileEntity = 'NONE'
            tileLoot = 'NONE'
            tileText = 'NONE'
            tileLock = 'NONE'

            if 'tile' in tile and tile['tile'] != 'NONE':
                tileTile = tile['tile']
                if 'entity' in tile and tile['entity'] != 'NONE':
                    tileEntity = tile['entity']
                    if type(tileEntity) == dict and type(tileEntity['level']) == list:
                        if tileEntity['level'][0] == '+':
                            tileEntity['level'].pop(0)
                            for xxx in range(len(tileEntity['level'])):
                                tileEntity['level'][xxx] += (self._enemyLevel + self._dungeonLevel)
                        tileEntity['level'] = random.choice(tileEntity['level'])
                if 'loot' in tile and tile['loot'] != 'NONE':
                    tileLoot = tile['loot']
                if 'text' in tile and tile['text'] != 'NONE':
                    tileText = tile['text']
                if 'lock' in tile and tile['lock'] != 'NONE':
                    for item in list(tile['lock'].keys()):
                        if type(tile['lock'][item]) == list:
                            tile['lock'][item] = tile['lock'][item][random.randint(0,len(tile['lock'][item])-1)]
                    if 'item' in tile['lock'] and type(tile['lock']['item']) == dict and type(tile['lock']['item']['amount']) == list:
                        tile['lock']['item']['amount'] = tile['lock']['item']['amount'][random.randint(0,len(tile['lock']['item']['amount'])-1)]
                    tileLock = tile['lock']

                if type(tileLock) == dict and 'item' in tileLock and type(tileLock['item']) == str and tileLock['item'].lower() == "True".lower():
                  tileLock['item'] = self.getLoot()
                if type(tileEntity) == dict and type(tileEntity['item']) == str and tileEntity['item'].lower() == "True".lower():
                  tileEntity['item'] = self.getLoot()
                if type(tileLoot) == str and tileLoot.lower() == "True".lower():
                  tileLoot = self.getLoot()
                if type(tileEntity) == str and tileEntity.lower() == "True".lower():
                  entityLoot = self.getLoot(0)
                  tileEntity = {'type': random.choice(list(self._enemies)), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
                if 'exit' in tile and tile['exit'] != 'NONE':
                    self._currentLevel[x][y] = {'tile': tileTile, 'entity': tileEntity, 'loot': tileLoot, 'text': tileText, 'lock': tileLock, 'exit': tile['exit']}
                else:
                    self._currentLevel[x][y] = {'tile': tileTile, 'entity': tileEntity, 'loot': tileLoot, 'text': tileText, 'lock': tileLock}

        
        else:
            
            self.logging(f'Message: it didn\'t go through one of the elif\'s,', f'Tile: {tile}', 'Function = readTile()', f'Map: {levelNumber}', f'X: {x}, Y: {y}')
            showerror('error', 'Error code 0001')
            self.exit(False)
        if self._currentLevel[x][y]['tile'][0] == "|":
          if self._currentLevel[x][y]['tile'][1:] in self.dataDict['defaultTiles']:
            self._currentLevel[x][y]['tile'] = random.choice(self.dataDict['defaultTiles'][self._currentLevel[x][y]['tile'][1:]])
          else:
            self._currentLevel[x][y]['tile'] = 'missingTile'
            self.logging(f'error at tile {x}:{y}: tried to grab from defaultTiles but it doesn\'t exist')

        if self._currentLevel[x][y]['entity']!= 'NONE':
            #if there is an enemy, it should display enemy instead

            display = self._currentLevel[x][y]['entity']['type']
            
        elif self._currentLevel[x][y]['loot']!= 'NONE':
            #if there is loot, it should display loot instead
            display = self._currentLevel[x][y]['loot']['type']
        else:
            #else display the tile
            display = self._currentLevel[x][y]['tile']
        if 'display' not in self._currentLevel[x][y]:
            self._currentLevel[x][y]['display'] = display

    #create a level off a 2D erray
    def createLevel(self, levelDefault, levelNumber):
        self.logging(f'levelNumber: {levelNumber}', 'createLevel()')
        level = copy.deepcopy(levelDefault)
        searchForExit = True
        if level[0] == 'NONE':
            level.pop(0)
            searchForExit = False
        #if there isn't an entrance declared, generate random entrance
        if not any(2 in sublist for sublist in level):
            self.logging('entrance needed')
            while not any(2 in sublist for sublist in level) and (any(0 in sublist for sublist in level) or any(8 in sublist for sublist in level)):
                tryLine = random.randint(0,len(level)-1)
                if 0 in level[tryLine] or 8 in level[tryLine]:
                    whereAir = [i for i, x in enumerate(level[tryLine]) if x == 0]
                    whereNonAir = [i for i, x in enumerate(level[tryLine]) if x == 8]
                    spawnable = whereAir + whereNonAir
                    level[tryLine][spawnable[random.randint(0,len(spawnable)-1)]] = 2
        #if there isn't an exit declared, generate random exit
        if not any(3 in sublist for sublist in level) and searchForExit:
            self.logging('exit needed')
            while not any(3 in sublist for sublist in level) and (any(0 in sublist for sublist in level) or any(8 in sublist for sublist in level)):
                tryLine = random.randint(0,len(level)-1)
                if 0 in level[tryLine]or 8 in level[tryLine]:
                    whereAir = [i for i, x in enumerate(level[tryLine]) if x == 0]
                    whereNonAir = [i for i, x in enumerate(level[tryLine]) if x == 8]
                    spawnable = whereAir + whereNonAir
                    level[tryLine][spawnable[random.randint(0,len(spawnable)-1)]] = 3
        #make 2D erray
        self._currentLevel = []
        for x in range(len(level)):
            self._currentLevel.append([])
            for y in range(len(level[x])):
                self._currentLevel[x].append({})
                if type(level[x][y]) == list:
                    if level[x][y][0] == '?':
                        level[x][y] = level[x][y][random.randint(1,len(level[x][y])-1)]

                if type(level[x][y]) == list:
                    #read the tile(with extra argument, for given text to signs and npc)
                    extraData = []
                    for z in range(len(level[x][y])):
                        if z != 0:
                            extraData.append(level[x][y][z])
                    self.readTile(level[x][y][0], x, y, extraData, levelNumber)
                else:
                    #read the tile(with extra argument
                    self.readTile(level[x][y], x, y, 'NONE', levelNumber)
        self.levelSize = [len(self._currentLevel), len(self._currentLevel[0])]

    #render how the dungeon looks like
    def rendering(self):
        if self.mode == 'Play':
            self._canvas.delete("all")
            #make the furthest visability square (the transition)
            self._sightFurthest = [] 
            for ix in range(self._viewDistance * 2 + 1):
                for iy in range(self._viewDistance * 2 + 1):
                    #add it to a list, so it remembers to shade it later
                    #the math to calculate how far sight is
                    self._sightFurthest.append(f'{ix + self._playerX - self._viewDistance}-{iy + self._playerY - self._viewDistance}')
            #make the normal visability square
            self._sight = [] 
            for ix in range(self._viewDistance * 2 +1 - (math.ceil(self._viewDistance/2)*2)):
                for iy in range(self._viewDistance * 2 + 1 - (math.ceil(self._viewDistance/2)*2)):
                    #add it to a list, so it remembers to keep original texture
                    #the math to calculate how far sight is
                    self._sight.append(f'{ix + self._playerX - self._viewDistance+math.ceil(self._viewDistance/2)}-{iy + self._playerY - self._viewDistance+math.ceil(self._viewDistance/2)}')
            
            #for all tiles, display them
            for x in range(len(self._currentLevel)):
                for y in range(len(self._currentLevel[x])):
                    if f"{x}-{y}" in self._sightFurthest:
                        #lookup what type of shading it needs
                        if f"{x}-{y}" in self._sight:
                            picType = 'normal-'
                        else:
                            picType = 'darknessFade-'
                    else:
                        picType = 'darknessFull-'
                    
                    #display the tile
                    if x==self._playerX and y == self._playerY:
                        self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['playerImages'][self._facingDirectionTexture.upper()]}"])
                    else:
                        try:
                            if picType == 'darknessFull-':
                                self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['tiles'][self._currentLevel[x][y]['display']]['ShowOutsideAs']}"])
                            else:
                                self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['tiles'][self._currentLevel[x][y]['display']]['Image']}"])
                        except Exception as e:
                            self.logging(f'error: {e}, error 0004, image json not difined/found')
                            showerror('error', 'Error code 0004')
                            self.exit(False)
            #for if stats changed, update those
            self.updateStats()
            #updae the window, so that it shows the new generated canvas
            self.gameWindow.update_idletasks()      
            self.gameWindow.update()

    #create the window
    def createCanvas(self):
        self.logging('createCanvas()')
        self._canvas = tkinter.Canvas(self.gameWindow, bg="black", height=len(self._currentLevel[0])*32, width=len(self._currentLevel)*32)
        self._canvas.grid(row=0,column=0)
        
    #for the stats like hp    
    def createStats(self):
        self.logging('createStats()')
        self._hpTextvar = tkinter.StringVar()
        self._hpTextvar.set(f'HP:')
        self._xpVar = tkinter.StringVar()
        self._xpVar.set(f'XP:')
        self._strengthVar = tkinter.StringVar()
        self._strengthVar.set(f'Floor:')
        self._levelVar = tkinter.StringVar()
        self._levelVar.set(f'Level:')
        self._floorVar = tkinter.StringVar()
        self._floorVar.set(f'Strength:')
        self._hpLabel = ttk.Label(self.gameWindow, textvariable=self._hpTextvar)
        self._hpLabel.grid(row=1,column=0, sticky="EW")
        self._strengthLabel = ttk.Label(self.gameWindow, textvariable=self._strengthVar)
        self._strengthLabel.grid(row=2,column=0, sticky="EW")
        self._xpLabel = ttk.Label(self.gameWindow, textvariable=self._xpVar)
        self._xpLabel.grid(row=3,column=0, sticky="EW")
        self._levelLabel = ttk.Label(self.gameWindow, textvariable=self._levelVar)
        self._levelLabel.grid(row=4,column=0, sticky="EW")
        self._floorLabel = ttk.Label(self.gameWindow, textvariable=self._floorVar)
        self._floorLabel.grid(row=5,column=0, sticky="EW")

    def updateStats(self):
        if self.playerStats["HP"]["current"] <= 0:
            showerror(title='Error',message=f'You died at floor {self._dungeonLevel + 1}!\nYou travelled {self._dungeonLevel - self._startingFloor} floors!')
            self.logging(f'U died, playerstats: {self.playerStats}, invetory: {self.inventory}, floor: {self._dungeonLevel + 1}')
            self.exit()
        while True:
            xpNeeded = self.defaultPlayerStats["XPneeded"]["multiplyByLevel"] * self.playerStats['level'] + self.defaultPlayerStats["XPneeded"]["startingNumber"]
            if self.playerStats['XP'] > xpNeeded:
                self.playerStats['XP'] -= xpNeeded
                self.playerStats['level'] += 1
                self.displayText(f'You levelled up to level {self.playerStats["level"]}!')
                self.playerStats["strength"] += self.defaultPlayerStats['statsPerLevel']['strength']
                self.playerStats["HP"]["current"] += self.defaultPlayerStats['statsPerLevel']['HP']
                self.playerStats["HP"]["max"] += self.defaultPlayerStats['statsPerLevel']['HP']
            else:
                break
        self._xpVar.set(f'XP: {self.playerStats["XP"]} / {xpNeeded}')
        self._hpTextvar.set(f'HP: {self.playerStats["HP"]["current"]} / {self.playerStats["HP"]["max"]}')
        self._levelVar.set(f'Level: {self.playerStats["level"]}')
        self._strengthVar.set(f'Strength: {self.playerStats["strength"]}')
        self._floorVar.set(f'Floor: {self._dungeonLevel + 1}')

    def rotate2Derray(self, erray, buttonList, turns = 1):
      self.rotate2DerrayButton.grid_remove()
      self.exportMapButton.grid_remove()
      self.printButton.grid_remove()

      for x in range(len(self.loadedLevel)):
        for y in range(len(self.loadedLevel[x])):
            self._buttonsList[x][y].destroy()
      for x in range(len(self.loadedLevel)):
        for y in range(len(self.loadedLevel[x])):
          self._buttonsList[x].pop(0)
            
      for turn in range(turns):
        newErray = []
        for x in range(len(erray[0])):
          newErray.append([])
        for x in range(len(erray)):
          for y in range(len(erray[len(erray) - (x + 1)])):
            newErray[y].append(erray[len(erray) - (x + 1)][y])
        self.loadedLevel = list(newErray)

      for x in range(len(self.loadedLevel)):
        for y in range(len(self.loadedLevel[x])):
            cords = [x,y]
            if type(self.loadedLevel[x][y]) != int:
                self._buttonsList[x].append(tkinter.Button(self.gameWindow, text=self.dataDict['appSettings']['unknown']['text'],bg = self.dataDict['appSettings']['unknown']['color'], command=lambda cords=cords:print(self.loadedLevel[cords[0]][cords[1]])))
            else:
                self._buttonsList[x].append(tkinter.Button(self.gameWindow, text=self.loadedLevel[x][y],bg = self.colors[self.loadedLevel[x][y]], command=lambda cords=cords:self.changeEditorButton(cords)))
            self._buttonsList[x][y].grid(column=x, row=y, ipadx=10, ipady=5, sticky="EW")
      
      if x//3 > 0:
        self.rotate2DerrayButton.grid(column=x//3*2+1,row=y+1,columnspan=x//3+1, ipadx=10, ipady=5, sticky="EW")
        self.exportMapButton.grid(column=x//3+1,row=y+1,columnspan=x//3, ipadx=10, ipady=5, sticky="EW")
        self.printButton.grid(column=0,row=y+1,columnspan=x//3+1, ipadx=10, ipady=5, sticky="EW")
      else:
        self.rotate2DerrayButton.grid(column=2,row=y+1,columnspan=1, ipady=5, sticky="EW")
        self.exportMapButton.grid(column=1,row=y+1,columnspan=1, ipady=5, sticky="EW")
        self.printButton.grid(column=0,row=y+1,columnspan=1, ipady=5, sticky="EW")

    #startup the program
    def startGame(self, mode = 'Play', chosenLevel = None):
        self.logging(f'startGame({mode}, {chosenLevel})')
        def exportMap(map):
            if askyesno('export', 'are you sure you want to export? \nIf you don\'t know how to edit it might be hard to remove'):
                if os.path.exists(f'gameData/levelData.json'):
                    with open(f'gameData/levelData.json') as level_json_file:
                        levelDataString = json.load(level_json_file)
                        if type(levelDataString) != dict and type(levelDataString) != list:
                            levelDataDict = json.loads(levelDataString)
                        else:
                            levelDataDict = levelDataString

                    levelDataDict[self.dataDict['dungeon']['defaultLevelList']].append(map)
            
                    with open(f'gameData/levelData.json', 'w') as outfile:
                        json.dump(levelDataDict, outfile)
                    showinfo('export', 'exported succesfully!')
        
        custom = False
        #look what mode
        if str(mode).lower() not in ['play', 'create']:
            chosenLevel = mode
            mode = 'Play'
        #look for given level
        if type(chosenLevel) == list:
          if self.dataDict['dungeon']['defaultLevelList'] in self._defaultlevels and len(self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']]) > 0:
            self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']][0] = list(chosenLevel)
            chosenLevel = 0
            custom = True
          else:
            self.logging('the "defaultLevelList" set in the gameData.json doesn\'t exist in the levelData.json')
            showerror('error',f'the "defaultLevelList" set in the gameData.json doesn\'t exist in the levelData.json')
            self.exit(False)
            
        #look for 10x10 format to generate that size level
        if type(chosenLevel) == str:
            if '//' in str(chosenLevel):
                splitting = '//'
            elif 'x' in str(chosenLevel):
                splitting = 'x'
            
            #split it at the x, so it can read the margins
            if chosenLevel.split(splitting)[0].isdigit() and chosenLevel.split(splitting)[1].isdigit():
                level = []
                #generate the 2D erray of the level
                for x in range(int(chosenLevel.split(splitting)[0])):
                    level.append([])
                    for y in range(int(chosenLevel.split(splitting)[1])):
                        if len(chosenLevel.split(splitting)) > 2:
                            if chosenLevel.split(splitting)[2].isdigit():
                                level[x].append(int(chosenLevel.split(splitting)[2]))
                            elif chosenLevel.split(splitting)[2][0] == '[' or chosenLevel.split(splitting)[2][0] == '{':
                                print(chosenLevel.split(splitting)[2])
                                try:
                                    level[x].append(json.loads(chosenLevel.split(splitting)[2]))
                                except Exception as e:
                                    self.logging(f'error: {e}, error 0003, tries to read: {chosenLevel.split(splitting)}, splitter: {splitting}')
                                    showerror('error', 'Error code 0003')
                                    self.exit(False)
                            else:
                                level[x].append(0)
                        else:
                            level[x].append(0)
                #make level 0 the given level
                self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']][0] = level
                #force it to play level 0
                chosenLevel = 0
                custom = True
        #if not given a number, it will force to play 0
        if not str(chosenLevel).isdigit():
          chosenLevel = 0
        else:
            custom = True
        if self.dataDict['dungeon']['defaultLevelList'] in self._defaultlevels and len(self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']]) > 0:
          self.loadedLevel = list(self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']][chosenLevel])
        else:
          self.logging('the "defaultLevelList" set in the gameData.json doesn\'t exist in the levelData.json')
          showerror('error',f'the "defaultLevelList" set in the gameData.json doesn\'t exist in the levelData.json')
          self.exit(False)
        
        if mode.lower() == 'create':
            self.mode = 'Create'
            #if using level editor  
            self._buttonsList = []
            #make 2D erray
            for x in range(len(self.loadedLevel)):
                self._buttonsList.append([])
            #create a lot of buttons
            for x in range(len(self.loadedLevel)):
                for y in range(len(self.loadedLevel[x])):
                    cords = [x,y]
                    if type(self.loadedLevel[x][y]) != int:
                        self._buttonsList[x].append(tkinter.Button(self.gameWindow, text=self.dataDict['appSettings']['unknown']['text'],bg = self.dataDict['appSettings']['unknown']['color'], command=lambda cords=cords:print(self.loadedLevel[cords[0]][cords[1]])))
                    else:
                        self._buttonsList[x].append(tkinter.Button(self.gameWindow, text=self.loadedLevel[x][y],bg = self.colors[self.loadedLevel[x][y]], command=lambda cords=cords:self.changeEditorButton(cords, chosenLevel)))
                    self._buttonsList[x][y].grid(column=x, row=y, ipadx=10, ipady=5, sticky="EW")
            self.printButton = tkinter.Button(self.gameWindow, text='export to console',command=lambda: print(self.loadedLevel))
            self.exportMapButton = tkinter.Button(self.gameWindow, text='export to json',command=lambda: exportMap(self.loadedLevel))
            self.rotate2DerrayButton = tkinter.Button(self.gameWindow, text='rotate 90 degrees',command=lambda: self.rotate2Derray(self.loadedLevel, self._buttonsList, 1))
            if x//3 > 0:
              self.rotate2DerrayButton.grid(column=x//3*2+1,row=y+1,columnspan=x//3+1, ipadx=10, ipady=5, sticky="EW")
              self.exportMapButton.grid(column=x//3+1,row=y+1,columnspan=x//3, ipadx=10, ipady=5, sticky="EW")
              self.printButton.grid(column=0,row=y+1,columnspan=x//3+1, ipadx=10, ipady=5, sticky="EW")
            else:
              self.rotate2DerrayButton.grid(column=2,row=y+1,columnspan=1, ipady=5, sticky="EW")
              self.exportMapButton.grid(column=1,row=y+1,columnspan=1, ipady=5, sticky="EW")
              self.printButton.grid(column=0,row=y+1,columnspan=1, ipady=5, sticky="EW")

        
        
        #if play mode
        if mode.lower() == 'play':
            self.mode = 'Play'
            #generate player
            hp = (self.defaultPlayerStats["statsPerLevel"]["HP"] * self.defaultPlayerStats["startLevel"]) + self.defaultPlayerStats["beginStats"]["HP"]
            strength = (self.defaultPlayerStats["statsPerLevel"]["strength"] * self.defaultPlayerStats["startLevel"]) + self.defaultPlayerStats["beginStats"]["strength"]
            self.playerStats = {'HP': {'max': hp, 'current': hp}, 'level' : self.defaultPlayerStats["startLevel"], 'XP': 0, 'strength': strength}



            #generate starting level
            self.checkStates()
            if custom == False:
              if self.dataDict['dungeon']['defaultLevelList'] in self._defaultlevels and len(self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']]) > 0:
                levelNumber = random.randint(0,len(self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']])-1)
              else:
                self.logging('the "defaultLevelList" set in the gameData.json doesn\'t exist in the levelData.json')
                showerror('error',f'the "defaultLevelList" set in the gameData.json doesn\'t exist in the levelData.json')
                self.exit(False)
            else:
              levelNumber = chosenLevel
            print(levelNumber)
            self.createLevel(self._defaultlevels[self.dataDict['dungeon']['defaultLevelList']][levelNumber], levelNumber)
            self.createStats()
            self.createCanvas()
            self.rendering()
        

    def exit(self, remove = True, dontExit = False):
        self.logging('exit( )')
        accounts_omac.saveAccount(self.accountDataDict, self.accountConfigSettings)
        if not self.doLogging and remove and os.path.exists(f'logs/logFiles/log{self.dt_string}.txt'):
            os.remove(f'logs/logFiles/log{self.dt_string}.txt')
        if not self.doReplayMode and remove and os.path.exists(f'logs/replayFiles/replay{self.dt_string}.txt'):
            os.remove(f'logs/replayFiles/replay{self.dt_string}.txt')
        if not dontExit:
          exit()


    def onGrid(self, cords):
        x,y = cords
        if x < 0 or y < 0 or y > self.levelSize[1]-1 or x > self.levelSize[0]-1:
            return False
        else:
            return True

    #check if tile is being able to be walked
    def isWalkable(self, cordinates = [0,0], human = False):
        x,y = cordinates
        if self.onGrid(cordinates):
            if x == self._playerX and y == self._playerY:
                return False
            if not human:
                if 'exit' in self._currentLevel[x][y] and self._currentLevel[x][y]['exit']['exit'] or self._currentLevel[x][y]['tile'] == 'exit':
                    return False
            if human and 'lock' in self._currentLevel[cordinates[0]][cordinates[1]] and self._currentLevel[cordinates[0]][cordinates[1]]['lock'] != 'NONE':
                self.displayText('The tile is locked, Interact with it')
                return False
            return self.dataDict['tiles'][self._currentLevel[x][y]['display']]['Walkable']
        else:
            return False

    #calculate distance between 2 cordinates
    def distence(self, cord1, cord2):
        #a^2 + b^2 == c^2
        x1,y1 =cord1
        x2,y2 =cord2
        xDis = abs(x1-x2)
        yDis = abs(y1-y2)
        distance = math.sqrt((xDis **2) + (yDis **2))
        return distance

    def delaySleep(self):
        #delay of enemy movement
        try:
            if self.dataDict['debug']['sleep']:
                time.sleep(self.dataDict['preference']['sleepTime'])
        except Exception as e:
            self.jsonError(e)
        self.rendering()


    #check if enemy's want to move
    def enemyTurn(self, reset = False):
        def attack():
            if self.doCombat:
                ATK = self._currentLevel[tile[0]][tile[1]]['entity']['level'] * self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]["enemy"]['statsPerLevel']['ATK']
                if self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]["enemy"]['hitChance'] > random.randint(1,99):
                    ATK -= ATK // 100 * random.randint(0, self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]["enemy"]['lessATKpointsPercentage'])
                    self.playerStats["HP"]["current"] -= ATK
                    self.displayText(f"{self._currentLevel[tile[0]][tile[1]]['entity']['type']} hit you, You took {ATK}HP damage, you have {self.playerStats['HP']['current']} HP left.")
                self.delaySleep()


        self.logging('enemyTurn')
        if self.doEnemyMovement != False:
            self.EnemyMoveRadius = [] 
            for ix in range((self._viewDistance+1) * 2 + 1):
                for iy in range((self._viewDistance+1) * 2 + 1):
                    if self.onGrid([ix,iy]):
                        self.EnemyMoveRadius.append([ix + self._playerX - self._viewDistance,iy + self._playerY - self._viewDistance])
            if reset:
                for tile in self.EnemyMoveRadius:
                    if self.onGrid(tile):
                        if self._currentLevel[tile[0]][tile[1]]['entity'] != 'NONE':
                            if 'movement' not in self._currentLevel[tile[0]][tile[1]]['entity']:
                                max = self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]['enemy']['movementRules']
                                if isinstance(max["movement"], float):
                                    if random.random() < max["movement"] % 1:
                                        max["movement"] = math.floor(max["movement"]+1)
                                    else:
                                        max["movement"] = math.floor(max["movement"])
                                if isinstance(max["attack"], float):
                                    if random.random() < max["attack"] % 1:
                                        max["attack"] = math.floor(max["attack"]+1)
                                    else:
                                        max["attack"] = math.floor(max["attack"])
                                self._currentLevel[tile[0]][tile[1]]['entity']['movement'] = {'done':{'movement':0,'attack':0}, 'max': max}
                            else:
                                self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['movement'] = 0
                                self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack'] = 0
            for _ in range(self.dataDict['debug']['enemyLoopPerEnemy']):
                for tile in self.EnemyMoveRadius:
                    if self.onGrid(tile):
                        if self._currentLevel[tile[0]][tile[1]]['entity'] != 'NONE':
                            if tile[0] < 0 or tile[1] < 0 or tile[0] > len(self._currentLevel)-1 or tile[1] > len(self._currentLevel[tile[0]])-1:
                                pass
                            elif self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['movement'] >= self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['movement'] and self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack'] >= self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['attack']:
                                pass
                            else:
                                moves = ['Up', 'Down', 'Left', 'Right']
                                bestMoves = {}
                                distances = []
                                for move in moves:
                                    match move:
                                        case 'Up':
                                            cords = [tile[0], tile[1]-1]
                                        case 'Down':
                                            cords = [tile[0], tile[1]+1]
                                        case 'Left':
                                            cords = [tile[0]-1, tile[1]]
                                        case 'Right':
                                            cords = [tile[0]+1, tile[1]]
                                    if not self.isWalkable(cords):
                                        pass
                                    else:
                                        if self.distence(cords, [self._playerX, self._playerY]) > self.distence([tile[0], tile[1]], [self._playerX, self._playerY]):
                                            if bool(random.getrandbits(1)):
                                                moveTheEnemy = True
                                            else:
                                                moveTheEnemy = False
                                        else:
                                            moveTheEnemy = True
                                        if moveTheEnemy:
                                            if self.distence(cords, [self._playerX, self._playerY]) in bestMoves:
                                                bestMoves[self.distence(cords, [self._playerX, self._playerY])].append([move, cords, [tile[0], tile[1]]])
                                            else:
                                                bestMoves[self.distence(cords, [self._playerX, self._playerY])] = [[move, cords, [tile[0], tile[1]]]]
                                                distances.append(self.distence(cords, [self._playerX, self._playerY]))

                                #start picking a move
                                if len(bestMoves) != 0:
                                    distances.sort()
                                    if self.distence([tile[0], tile[1]], [self._playerX, self._playerY]) > 1.0:
                                        if not self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['movement'] >= self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['movement']:
                                            self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['movement'] += 1
                                            if self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['attackRule'] == 'insteadOf':
                                                self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack'] += 1
                                            if len(bestMoves[distances[0]]) > 1:
                                                self.moveEnemy(bestMoves[distances[0]][random.randint(0,len(bestMoves[distances[0]])-1)])
                                            else:
                                                self.moveEnemy(bestMoves[distances[0]][0])

                                    else:
                                        if not self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack'] >= self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['attack']:
                                            for attackTimes in range(self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['attack']-self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack']):
                                                
                                                if self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['attackRule'] == 'insteadOf' and not self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['movement'] >= self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['movement']:
                                                    self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack'] += 1
                                                    self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['movement'] += 1
                                                    attack()
                                                elif self._currentLevel[tile[0]][tile[1]]['entity']['movement']['max']['attackRule'] == 'and':
                                                    self._currentLevel[tile[0]][tile[1]]['entity']['movement']['done']['attack'] += 1
                                                    attack()

             
    def moveEnemy(self, moveData):
        move, NewXY, XY = moveData
        newX,newY = NewXY
        x,y = XY

        types = ['display', 'entity']
        for each in types:
            switch = []
            switch.append(self._currentLevel[x][y][each])
            switch.append(self._currentLevel[newX][newY][each])
            self._currentLevel[x][y][each] = switch[1]
            self._currentLevel[newX][newY][each] = switch[0]
        self.delaySleep()
        if self._currentLevel[x][y]['loot'] != 'NONE':
          self._currentLevel[x][y]['display'] = self._currentLevel[x][y]['loot']['type']


    def damageMessage(self, cords, damage):
        if self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] > 0:
            self.displayText(f"You dealt {damage}HP damage to {self._currentLevel[cords[0]][cords[1]]['entity']['type']}, he has {self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current']}HP left")
            self.playerStats['XP'] += damage // self.dataDict['balancing']['XPperDamageDevidedBy']
        else:
            self.displayText(f"You dealt {damage}HP damage to {self._currentLevel[cords[0]][cords[1]]['entity']['type']}, he is ded")
            self.playerStats['XP'] += damage * self.dataDict['balancing']['killMultiplierXP'] // self.dataDict['balancing']['XPperDamageDevidedBy']
            self.playerStats['XP'] += self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['entity']['type']]["enemy"]['statsPerLevel']['deathXP'] * self._currentLevel[cords[0]][cords[1]]['entity']['level']

    def sliceEnemy(self, cords, damage):
        try:
            if self._currentLevel[cords[0]][cords[1]]['entity'] != 'NONE':
                if 'HP' not in self._currentLevel[cords[0]][cords[1]]['entity']:
                    hp = self._currentLevel[cords[0]][cords[1]]['entity']['level'] * self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['entity']['type']]["enemy"]['statsPerLevel']['HP']
                    self._currentLevel[cords[0]][cords[1]]['entity']['HP'] = {'Max': hp, 'current': hp + random.randint(-1,1)}
                self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] -= damage
                self.damageMessage(cords, damage)
        except IndexError:
            pass
        except Exception as e:
            self.logging(e, f'cords: {cords}', f'damage: {damage}', 'Function = sliceEnemy()')
            
    def lockedTile(self, cords):
        self.logging(self._currentLevel[cords[0]][cords[1]], cords)
        try:
          if 'HP' in self._currentLevel[cords[0]][cords[1]]['lock'] and self.playerStats["HP"]["current"] < self._currentLevel[cords[0]][cords[1]]['lock']['HP']:
              self.displayText(f"It's locked, Not enough HP, {self._currentLevel[cords[0]][cords[1]]['lock']['HP']} HP needed to unlock this lock")
          elif 'Strength' in self._currentLevel[cords[0]][cords[1]]['lock'] and self.playerStats["strength"] < self._currentLevel[cords[0]][cords[1]]['lock']['Strength']:
              self.displayText(f"It's locked, Not enough Strength, {self._currentLevel[cords[0]][cords[1]]['lock']['Strength']} Strength needed to unlock this lock")
          elif 'level' in self._currentLevel[cords[0]][cords[1]]['lock'] and self.playerStats["level"] < self._currentLevel[cords[0]][cords[1]]['lock']['level']:
              self.displayText(f"It's locked, Not high enough Level, Level {self._currentLevel[cords[0]][cords[1]]['lock']['Level']} needed to unlock this lock")
          elif 'Level' in self._currentLevel[cords[0]][cords[1]]['lock'] and self.playerStats["level"] < self._currentLevel[cords[0]][cords[1]]['lock']['Level']:
              self.displayText(f"It's locked, Not high enough Level, Level {self._currentLevel[cords[0]][cords[1]]['lock']['Level']} needed to unlock this lock")
          elif 'item' in self._currentLevel[cords[0]][cords[1]]['lock'] and self._currentLevel[cords[0]][cords[1]]['lock']['item']['type'] != 'NONE' and self._currentLevel[cords[0]][cords[1]]['lock']['item']['type'] in self.inventory and self.inventory[self._currentLevel[cords[0]][cords[1]]['lock']['item']['type']]['amount'] < self._currentLevel[cords[0]][cords[1]]['lock']['item']['amount']:
              self.displayText(f"It's locked, You don't have {self._currentLevel[cords[0]][cords[1]]['lock']['item']['amount']} x '{self._currentLevel[cords[0]][cords[1]]['lock']['item']['type']}'")
          elif 'item' in self._currentLevel[cords[0]][cords[1]]['lock'] and self._currentLevel[cords[0]][cords[1]]['lock']['item']['type'] not in self.inventory:
              self.displayText(f"It's locked, You don't have {self._currentLevel[cords[0]][cords[1]]['lock']['item']['amount']} x '{self._currentLevel[cords[0]][cords[1]]['lock']['item']['type']}'")
          else:
              if 'item' in self._currentLevel[cords[0]][cords[1]]['lock'] and self._currentLevel[cords[0]][cords[1]]['lock']['item']['type'] != 'NONE':
                  if self._currentLevel[cords[0]][cords[1]]['lock']['item']['type'] == self.equippedWeapon and self.inventory[self._currentLevel[cords[0]][cords[1]]['lock']['item']['type']]['amount'] == self._currentLevel[cords[0]][cords[1]]['lock']['item']['amount']:
                      self.displayText(f"You have item: '{self.equippedWeapon}' equipped as weapon, to use it you need to unequip it first")
                  else:
                      self.inventory[self._currentLevel[cords[0]][cords[1]]['lock']['item']['type']]['amount'] -= self._currentLevel[cords[0]][cords[1]]['lock']['item']['amount']
                      self.displayText(f"The lock has been unlocked")
                      self._currentLevel[cords[0]][cords[1]]['lock'] = 'NONE'
                      self.interact()
              elif 'level' in self._currentLevel[cords[0]][cords[1]]['lock'] or 'Level' in self._currentLevel[cords[0]][cords[1]]['lock'] or 'Strength' in self._currentLevel[cords[0]][cords[1]]['lock'] or 'HP' in self._currentLevel[cords[0]][cords[1]]['lock']:
                  self.displayText(f"The lock has been unlocked")
                  self._currentLevel[cords[0]][cords[1]]['lock'] = 'NONE'
                  self.interact()
        except Exception as e:
          self.logging(e)
          self.exit(False)


    #interact with something
    def interact(self) -> None:
        self.replayWrite('interact')
        self.logging('interact()')
        
        def pickupLoot():
            if self._currentLevel[cords[0]][cords[1]]['loot'] != 'NONE':
                self.displayText(f"You picked up {self._currentLevel[cords[0]][cords[1]]['loot']['amount']} X {self._currentLevel[cords[0]][cords[1]]['loot']['type']}")
                if self._currentLevel[cords[0]][cords[1]]['loot']['type'] in self.inventory:

                    self.inventory[self._currentLevel[cords[0]][cords[1]]['loot']['type']]['amount'] += self._currentLevel[cords[0]][cords[1]]['loot']['amount']
                else:
                    self.inventory[self._currentLevel[cords[0]][cords[1]]['loot']['type']] = {'amount':self._currentLevel[cords[0]][cords[1]]['loot']['amount']}
                    
                if self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['loot']['type']]["loot"]['isWeapon'] == True:
                    if self.autoEquip == True and self.hasWeaponWeight < self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['loot']['type']]["loot"]['weapon']['weaponWeight'] and self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['loot']['type']]["loot"]['weapon']['minStrength'] <= self.playerStats['strength']:
                        self.equippedWeapon = self._currentLevel[cords[0]][cords[1]]['loot']['type']
                        self.hasWeaponWeight = self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['weaponWeight']
                        self.displayText(f"You equipped {self._currentLevel[cords[0]][cords[1]]['loot']['type']}")
                
                self._currentLevel[cords[0]][cords[1]]['loot']= 'NONE'
                self._currentLevel[cords[0]][cords[1]]['display']= 'floor'
                self.rendering()

        match self._facing:
            case 'U':
                cords = [self._playerX, self._playerY-1]
            case 'D':
                cords = [self._playerX, self._playerY+1]
            case 'L':
                cords = [self._playerX -1, self._playerY]
            case 'R':
                cords = [self._playerX +1, self._playerY]
        
        if self.onGrid(cords):

            if 'lock' in self._currentLevel[cords[0]][cords[1]] and self._currentLevel[cords[0]][cords[1]]['lock'] != 'NONE':
                self.lockedTile(cords)
            else:
                if 'transform' in self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['tile']]:
                    self._currentLevel[cords[0]][cords[1]]['display'] = self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['tile']]['transform']['TransformInto']
                    print(self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['tile']])
                    print(self._currentLevel[cords[0]][cords[1]]['tile'])
                    self._currentLevel[cords[0]][cords[1]]['tile'] = self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['tile']]['transform']['TransformInto']
                    self.rendering()
                if self._currentLevel[cords[0]][cords[1]]['text'] != 'NONE':
                    if type(self._currentLevel[cords[0]][cords[1]]['text']) == list:
                        self._currentLevel[cords[0]][cords[1]]['text'] = self._currentLevel[cords[0]][cords[1]]['text'][random.randint(0,len(self._currentLevel[cords[0]][cords[1]]['text']) -1)]
                    self.displayText(f"{self._currentLevel[cords[0]][cords[1]]['display']}: {self._currentLevel[cords[0]][cords[1]]['text']}")
                    if self._currentLevel[cords[0]][cords[1]]['entity'] != 'NONE' or self._currentLevel[cords[0]][cords[1]]['loot'] != 'NONE':
                        self._currentLevel[cords[0]][cords[1]]['text'] = 'NONE'

                if self._currentLevel[cords[0]][cords[1]]['entity'] != 'NONE':
                    if 'HP' not in self._currentLevel[cords[0]][cords[1]]['entity']:
                        hp = self._currentLevel[cords[0]][cords[1]]['entity']['level'] * self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['entity']['type']]["enemy"]['statsPerLevel']['HP']
                        self._currentLevel[cords[0]][cords[1]]['entity']['HP'] = {'Max': hp, 'current': hp + random.randint(-1,1)}
                    
                    damage = self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['attack']
                    if self.dataDict['balancing']['doStrengthDamage']:
                        damage += self.playerStats['strength'] // self.dataDict['balancing']['strengthDevidedBy']
                    if self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['minStrength'] > self.playerStats['strength']:
                        damage = random.randint(1,damage)
                    if self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['type'] == 'stab':
                        if self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['minStrength'] <= self.playerStats['strength'] or bool(random.getrandbits(1)):
                            self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] -= damage
                            self.damageMessage(cords, damage)
                        else:
                            self.displayText(f"You missed, The strength you need to use this weapon is {self.dataDict['tiles'][self.equippedWeapon]['loot']['weapon']['minStrength']}")
                    elif self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['type'] == 'slice':
                        if self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['minStrength'] <= self.playerStats['strength'] or bool(random.getrandbits(1)):
                            self.sliceEnemy([self._playerX, self._playerY-1],damage)
                            self.sliceEnemy([self._playerX, self._playerY+1],damage)
                            self.sliceEnemy([self._playerX-1, self._playerY],damage)
                            self.sliceEnemy([self._playerX+1, self._playerY],damage)
                        else:
                            self.displayText(f"You missed, The strength you need to use this weapon is {self.dataDict['tiles'][self.equippedWeapon]['loot']['weapon']['minStrength']}")

                    if self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] <= 0:
                        if self._currentLevel[cords[0]][cords[1]]['entity']['item'] != 'NONE':
                            pickupLoot()
                            self._currentLevel[cords[0]][cords[1]]['loot']= {'type' : self._currentLevel[cords[0]][cords[1]]['entity']['item']['type'], 'amount': self._currentLevel[cords[0]][cords[1]]['entity']['item']['amount']}
                            self._currentLevel[cords[0]][cords[1]]['display'] = self._currentLevel[cords[0]][cords[1]]['loot']['type']
                        else:
                            self._currentLevel[cords[0]][cords[1]]['display']= 'floor'
                        self._currentLevel[cords[0]][cords[1]]['entity']= 'NONE'
                        self._currentLevel[cords[0]][cords[1]]['text'] = 'NONE'
                    self.enemyFullTurn()
                    self.rendering()

                elif self._currentLevel[cords[0]][cords[1]]['loot'] != 'NONE':
                    pickupLoot()
            

    def merge(self, item) -> bool:  
        self.replayWrite(f'merge "{item}"')
        if item in self.dataDict['tiles'] and 'loot' in self.dataDict['tiles'][item] and 'mergable' in self.dataDict['tiles'][item]['loot']:
            if self.inInventory(item):
                if item == self.equippedWeapon and self.inventory[item]['amount'] <= self.dataDict['tiles'][item]['loot']['mergable']['mergeAmount']:
                    self.displayText(f"You have item: '{item}' equipped as weapon, to merge it you need to unequip it first")
                    return False 
                if self.inventory[item]['amount'] < self.dataDict['tiles'][item]['loot']['mergable']['mergeAmount']:
                    self.displayText(f"You need {self.dataDict['tiles'][item]['loot']['mergable']['mergeAmount']} of item: '{item}' to merge it")
                    return False
                else:
                    self.inventory[item]['amount'] -= self.dataDict['tiles'][item]['loot']['mergable']['mergeAmount']
                    self.displayText(f"You merged '{item}'")
                    for item2 in list(self.dataDict['tiles'][item]['loot']['mergable']['mergeIntoAndAmount'].keys()):
                        self.displayText(f"into {self.dataDict['tiles'][item]['loot']['mergable']['mergeIntoAndAmount'][item2]} x '{item2}'")
                        if item2 in self.inventory:
                            self.inventory[item2]['amount'] += self.dataDict['tiles'][item]['loot']['mergable']['mergeIntoAndAmount'][item2]
                        else:
                            self.inventory[item2] = {'amount':self.dataDict['tiles'][item]['loot']['mergable']['mergeIntoAndAmount'][item2]}

                    return True
            else:
                self.displayText(f"You don't have item: '{item}'")
                return False
        else:
            self.displayText(f"You can't merge item: '{item}'")
            return False

        


    #checks if move is possible, and then moves
    def movePlayer(self, direction = 'Up'):
        #return
        self.logging(f'movePlayer({direction})')
        match direction:
            case 'w':
                self.moveUp()
            case 's':
                self.moveDown()
            case 'a':
                self.moveLeft()
            case 'd':
                self.moveRight()
            case 'wait':
                self.wait()
            case ' ':
                self.wait()
            case 'e':
                self.interact()
            case 'item':
                self.useItem(input('item>>'))
            case 'inv':
                self.showInventory()
            case 'weapon':
                self.equipWeapon(input('weapon>>'))
            case 'info':
                self.itemInfo(input('item>>'))
            case 'merge':
                self.merge(input('item>>'))
            case 'repeat':
                try:
                    amount = int(input('amount>>'))
                    move = input('command to repeat>>')
                    for i in range(amount):
                        self.movePlayer(move)
                except:
                    self.displayText('Invalid amount')
            case 'nf':
                if 'allowDebugTeleport' in self.dataDict['debug'] and self.dataDict['debug']['allowDebugTeleport']:
                    self.newLevel(self.dataDict['dungeon']['defaultLevelList'])


    def lookUp(self):
        self._facing = 'U'
        self.replayWrite('lookUp')

    def lookDown(self):
        self._facing = 'D'
        self.replayWrite('lookDown')

    def lookLeft(self):
        self._facing = 'L'
        self._facingDirectionTexture = 'L'
        self.rendering()
        self.replayWrite('lookLeft')

    def lookRight(self):
        self._facing = 'R'
        self._facingDirectionTexture = 'R'
        self.rendering()
        self.replayWrite('lookRight')

    def moveUp(self):
        cords = [self._playerX, self._playerY-1]
        self._facing = 'U'
        self.replayWrite('moveUp')
        self.checkMovement(cords)

    def moveDown(self):
        cords = [self._playerX, self._playerY+1]
        self._facing = 'D'
        self.replayWrite('moveDown')
        self.checkMovement(cords)

    def moveLeft(self):
        cords = [self._playerX -1, self._playerY]
        self._facingDirectionTexture = 'L'
        self._facing = 'L'
        self.replayWrite('moveLeft')
        self.checkMovement(cords)

    def moveRight(self):
        cords = [self._playerX +1, self._playerY]
        self._facingDirectionTexture = 'R'
        self._facing = 'R'
        self.replayWrite('moveRight')
        self.checkMovement(cords)

    def checkMovement(self, cords):            
        if self.isWalkable(cords, True):
            self._playerX, self._playerY = cords
            if 'exit' in self._currentLevel[self._playerX][self._playerY] and self._currentLevel[self._playerX][self._playerY]['exit']['exit']:
              if 'nextLevelList' in self._currentLevel[self._playerX][self._playerY]['exit'] and self._currentLevel[self._playerX][self._playerY]['exit']['nextLevelList'] in self._defaultlevels:
                self.newLevel(self._currentLevel[self._playerX][self._playerY]['exit']['nextLevelList'])
              else:
                self.newLevel(self.dataDict['dungeon']['defaultLevelList'])
            else:
                self.enemyFullTurn()
        self.rendering()

    def logging(self, item,q=0, w=0, e=0,r=0 ,t=0,y=0, u=0, i=0, o=0, p=0):
        if self.doLogging:
            self.log = open(f'logs/logFiles/log{self.dt_string}.txt', "a+")
            self.log.write(f'{item}')
            extra = [q,w,e,r,t,y,u,i,o,p]
            for x in extra:
                if x != 0:
                    self.log.write(f' {x} ')
            self.log.write(f'\n')
            self.log.close()  

    def replayWrite(self, text):
        if self.doReplayMode:
            self.replay = open(f'logs/replayFiles/replay{self.dt_string}.txt', "a+")  
            self.replay.write(f'{text}\n')
            self.replay.close() 

    def enemyFullTurn(self):
        self.enemyTurn(True)
        if self.dataDict['debug']['enemyLoop'] >= 2:
            for _ in range(self.dataDict['debug']['enemyLoop']-1):
                self.enemyTurn(False)

    def wait(self) -> None:
        self.replayWrite('wait')
        self.enemyFullTurn()

    def autoSelect(self, syntax= 'show') -> bool:
        self.replayWrite(f'equipWeapon "{syntax}"')
        match syntax:
            case 0:
                syntax = False
            case 1:
                syntax = True
        if syntax == 'show':
            self.displayText(f'"autoSelect better weapons" is set to: {self.autoEquip}')
        elif syntax == True or syntax == False:
            self.autoEquip = syntax
            self.displayText(f'"autoSelect better weapons" has been set to: {self.autoEquip}')
        else:
            self.displayText(f'invalid syntax in autoSelect() function.\nSyntax needed: (True/False/\'show\'), syntax received: {syntax}')
            return False
        return True


    def showInventory(self) -> dict:
        items = list(self.inventory.keys())
        text = 'Your inventory contains:\n'
        for item in items:
            if self.inventory[item]["amount"] > 0:
                text += f'{self.inventory[item]["amount"]} x {item}\n' 
        self.displayText(text)
        return self.inventory

    def inInventory(self, item) -> bool:
        if item in self.inventory:
            if self.inventory[item]['amount'] > 0:
                return True
        return False

    def useItem(self, item) -> bool:
        usedItem = False
        self.replayWrite(f'useItem "{item}"')
        if self.inInventory(item):
            if item == self.equippedWeapon and self.inventory[item]['amount'] == 1:
                self.displayText(f"You have item: '{item}' equipped as weapon, to use it you need to unequip it first")
                return False
            else:
                if self.dataDict['tiles'][item]["loot"]["isConsumable"]:
                    usedItem = True
                    if 'strengthLevels' in self.dataDict["tiles"][item]["loot"]["consumable"]:
                        usedItem = True
                        self.playerStats["strength"] += self.dataDict["tiles"][item]["loot"]["consumable"]["strengthLevels"]
                    if self.dataDict['tiles'][item]["loot"]["consumable"]["type"] == '%':
                        extraHP = self.dataDict['tiles'][item]["loot"]["consumable"]["HPAmount"] * (self.playerStats["HP"]["max"] // 100)
                    elif self.dataDict['tiles'][item]["loot"]["consumable"]["type"] == '-%':
                        extraHP = self.dataDict['tiles'][item]["loot"]["consumable"]["HPAmount"] * (self.playerStats["HP"]["max"] // 100) * -1
                    elif self.dataDict['tiles'][item]["loot"]["consumable"]["type"] == '-':
                        extraHP = self.dataDict['tiles'][item]["loot"]["consumable"]["HPAmount"] * -1
                    elif self.dataDict['tiles'][item]["loot"]["consumable"]["type"] == '+':
                        extraHP = self.dataDict['tiles'][item]["loot"]["consumable"]["HPAmount"]
                    elif self.dataDict['tiles'][item]["loot"]["consumable"]["type"] == 'set':
                        extraHP = 0
                        self.playerStats["HP"]["current"] = self.dataDict['tiles'][item]["loot"]["consumable"]["HPAmount"]
                    self.playerStats["HP"]["current"] += extraHP
                    if self.playerStats["HP"]["current"] > self.playerStats["HP"]["max"]:
                        self.playerStats["HP"]["current"] = self.playerStats["HP"]["max"]
                if 'special' in self.dataDict['tiles'][item]["loot"]:
                    if 'nextFloor' in self.dataDict['tiles'][item]["loot"]['special']:
                        usedItem = True
                        self.newLevel(self.dataDict['tiles'][item]["loot"]['special']['nextFloor'])
                if 'text' in self.dataDict['tiles'][item]:
                    if self.dataDict['tiles'][item]['text']['fromList']:
                        text = self.dataDict['text'][self.dataDict['tiles'][item]['text']['text']][random.randint(0,len(self.dataDict['text'][self.dataDict['tiles'][item]['text']['text']])-1)]
                    else:
                        text = self.dataDict['tiles'][item]['text']['text']
                    self.displayText(text)
                if usedItem:
                    self.inventory[item]['amount'] -= 1
                    self.rendering()
                    return True
                elif self.dataDict['tiles'][item]["loot"]["isWeapon"]:
                    self.displayText(f"Item: '{item}' is defined as a weapon\nUse 'equipWeapon({item})' to equip it as weapon, or check the item information with 'itemInfo({item})'")
                    return False

        else:
            self.displayText(f"You don\'t have: '{item}'\nUse 'showInventory()' to see the items you have")
            return False


    def itemInfo(self, item) -> bool:
        if item not in self.dataDict['tiles']:
            self.displayText(f'{item} does not exist')
            return False
        elif self.dataDict['tiles'][item]['isLoot'] == False:
            self.displayText(f'{item} does not exist as item')
            return False
        else:
            self.displayText(f'-=={item}==-')
            self.displayText(f'Minimum per tile: {self.dataDict["tiles"][item]["loot"]["amount"]["min"]}\nMaximum per tile: {self.dataDict["tiles"][item]["loot"]["amount"]["max"]}')
            if self.dataDict["tiles"][item]["loot"]["isWeapon"]:
                self.displayText(f'Strength needed to weild this weapon: {self.dataDict["tiles"][item]["loot"]["weapon"]["minStrength"]}')
                self.displayText(f'It does {self.dataDict["tiles"][item]["loot"]["weapon"]["attack"]} attack damage\nWeapon type is {self.dataDict["tiles"][item]["loot"]["weapon"]["type"]}\nWeapon weight is {self.dataDict["tiles"][item]["loot"]["weapon"]["weaponWeight"]}')
            if 'loot' in self.dataDict["tiles"][item] and 'mergable' in self.dataDict["tiles"][item]['loot']:
                if self.dataDict["tiles"][item]['loot']["mergable"]:
                    text = ''
                    for item2 in list(self.dataDict['tiles'][item]['loot']['mergable']['mergeIntoAndAmount'].keys()):
                        if text != '':
                            text += ', '
                        text += f"{self.dataDict['tiles'][item]['loot']['mergable']['mergeIntoAndAmount'][item2]} x '{item2}'"
                    self.displayText(f"You can merge {self.dataDict['tiles'][item]['loot']['mergable']['mergeAmount']} x this item into: {text}")
            self.displayText(f'Item Rarity: {self.dataDict["tiles"][item]["loot"]["rarity"]}')
            if self.dataDict["tiles"][item]["loot"]["isConsumable"]:
                if 'strengthLevels' in self.dataDict["tiles"][item]["loot"]["consumable"]:
                    self.displayText(f'You will gain {self.dataDict["tiles"][item]["loot"]["consumable"]["strengthLevels"]} strength levels when consumed')
                if self.dataDict["tiles"][item]["loot"]["consumable"]["type"] != 'set':
                    if self.dataDict["tiles"][item]["loot"]["consumable"]["type"] != '-' and self.dataDict["tiles"][item]["loot"]["consumable"]["type"] != '-%':
                        percentOrNot = ""
                        if self.dataDict["tiles"][item]["loot"]["consumable"]["type"] == '%':
                            percentOrNot = '%'
                        self.displayText(f'It restores {self.dataDict["tiles"][item]["loot"]["consumable"]["HPAmount"]}{percentOrNot} HP when consumed')
                    else:
                      percentOrNot = ""
                      if self.dataDict["tiles"][item]["loot"]["consumable"]["type"] == '-%':
                          percentOrNot = '%'
                      self.displayText(f'You will take {self.dataDict["tiles"][item]["loot"]["consumable"]["HPAmount"]}{percentOrNot} HP damage when consumed')
                else:
                    self.displayText(f'Will set your HP to {self.dataDict["tiles"][item]["loot"]["consumable"]["HPAmount"]} when consumed')
            if "special" in self.dataDict["tiles"][item]["loot"]:
                if self.dataDict["tiles"][item]["loot"]["special"]["nextFloor"]:
                    self.displayText('It will warp you to the next floor')
            return self.dataDict["tiles"][item]
        

    def equipWeapon(self,item) -> bool:
        self.replayWrite(f'equipWeapon "{item}"')
        if self.inInventory(item):
            if self.dataDict['tiles'][item]["loot"]["isWeapon"]:
                self.equippedWeapon = item
                self.hasWeaponWeight = self.dataDict['tiles'][self.equippedWeapon]["loot"]['weapon']['weaponWeight']
                self.displayText(f"You equipped {item}")
                return True
            else:
                self.displayText(f"Item: '{item}' is not defined as a weapon\nUse 'useItem({item})' to use it as item, or check the item information with 'itemInfo({item})'")
                return False
        else:
            self.displayText(f"You don\'t have: '{item}'\nUse 'showInventory()' to see the items you have")
            return False

    def newLevel(self, levelType):
        self.logging('newLevel()')
        self._dungeonLevel += 1
        self.loadState()
        levelNumber = random.randint(0,len(self._defaultlevels[levelType])-1)
        print(levelNumber)
        self._canvas.destroy()
        self.createLevel(self._defaultlevels[levelType][levelNumber], levelNumber)
        self.createCanvas()
        self.rendering()

    def displayText(self, text,q=0, w=0, e=0,r=0 ,t=0,y=0):
        extra = [q,w,e,r,t,y]
        for x in extra:
            if x != 0:
                text += f'\n{x}'
        print(text)
        self.rendering()