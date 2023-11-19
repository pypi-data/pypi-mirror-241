# =============================================================================
# Author: Bob Anderson    16 November 2023
#
#     A threaded single camera system with a tkinter GUI using
#     a separate core for image capture into RAM
#
#     Incorporates control of the IOTAflasherpip instal
#
# =============================================================================

__version__ = "1.0.0"

import gc
import glob

# import serial
import serial.tools.list_ports as port_list
import serial.serialwin32 as win_serial


import matplotlib
from astropy.io import fits
# from matplotlib.pyplot import Figure
# import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg,
# NavigationToolbar2Tk
# )

import psutil
import tkinter
from tkinter import ttk, scrolledtext, simpledialog
from tkinter.simpledialog import Dialog

import pyautogui
from dateutil import parser
import datetime
from datetime import timezone

# import win32api
import pickle
import tkinter.filedialog as fd
import tkinter.messagebox as messageBox
import tkinter.simpledialog as simpleDialog
import time
# from time import perf_counter
import os
import threading
import tkinter as tk
import numpy as np
import sys

# Special imports (modules not normally available - require special install)
# import PySpin
import zwoasi as asi
from PIL import Image, ImageTk
import astropy.io.fits as pyfits
from multiprocess import Queue, Value, Process  # noqa import can't find module, but they work
# from numba import njit
# from numba.typed import List
import array

class NonModalInfoDialog(tk.Toplevel):

    # padx is used to make the dialog box big enough to display the whole title. This is needed
    # when the text provided is not wide enough. The user will see this and put a value in padx
    # to achieve the look wanted.

    # This is non-modal because we don't call self.grab_set()

    def __init__(self, parent, title=None, text='No text given', padx=None):
        super().__init__(parent)

        self.attributes('-topmost', 'true')

        self.focus()

        if title:
            self.title(title)
        else:
            self.title('No title given')

        if padx is None:
            padx = 100

        ttk.Label(self, text=text).pack(padx=padx)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

class AutoScrollbar(ttk.Scrollbar):
    """ A scrollbar that hides itself if it's not needed.
        Works only if you use the grid geometry manager """
    def set(self, lo, hi):
        try:
            if float(lo) <= 0.0 and float(hi) >= 1.0:
                self.grid_remove()
            else:
                self.grid()
                ttk.Scrollbar.set(self, lo, hi)
        except Exception as _:  # noqa
            pass
    def pack(self, **kw):
        raise tk.TclError('Cannot use pack with this widget')
    def place(self, **kw):
        raise tk.TclError('Cannot use place with this widget')
    def remove(self):
        self.grid_remove()

class A_ScollableCanvas(ttk.Frame):
    """ Advanced zoom of the image """
    def __init__(self, mainframe, width, height, pixelValueDisplay, zoom_factor=1):
        """ Initialize the main Frame """
        ttk.Frame.__init__(self, master=mainframe)
        self.container = None
        self.rawTile = None
        self.rawImage = None
        self.pixelValueDisplay = pixelValueDisplay
        self.vbar = AutoScrollbar(self.master, orient='vertical')
        self.hbar = AutoScrollbar(self.master, orient='horizontal')
        self.vbar.grid(row=0, column=1, sticky='ns')
        self.hbar.grid(row=1, column=0, sticky='we')
        # Create canvas and put image on it
        self.canvas = tk.Canvas(self.master, highlightthickness=0,
                                xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set, cursor='arrow')
        # The sticky value used below works. It's sticky 'ns' and 'we' (expands to fill all space)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()  # wait till canvas is created
        self.vbar.configure(command=self.scroll_y)  # bind scrollbars to the canvas
        self.hbar.configure(command=self.scroll_x)
        # Make the canvas expandable
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        # Bind events to the Canvas
        self.canvas.bind('<Configure>', self.show_image)  # canvas is resized
        self.canvas.bind('<ButtonPress-1>', self.left_click)
        # self.canvas.bind('<B1-Motion>',     self.move_to)
        # self.canvas.bind('<MouseWheel>', self.wheel)  # with Windows and MacOS, but not Linux
        # self.canvas.bind('<Button-5>',   self.wheel)  # only with Linux, wheel scroll down
        # self.canvas.bind('<Button-4>',   self.wheel)  # only with Linux, wheel scroll up
        # self.height, self.width = self.image.shape
        self.height = height
        self.width = width
        self.imscale = zoom_factor  # scale for the canvas image
        # print(f'Constructing a new scrollable canvas: {self.width} x {self.height} with zoom = {zoom_factor}')

        # Put image into container rectangle and use it to set proper coordinates to the image

        self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)
        self.canvas.update()  # wait till container is created

        # self.show_image()

    def close(self):
        self.vbar.set(lo=-1, hi=2)
        self.vbar.update()
        self.hbar.set(lo=-1, hi=2)
        self.hbar.update()

        self.vbar.destroy()
        self.hbar.destroy()
        self.canvas.grid_remove()
        self.grid_remove()
        # print('A_ScrollableCanvas executed its close()')
    def scroll_y(self, *args, **kwargs):
        """ Scroll canvas vertically and redraw the image """
        self.canvas.yview(*args, **kwargs)   # noqa # scroll vertically
        self.show_image()  # redraw the image
    def scroll_x(self, *args, **kwargs):
        """ Scroll canvas horizontally and redraw the image """
        self.canvas.xview(*args, **kwargs)   # noqa # scroll horizontally
        self.show_image()  # redraw the image
    def left_click(self, event):
        """ Remember previous coordinates for scrolling with the mouse """
        if self.rawTile is not None:
            if self.rawTile.dtype == np.uint16:
                scale = 16
            else:
                scale = 1
            try:
                msg = f'pixel value clicked on:  {self.rawTile[event.y, event.x] // scale}'
                # print(msg)
                self.pixelValueDisplay.configure(text=msg)

            except IndexError as e1:
                self.pixelValueDisplay.configure(text=f'{e1}')
                # print(f'{e}')
        else:
            pass
            # print(f'x: {event.x}  y: {event.y}')
        self.canvas.scan_mark(event.x, event.y)

    # def move_to(self, event):
    #     """ Drag (move) canvas to the new position """
    #     self.canvas.scan_dragto(event.x, event.y, gain=1)
    #     self.show_image()  # redraw the image
    def wheel(self, event):
        """ Zoom with mouse wheel """
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        bbox = self.canvas.bbox(self.container)  # get image area
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]: pass  # Ok! Inside the image
        else: return  # zoom only inside image area
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down (to zoom out)
            if self.imscale > 1:
                self.imscale //= 2
        if event.num == 4 or event.delta == 120:  # scroll up (to zoom in)
            if self.imscale < 16:
                self.imscale *= 2
        self.show_image()

    def zoom_factor(self):
        return self.imscale

    def set_new_image(self, image, theRawImage):
        self.image = image
        self.rawImage = theRawImage
        self.show_image()
    def show_image(self, event=None):    # noqa (event not used
        """ Show image on the Canvas """
        if self.container is None:
            return
        bbox1 = self.canvas.bbox(self.container)  # get image area
        # Remove 1 pixel shift at the sides of the bbox1
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
        bbox2 = (self.canvas.canvasx(0),  # get visible area of the canvas
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  # whole image is in the visible area
            bbox[0] = bbox1[0]
            bbox[2] = bbox1[2]
        if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  # whole image is in the visible area
            bbox[1] = bbox1[1]
            bbox[3] = bbox1[3]
        self.canvas.configure(scrollregion=tuple(bbox))   # noqa # set scroll region
        x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        try:
            if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
                # x = min(int(x2 / self.imscale), self.width)   # sometimes it is larger on 1 pixel...
                # y = min(int(y2 / self.imscale), self.height)  # ...and sometimes not
                self.rawTile = self.rawImage[int(y1):int(y2), int(x1):int(x2)]
                imagetk = ImageTk.PhotoImage(Image.fromarray(self.image[int(y1):int(y2), int(x1):int(x2)]))
                imageid = self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                                   anchor='nw', image=imagetk)
                self.canvas.lower(imageid)  # set image into background
                self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection
        except Exception as e1:
            print(f'In show_image() of Zoom_Advanced: {e1}')

# Constants  ##################################

DEV_MODE = False
WRITE_FILES_ASAP = True     # Set this false to file writing commence only at end of image acquisition
MAX_RAM_USAGE_PCT = 90      # Threshold memory usage used  to stop acquisition for excessive memory usage
VERSION = 'src Version 1.0.0'

RAW16 = 2  # Unique to ZWO - code number for 16 bit output
UINT8 = 0  # Unique to ZWO - code number for unsigned 8 bit output

FLASH_OFF_FRAME_COUNT = 10
FLASH_ON_FRAME_COUNT = 10
FLASH_FRAMES = FLASH_OFF_FRAME_COUNT + FLASH_ON_FRAME_COUNT

# Globals  ###################################

flashLightCurve = []

canvasFrame = None  # Used in zooming the image
imageZoomScroller = None
pixelValueLabel = None

histogramStack = []

arduinoPort = None

frameNumber = 0
timeOfLastFrame = None
numFramesTimed = None
avgFrameTime = 0.0

rawImage = None

lastLedIntensity = 0

flashOffCmdString = ''
flashOnCmdString = ''

doNotAskForTimeCorrectionAgain = False
okToCorrectComputerUTCtime = False
permissionToChangeClockGranted = False
leapSeconds = 0

lastROIinputString = ''

binSizeSet = False
bin_size = None
imageTypeSet = False
image_type = None

cameraInfoDict = {}
cameraControlInfo = {}

# This dictionary contains the current value of all camera parameters. It must be maintained this
# way whenever individual camera parameters are changed.
cameraState = {'videoOn': False}

# These globals are used by scrubImage() for speed of access

xOffsetOfRoi = 0
yOffsetOfRoi = 0
xRoiSize = 0
yRoiSize = 0

outlawList = [()]  # outlaw points is a list of coordinate tuples

GLOBAL = {}  # noqa # A dictionary to fill with globals

GLOBAL['imageWriteQueue'] = Queue()
GLOBAL['guiCmdQueue'] = Queue()
GLOBAL['displayQueue'] = Queue()
GLOBAL['camCmdQueue'] = Queue()
GLOBAL['camReaderQueue'] = Queue()

timestampList = []  # Used for debugging only

GLOBAL['fileWritingInProgress'] = Value('i', False)
GLOBAL['cameraIsRunning'] = Value('i', False)
GLOBAL['numFramesToRecord'] = Value('i', 0)
GLOBAL['numFramesWritten'] = Value('i', 0)
GLOBAL['framesAcquired'] = Value('i', 0)
GLOBAL['UTCstartArmed'] = Value('i', False)

saveFolderRoot = ''
fitsFolderPath = ''
folderName = ''
fitsRoot = ''  # optional identifier (prefix for each FITS file written

iniDict = {}
window: tkinter.Tk
textlbl: tkinter.Label
imglabel: tkinter.Label
canvas: tkinter.Canvas
image_container = None
memoryUsageBar: ttk.Progressbar
memoryUsageLabel = tkinter.Label
fileProgressBar: ttk.Progressbar
startButton: tk.Button
setUtcButton: tk.Button
roiXoffsetScale: ttk.Scale
roiYoffsetScale: ttk.Scale
gainEntry: ttk.Spinbox
setExposureButton: tk.Button
setGammaButton: tk.Button
setUSB3SpeedButton: tk.Button
showCameraSettingsButton: tk.Button
scrubCheckbox: tk.Checkbutton
ledCurrentSelectorLabel: tk.simpledialog
ledCurrentSelector: tk.OptionMenu
ledIntensityScale: tk.Scale

frameCount: tk.StringVar
framePath: tk.StringVar
contrastLow: tk.DoubleVar
contrastHigh: tk.DoubleVar
xOffsetRoi: tk.IntVar
yOffsetRoi: tk.IntVar
gain: tk.DoubleVar
exposure: tk.IntVar
gamma: tk.StringVar
blackSetting: tk.StringVar
utcSetting: tk.StringVar
utcDuration: tk.DoubleVar
roiSetting: tk.StringVar
imageXoffset: tk.IntVar
imageYoffset: tk.IntVar
zoomLevel: tk.StringVar
ledIntensityRange: tk.StringVar
ledIntensity: tk.IntVar
highCheckBox: tk.IntVar
midCheckBox: tk.IntVar
lowCheckBox: tk.IntVar
gui: tk.Tk

class USB3SpeedDialog(Dialog):
    # override body() to build your input form
    def body(self, master):
        tk.Label(master, text="Select USB3 speed to be used by the camera", anchor="w").pack(fill="x")
        # need to return the widget to have first focus
        # return self.text
        return None

    def answer_high(self):
        self.answer = 'High'
        self.ok()  # noqa Dialog class does provide this method

    def answer_normal(self):
        self.answer = 'Normal'
        self.ok()  # noqa Dialog class does provide this method

    # override buttonbox() to create your action buttons
    def buttonbox(self):
        box = tk.Frame(self)
        # note that self.ok() and self.cancel() are defined inside `Dialog` class
        tk.Button(box, text="High", width=10, command=self.answer_high, default=tk.ACTIVE)\
            .pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Normal", width=10, command=self.answer_normal)\
            .pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    # override apply() to return data you want
    def apply(self):
        self.result = self.answer

class SliderDialog(Dialog):
    def __init__(self, a_gui, title=None, initialValue=50, minVal=0, maxVal=100, length=400):
        self.initialValue = initialValue  # body() is called by iDialog.__init__ so we have to set initialValue here.
        self.minVal = minVal
        self.maxVal = maxVal
        self.length = length
        Dialog.__init__(self, a_gui, title=title)

    # override body() to build your input form
    def body(self, master):
        self.slider = tk.Scale(master, from_=self.minVal, to=self.maxVal, orient='horizontal', length=self.length)
        self.slider.set(self.initialValue)
        self.slider.pack(side=tk.TOP, expand=True, fill="x")

    # override buttonbox() to create your action buttons
    def buttonbox(self):
        box = tk.Frame(self)
        tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)  # noqa
        tk.Button(box, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)  # noqa
        box.pack()

    # override apply() to return data you want
    def apply(self):
        self.result = self.slider.get()

class ButtonAnswerDialog(Dialog):
    def __init__(self, a_gui, title=None, buttonOneText='One', buttonTwoText='Two', length=400):
        self.length = length
        self.buttonOneText = buttonOneText
        self.buttonTwoText = buttonTwoText
        Dialog.__init__(self, a_gui, title=title)

    def answer_one(self):
        self.answer = self.buttonOneText
        self.ok()  # noqa Dialog class does provide this method

    def answer_two(self):
        self.answer = self.buttonTwoText
        self.ok()  # noqa Dialog class does provide this method

    # override body() to build your input form
    def body(self, master):
        return

    # override buttonbox() to create your action buttons
    def buttonbox(self):
        box = tk.Frame(self)
        tk.Button(box, text=self.buttonOneText, width=10, command=self.answer_one, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)  # noqa
        tk.Button(box, text=self.buttonTwoText, width=10, command=self.answer_two).pack(side=tk.LEFT, padx=5, pady=5)  # noqa
        box.pack()

    # override apply() to return data you want
    def apply(self):
        self.result = self.answer

# function to write FITS files from frames in the queue: This operates in a separate thread
def writeFilesThread():
    global fileProgressBar, xRoiSize, yRoiSize, xOffsetOfRoi, yOffsetOfRoi, flashLightCurve

    while True:
        if GLOBAL['fileWritingInProgress'].value or WRITE_FILES_ASAP:

            imageList = GLOBAL['imageWriteQueue'].get()  # noqa
            # Documentation: imageList contains [frameNumber, droppedFrames, image, time.perf_counter_ns(), averageFrameTime, cpu_utc]
            averageFrameTime = imageList[4] / 1_000_000  # Turns ns into milliseconds
            frame = imageList[0]  # frameNumber from the queue is relative to first image given to be written
            # print(f"frameNum: {GLOBAL['numFramesWritten'].value}  "
            #       f"framesToRecord: {GLOBAL['numFramesToRecord'].value}  "
            #       f"currentFrame: {frame}")
            increment = int(np.ceil((GLOBAL['numFramesToRecord'].value + FLASH_FRAMES) / 100))
            if frame % increment == 0:
                progress = (frame / (GLOBAL['numFramesToRecord'].value + FLASH_FRAMES)) * 100
                fileProgressBar['value'] = min(progress, 100)

            GLOBAL['numFramesWritten'].value += 1
            # Compose filename
            filepath = f'{fitsFolderPath}/{fitsRoot}{imageList[0]:07d}.fits'
            image = imageList[2]
            if cameraState['imageType'] == RAW16:  # raw16
                outlist = pyfits.PrimaryHDU(image)
            else:
                image = np.array(image, dtype='uint8')
                outlist = pyfits.PrimaryHDU(image)

            # Compose FITS header
            outhdr = outlist.header
            # Add required elements
            outhdr['SIMPLE'] = True
            outhdr['NAXIS'] = 2
            # end required elements

            ts_str = imageList[5].strftime('%Y-%m-%dT%H:%M:%S.%f')
            outhdr['CPU-OBS'] = ts_str
            outhdr.comments['CPU-OBS'] =  'System Clock:Est. Frame Start'
            outhdr['SWCREAT1'] = __version__

            outhdr['INSTRUME'] = cameraState['cameraName']
            outhdr['COMMENT'] = f"  exposure req: {cameraState['exposure'][0] / 1_000:0.3f} milliseconds"
            outhdr['COMMENT'] = f"avg frame time: {averageFrameTime:0.3f} milliseconds"
            fps = 1.0 / (averageFrameTime / 1000.0)
            outhdr['COMMENT'] = f"avg frame rate: {fps:0.2f} fps"
            # outhdr['COMMENT'] = f"flashLevel: {np.sum(image)}"
            flashLightCurve.append(np.sum(image))
            # print(f"frame {frame:04d}  flashLevel: {np.sum(image)}")

            outhdr['COMMENT'] = f"gain: {cameraState['gain'][0]}"
            outhdr['COMMENT'] = f"ZWO gamma: {cameraState['gamma']} (ZWO 50 = gamma of 1.0)"
            outhdr['COMMENT'] = f"A/D bit depth: {cameraState['bitDepth']}"
            outhdr['COMMENT'] = f"black level: {cameraState['blackLevel']}"
            outhdr['COMMENT'] = f"full sensor width: {cameraState['maxImageWidth']} pixels"
            outhdr['COMMENT'] = f"full sensor height: {cameraState['maxImageHeight']} pixels"
            outhdr['COMMENT'] = f"ROI width: {cameraState['currentImageWidth']} pixels"
            outhdr['COMMENT'] = f"ROI height: {cameraState['currentImageHeight']} pixels"
            outhdr['COMMENT'] = f"ROI height offset: {cameraState['yOrigin']}"
            outhdr['COMMENT'] = f"ROI width offset: {cameraState['xOrigin']}"

            # write the fits file
            outlist.writeto(filepath, overwrite=True)

            if frame >= GLOBAL['numFramesToRecord'].value - 1 + FLASH_FRAMES:  # This the termination test
                fileProgressBar['value'] = 0
                showInfo('File write status',
                         f"\n@ frame: {frame+1} ... all RAM images have been written to files.\n\n\n\n")
                GLOBAL['numFramesWritten'].value = 0
                processFlashLightCurve()
                flashLightCurve = []  # Reset the list to empty, ready for the next capture.

        else:
            time.sleep(0.1)

def processFlashLightCurve(ts1='2023-11-11 16:29:20+00:00', ts2='2023-11-11 16:29:21+00:00'):
    global flashLightCurve, fitsFolderPath

    DOC_ON = True

    # The values for ts1 and ts1 are for test purposes only. Used with a 100 ms exposure, and a 1010 frame
    # manual record (1000 frames - 100 seconds - between flash edges), the timing will be accurate
    # ts2 = 2023-11-11 16:31:10+00:00

    # For a 110 frame manual record, use ts2 = 2023-11-11 16:29:30+00:00

    # For a 110 frame manual record at 10 ms exposure, use ts2 = 2023-11-11 16:29:21+00:00

    t1 = parser.parse(ts1)  # Create a datetime object
    t2 = parser.parse(ts2)

    if DOC_ON: print(t1,t2, '\n')

    seconds_apart = (t2-t1).total_seconds()

    if DOC_ON: print(f"timestamp difference: {seconds_apart} seconds")

    if DOC_ON: print(len(flashLightCurve))
    if DOC_ON: print(flashLightCurve)

    # Initially we extract parameters from the entire set of points. Those values may be 'off' a bit if
    # viewing conditions are very different as the recording progresses.
    # We will assume that that is happening and refine the calcultions by isolating flash light curve points
    # from the beginning, and then from the end of the recording, and recalculating using only nearby points.

    # First estimation:
    max_flash_level = np.max(flashLightCurve)
    min_flash_level = np.min(flashLightCurve)
    mid_flash_level = (max_flash_level + min_flash_level) // 2

    # Find first flash region using the 'first estimation' values
    first_flash = []

    state = 'accumulateBottom'

    for value in flashLightCurve:
        if state == 'accumulateBottom':
            if value < mid_flash_level:
                first_flash.append(value)
            else:
                state = 'accumulateTop'

        if state == 'accumulateTop':
            if value >= mid_flash_level:
                first_flash.append(value)
            else:
                break

    if DOC_ON: print(f"\nfirst_flash: {first_flash}")

    # Now we recalculate the parameters using only the points in the first flash
    max_flash_level_first = np.max(first_flash)
    min_flash_level_first = np.min(first_flash)
    mid_flash_level_first = (max_flash_level_first + min_flash_level_first) // 2
    lower_half_first = [value for value in first_flash if value < mid_flash_level_first]
    median_low_first = int(np.median(lower_half_first))

    thresh = (max_flash_level_first - min_flash_level_first) // 1000  # This gets ms level precision for 1 second exposures
    for i, value in enumerate(first_flash):
        if value > median_low_first + thresh:
            first_flash_index = i
            print(f"found R transition point at frame {first_flash_index} with value {value}")
            break

    # std_first_bottom = np.std(first_flash[0:i])  # noqa
    mean_first_bottom = np.mean(first_flash[0:i])  # noqa
    # snr_bottom = mean_first_bottom / std_first_bottom
    # if DOC_ON: print(f"std first_flash bottom: {std_first_bottom:0.2f}  mean_low_first: {mean_first_bottom:0.1f}  SNR: {snr_bottom:0.0f}")
    # std_first_top = np.std(first_flash[i+1:-1])
    mean_first_top = np.mean(first_flash[i+1:-1])
    # snr_top = mean_first_top / std_first_top
    # if DOC_ON: print(f"std first_flash top: {std_first_top:0.2f}  mean_first_top: {mean_first_top:0.1f}  SNR: {snr_top:0.0f}")

    time_correction_first = (first_flash[i] / (mean_first_top - mean_first_bottom)) * cameraState['exposure'][0]  # microseconds
    if DOC_ON: print(f"time_corrrection first_flash: {time_correction_first:0.2f} microseconds")

    tf1 = t1 - datetime.timedelta(microseconds=round(time_correction_first))
    if DOC_ON: print(tf1)

    # Now we need to find the last flash. To do that, we'll work backwards

    state = 'traverseRightBottom'
    k = len(flashLightCurve) - 1  # We use k to iterate backwards through the flashLightCurve
    while True:
        value = flashLightCurve[k]
        if state == 'traverseRightBottom':
            if value < mid_flash_level:  # we're still in the flash off portion of the tail
                k -= 1
            else:
                state = 'traverseTop'
                last_flash_top_end = k  # Save this because we need to know where the top of the last flash ends

        if state == 'traverseTop':
            if value >= mid_flash_level:  # We're still in the flash on portion
                k -= 1
            else:
                state = 'traverseLeftBottom'

        if state == 'traverseLeftBottom':
            k -= FLASH_OFF_FRAME_COUNT  # No need to do anything other than backup to give a normal flash off zone
            last_flash_bottom_start = k
            break

        if k <= 0:
            showInfo('Data error', "Could not find the terminating flash")

    last_flash = flashLightCurve[last_flash_bottom_start:last_flash_top_end+1]  # noqa
    if DOC_ON: print(f"last_flash: {last_flash}")

    # Now we recalculate the parameters
    max_flash_level_last = np.max(last_flash)
    min_flash_level_last = np.min(last_flash)
    mid_flash_level_last = (max_flash_level_last + min_flash_level_last) // 2
    lower_half_last = [value for value in last_flash if value < mid_flash_level_last]
    median_low_last = int(np.median(lower_half_last))
    if DOC_ON:
        print(f"max_flash_level_last: {max_flash_level_last}  min_flash_level_last: {min_flash_level_last} "
              f" median_low_last: {median_low_last}")

    if DOC_ON: print(f"last_flash_bottom_start: {last_flash_bottom_start}")

    thresh = (max_flash_level_last - min_flash_level_last) // 1000  # ms precision for 1 second exposure
    for i in range(last_flash_bottom_start, len(flashLightCurve)):
        if flashLightCurve[i] > median_low_last + thresh:
            last_flash_index = i
            print(f"found R transition point at frame {last_flash_index} with value {value}")
            break

    # std_last_bottom = np.std(flashLightCurve[last_flash_bottom_start:last_flash_index])  # noqa
    mean_last_bottom = np.mean(flashLightCurve[last_flash_bottom_start:last_flash_index])  # noqa
    # snr_bottom = mean_last_bottom / std_last_bottom
    # if DOC_ON: print(f"\nstd last_flash bottom: {std_last_bottom:0.2f}  mean_low_last: {mean_last_bottom:0.1f}  SNR: {snr_bottom:0.0f}")
    # std_last_top = np.std(flashLightCurve[last_flash_index+1:last_flash_top_end])
    # if DOC_ON: print(flashLightCurve[last_flash_index+1:last_flash_top_end])
    mean_last_top = np.mean(flashLightCurve[last_flash_index+1:last_flash_top_end])
    # snr_top = mean_last_top / std_last_top
    # if DOC_ON: print(f"std last_flash top: {std_last_top:0.2f}  mean_last_top: {mean_last_top:0.1f}  SNR: {snr_top:0.0f}")

    time_correction_last = (flashLightCurve[last_flash_index] / (mean_last_top - mean_last_bottom)) * cameraState['exposure'][0]
    if DOC_ON: print(f"time_corrrection last_flash: {time_correction_last:0.2f} microseconds")

    tf2 = t2 - datetime.timedelta(microseconds=round(time_correction_last))

    # Because datetime objects have 1 microsecond resolution (not enough to reliably extrapolate over 1000 to 10000 points),
    # we calculate our own delta with more than 1 microsecond resolution
    precison_time_difference = (t2 - t1).total_seconds() * 1_000_000 + time_correction_first - time_correction_last
    precision_delta = precison_time_difference / (last_flash_index - first_flash_index)  # noqa
    if DOC_ON: print(f"precision_time_difference: {precison_time_difference:0.2f} microseconds")
    if DOC_ON: print(f"precision_delta: {precision_delta:0.2f} microseconds")
    if DOC_ON: print(tf2)
    if DOC_ON: print(tf2-tf1)

    # Now we need to calculate a timestamp list.

    # We calculate a frame time from the timestamped readings...
    if DOC_ON: print(first_flash_index, last_flash_index)  # noqa
    frameTime = (tf2 - tf1) / (last_flash_index - first_flash_index)   # noqa
    if DOC_ON: print(type(frameTime), frameTime)

    timestamps = []
    t0 = tf1 - datetime.timedelta(microseconds=first_flash_index * precision_delta)
    print(f"len(flashLightcurve): {len(flashLightCurve)}")
    for i in range(len(flashLightCurve)):
        tn = t0 + datetime.timedelta(microseconds=i * precision_delta)
        ts_str = tn.strftime('%Y-%M-%dT%H:%M:%S.%f')
        timestamps.append(ts_str)
        print(f"{i:03d}: {ts_str}")
    print(f"{first_flash_index:03d} should be {tf1}  ...was: {timestamps[first_flash_index]}")
    print(f"{last_flash_index:03d} should be {tf2}  ...was: {timestamps[last_flash_index]}")

    # Finally, we need to add to all the FITS files DATE-OBS (timestamp header)
    fitsFiles = glob.glob(f'{fitsFolderPath}/*.fits')
    print(f"Num fits files found: {len(fitsFiles)}  last was: {fitsFiles[-1]}")

    # Now we sort them. This not needed fo src, but may be important for the planned utility.
    # In any case, it doesn't hurt.
    fitsFiles.sort()

    print(f"len(fitsFIles): {len(fitsFiles)}  len(timestamps): {len(timestamps)}")
    # assert len(fitsFiles) == len(timestamps), 'The number of FITS files and the number of timestamps are not equal!'

    cpu_timestamps = []
    i = 0
    for frame_file in fitsFiles:
        with fits.open(frame_file, mode='update') as hdul:
            hdr = hdul[0].header
            hdr['DATE-OBS'] = timestamps[i]
            hdr.comments['DATE-OBS'] = 'GPS: IotaFlasher v1.0'
            try:
                cpu_timestamp = hdr['CPU-OBS']
                cpu_timestamps.append(cpu_timestamp)
            except KeyError:
                pass
            i += 1

    print(f"Number of CPU-OBS timestamps found: {len(cpu_timestamps)}")

    if len(cpu_timestamps) > 0:
        cpu_frame_times = []
        # We can do a dropped/duplicated frame analysis
        for ts in cpu_timestamps:
            cpu_frame_times.append(datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S.%f'))
        deltas = []
        for i in range(1, len(cpu_frame_times)):
            deltas.append((cpu_frame_times[i] - cpu_frame_times[i-1]).total_seconds())
        print(f"avg delta: {np.mean(deltas):0.6f}  median delta: {np.median(deltas)}  max delta: {np.max(deltas)}  min delta: {np.min(deltas)}")

def getFormattedSettings():
    global cameraState, avgFrameTime
    lines = []  # noqa could be written as literal
    lines.append(f'Camera: {cameraState["cameraName"]}'
                 f' (sensor size: {cameraState["maxImageWidth"]}x{cameraState["maxImageHeight"]})'
                 f' (pixel size: {cameraState["pixelSize"]} microns)'
                 f' (ADC: {cameraState["bitDepth"]} bits)')
    lines.append('')

    requestedExposureTime = cameraState["exposure"][0]/1000

    # requestedFrameRate = 1000.0 / requestedExposureTime

    if cameraState["exposure"][1]:
        lines.append(f'Exposure time: {requestedExposureTime:0.3f} milliseconds (automatic exposure)   ')
                     # f'(FPS: {requestedFrameRate:0.3f})')
    else:
        lines.append(f'Requested exposure time: {requestedExposureTime:0.3f} milliseconds   ')
                     # f'(FPS: {requestedFrameRate:0.3f})')

    lines.append('')

    if avgFrameTime == 0.0:
        lines.append(f'Average frame time: -- cannot be measured until video is started')
    else:
        # frameChangeTime = 0.075  # 75 microseconds estimated camera processing time between frame (ns units)
        avgFrameRate = 1000.0 / avgFrameTime
        # lines.append(f'Actual exposure time: {avgFrameTime - frameChangeTime:0.3f} milliseconds   '
        #              f'(FPS: {avgFrameRate:0.3f})')
        lines.append(f'Average frame time: {avgFrameTime:0.3f} milliseconds   '
                     f'(FPS: {avgFrameRate:0.3f})')
        if (requestedExposureTime / avgFrameTime) < 0.80:
            showInfo('Camera settings issue\t\t\t\t\t\t\t\t',
                     f"Your request for an exposure time of {requestedExposureTime:0.3} milliseconds could "
                     f"not be honored by the camera.\n\n"
                     f"The combination of the selected ROI, binning level, USB3 speed (high or normal), "
                     f"the USB bandwidth percentage allocated to "
                     f"the camera, and the pixel type (1 byte or 2 bytes) required a longer exposure time "
                     f"(i.e., a lower frame rate).\n\n"
                     f"The camera increased the exposure time so that the USB3 connection was not overloaded, "
                     f"which could lead to dropped frames. This adjustment nearly always guarantees that there "
                     f"will be no dropped frames.")

    lines.append('')

    if cameraState["gain"][1]:
        lines.append(f'Gain: {cameraState["gain"][0]} (automatic gain)')
    else:
        lines.append(f'Gain: {cameraState["gain"][0]}')
    lines.append(f'Black level: {cameraState["blackLevel"]}')
    lines.append(f'Gamma setting: {cameraState["gamma"]}  (50 corresponds to gamma = 1.0)')
    lines.append(f'Electrons per ADU: {cameraState["elecPerADU"]:0.4f}')
    lines.append('')

    lines.append(f'bin size: {cameraState["binSize"]}')
    lines.append(f'ROI: {cameraState["currentImageWidth"]} x {cameraState["currentImageHeight"]} '
                 f'@ x = {cameraState["xOrigin"]}  y = {cameraState["yOrigin"]}')

    if cameraState["imageType"] == 0:
        lines.append(f'Image format: RAW8')
    elif cameraState["imageType"] == 1:
        lines.append(f'Image format: RGB24')
    elif cameraState["imageType"] == 2:
        lines.append(f'Image format: RAW16')
    elif cameraState["imageType"] == 3:
        lines.append(f'Image format: Y8')
    else:
        lines.append(f'Image format: Unknown - this is an error')

    lines.append('')

    flip_str = ['none', 'horizontal', 'vertical', 'horizontal and vertical']
    flip_state = cameraState['flipStatus']
    lines.append(f'Image flip: {flip_str[flip_state]}')

    lines.append('')

    if cameraState["bandwidth"][1]:
        lines.append(f'USB3 bandwidth usage: {cameraState["bandwidth"][0]}%  (automatic by camera)')
    else:
        lines.append(f'USB3 bandwidth usage: {cameraState["bandwidth"][0]}%  (set by user)')

    if cameraState["speedMode"] == 0:
        lines.append(f'USB3 speed mode: Normal')
    else:
        lines.append(f'USB3 speed mode: High speed mode')

    lines.append('')

    # The temperature in cameraState has already been divided by 10 to give degrees C correctly
    lines.append(f'Sensor temperature: {cameraState["temperature"]:0.1f} degrees C')

    lines.append('')
    lines.append(f'Dropped frame count: {cameraState["droppedFrames"]}')

    return lines

def connectToArduino(port):
    global arduinoPort

    try:
        arduinoPort = win_serial.Serial(
            port,
            baudrate=115200,
            # bytesize=serial.serialutil.EIGHTBITS,
            bytesize=8,
            # parity=serial.serialutil.PARITY_NONE,
            parity='N',
            # stopbits=serial.serialutil.STOPBITS_ONE,
            stopbits=1,
            rtscts=True,
            write_timeout=0.5  # seconds
        )
    except win_serial.SerialException as e:  # noqa
        showInfo('Arduino error',f"{e}")

    # Opening the Arduino port resets the Arduino (Windows behavior on the DTR line is the culprit)
    # So we give it time to get itself ready for our commands.
    my_dialog = NonModalInfoDialog(
        gui,
        title=f'Arduino availability:',
        text='Arduino was found ...\n'
              '... waiting for it to finish resetting.\n\n'
    )
    time.sleep(2)
    my_dialog.destroy()

def guiCmdHandler():
    global leapSeconds
    global cameraInfoDict, cameraState, cameraControlInfo, avgFrameTime, setUSB3SpeedButton

    while True:
        cmd = GLOBAL['guiCmdQueue'].get()  # noqa
        msg_arrival_time = time.perf_counter_ns()
        if cmd[0] == 'noCameraFound':
            showInfo(title='No camera found', msg=f'No ZWO ASI camera found.')
        elif cmd[0] == 'cameraFound':
            msg_sent_time = cmd[-1]
            if DEV_MODE:
                print(f'camera found: {msg_arrival_time - msg_sent_time} ns')
            askCameraSettings(show_settings=False)
        elif cmd[0] == 'flashON':
            sendLedIntensityCommandToArduino(flashOnCmdString)
        elif cmd[0] == 'flashOFF':
            sendLedIntensityCommandToArduino(flashOffCmdString)
        elif cmd[0] == 'ArduinoComPort':
            port = cmd[1]
            # showInfo(title='Arduino connection status', msg=f'Arduino is connected to port {port}')
            if not port == 'None':
                connectToArduino(port)  # sleeps for 2 seconds
            else:
                NonModalInfoDialog(gui, title='Arduino availability:',
                                   text='No com port to an Arduino Mega 2560 could be located')
                disableLEDintensityControls()
        elif cmd[0] == 'avgFrameTime':
            avgFrameTime = cmd[1]
        elif cmd[0] == 'cameraException':
            showInfo(title='!!! Exception thrown in camProc !!!', msg=cmd[1])
        elif cmd[0] == 'saveControlInfo':
            GLOBAL['camCmdQueue'].put(['startVideo'])
            cameraState['videoOn'] = True
            pixelValueLabel.configure(text='Video turned on')  # noqa


            cameraControlInfo = cmd[1]
            if DEV_MODE or True:  # TODO Remove this 'always print cameraControlInfo' override
                lines = []
                for cn in sorted(cmd[1].keys()):
                    print(f'    {cn}:')
                    lines.append(f'    {cn}:')
                    for k in sorted(cmd[1][cn].keys()):
                        print(f'        {k}: {repr(cmd[1][cn][k])}')
                        lines.append(f'        {k}: {repr(cmd[1][cn][k])}')
        elif cmd[0] == 'cameraInfo':
            cameraInfoDict = cmd[1]
            cameraState.update({'elecPerADU': cameraInfoDict["ElecPerADU"]})
            cameraState.update({'bitDepth': cameraInfoDict['BitDepth']})
            cameraState.update({'maxImageWidth': cameraInfoDict['MaxWidth']})
            cameraState.update({'maxImageHeight': cameraInfoDict['MaxHeight']})
            cameraState.update({'cameraName': cameraInfoDict['Name']})
            cameraState.update({'isColorCam': cameraInfoDict['IsColorCam']})
            cameraState.update({'pixelSize': cameraInfoDict["PixelSize"]})
        elif cmd[0] == 'gain':
            cameraState.update({'gain': cmd[1]})
        elif cmd[0] == 'exposure':
            cameraState.update({'exposure': cmd[1]})
        elif cmd[0] == 'blackLevel':
            cameraState.update({'blackLevel': cmd[1][0]})
        elif cmd[0] == 'gamma':
            cameraState.update({'gamma': cmd[1][0]})
        elif cmd[0] == 'roiSize':
            cameraState.update({'currentImageWidth': cmd[1][0]})
            cameraState.update({'currentImageHeight': cmd[1][1]})
            cameraState.update({'binSize': cmd[1][2]})
            cameraState.update({'imageType': cmd[1][3]})
        elif cmd[0] == 'roiCorner':
            cameraState.update({'xOrigin': cmd[1][0]})
            cameraState.update({'yOrigin': cmd[1][1]})
        elif cmd[0] == 'temperature':
            cameraState.update({'temperature': cmd[1][0]/10})
        elif cmd[0] == 'droppedFrames':
            cameraState.update({'droppedFrames': cmd[1]})
        elif cmd[0] == 'bandwidth':
            cameraState.update({'bandwidth': cmd[1]})
        elif cmd[0] == 'speedMode':
            cameraState.update({'speedMode': cmd[1][0]})
        elif cmd[0] == 'SDKversion':
            cameraState.update({'SDKversion': cmd[1]})
        elif cmd[0] == 'flipStatus':
            cameraState.update({'flipStatus': cmd[1][0]})
        elif cmd[0] == 'settingsDone':
            setting_lines = getFormattedSettings()
            show_scrollable_list(width=1000, height=600, lines=setting_lines, title='Current camera settings')

            if DEV_MODE:
                print(f'camera parameters in cameraState{"{}"}: {cameraState.keys()}')
            # print(f'camera parameters in cameraInfo{"{}"}: {cameraInfoDict.keys()}')
            titleMsg = f'{VERSION}  {cameraState["cameraName"]}' \
                       f' (sensor size: {cameraState["maxImageWidth"]}x{cameraState["maxImageHeight"]})' \
                       f' (pixel size: {cameraState["pixelSize"]} microns)' \
                       f' (ADC: {cameraState["bitDepth"]} bits)'
            gui.title(titleMsg)
        elif cmd[0] == 'leapSecondsChange':
            leapSeconds = cmd[1]
            showInfo('Leap second change',
                     f'A new leapSeconds value of {leapSeconds} was detected,\n'
                     f'saved, and is now in use.')
        elif cmd[0] == 'disableButtons':
            setExposureButton.config(state=tk.DISABLED)
            setGammaButton.config(state=tk.DISABLED)
            showCameraSettingsButton.config(state=tk.DISABLED)
            gainEntry.config(state=tk.DISABLED)
        elif cmd[0] == 'enableButtons':
            setUtcButton.config(bg='lightgray', text='Arm UTC start')
            startButton.config(bg='red', text='Start acquisition')
            setExposureButton.config(state=tk.NORMAL)
            setGammaButton.config(state=tk.NORMAL)
            showCameraSettingsButton.config(state=tk.NORMAL)
            gainEntry.config(state=tk.NORMAL)
        elif cmd[0] == 'captureReport':
            messageBox.showinfo('Capture statistics', f'{cmd[1]}\n\n{cmd[2]}')
        elif cmd[0] == 'utcButtonGreen':
            setUtcButton.config(bg='green', text='UTC is running')
        elif cmd[0] == 'noCamera':
            messageBox.showerror('Camera not found',
                                 f"No camera was found.\n\n"
                                 f"Is it turned off?")
        elif cmd[0] == 'serialPortParameters':
            messageBox.showinfo('Serial port parameters', f'{cmd[1]}{cmd[2]}{cmd[3]}{cmd[4]}')
        else:
            # This catches unimplemented commands, printing them quietly to the command window
            print(f'guiCmd received: {cmd}')


def camCaptureProc(GLOBAL):  # noqa (GLOBAL shadows)

    homeDir = os.path.split(__file__)[0]
    # print(f"homeDir: {homeDir}")
    asi.init(os.path.join(homeDir, "ASICamera2.dll"))
    num_cameras = asi.get_num_cameras()

    cameraIsInVideoCapture = False

    frameNumber = 0
    numFramesTimed = None
    timeOfLastFrame = None
    currentWriteFrame = None
    sendImagesToTheWriteQueue = False
    avgFrameTime = 0.0

    UTCstartTime = None

    def resetFrameTimeAverage():
        global frameNumber, timeOfLastFrame, numFramesTimed, avgFrameTime
        frameNumber = 0
        timeOfLastFrame = None
        numFramesTimed = None
        avgFrameTime = 0.0

    numBytes = None

    if num_cameras == 0:
        GLOBAL['guiCmdQueue'].put(["noCameraFound", "No ASI camera connected."])
        return
    else:
        GLOBAL['guiCmdQueue'].put(["cameraFound", time.perf_counter_ns()])

        ports = list(port_list.comports())
        if ports:  # If any COM ports were found ...
            for port in ports:  # Find out what is attached to each com port
                full_name = f'{port}'
                if 'Arduino Mega 2560' in full_name:  # This is the only port we want to use
                    print(f'Found the Arduino at {port.device}')
                    GLOBAL['guiCmdQueue'].put(['ArduinoComPort', port.device])
                else:
                    print(f'No Arduino port found.')
                    GLOBAL['guiCmdQueue'].put(['ArduinoComPort', "None"])
        else:  # No COM ports were found, so ...
            print(f'No Arduino port found.')
            GLOBAL['guiCmdQueue'].put(['ArduinoComPort', "None"])

        cameras_found = asi.list_cameras()
        if num_cameras == 1:
            camera_id = 0
            print(f'Found one camera: {cameras_found[0]}')
        else:
            print(f'Found {num_cameras} cameras')
            for n in range(num_cameras):
                print(f'    {n}: {cameras_found[n]}')
            # TO DO: allow user to select a camera - maybe - sometime - if good use case found (unlikely)
            camera_id = 0
            print(f'Using camera {camera_id}: {cameras_found[camera_id]}')

        camera = asi.Camera(camera_id)

    # TODO Remove this exploratory code
    print(f"asi.ASI_HIGH_SPEED_MODE: {asi.ASI_HIGH_SPEED_MODE}")
    control_value = camera.get_control_value(asi.ASI_HIGH_SPEED_MODE)
    print(f"high speed mode value: {control_value}")
    num_controls = camera.get_num_controls()
    print(f"num_controls: {num_controls}")
    # camera.set_control_value(asi.ASI_HIGH_SPEED_MODE, 1)  # This breaks the ASI432 - no video It doesn't have that control

    controls = camera.get_controls()

    GLOBAL['guiCmdQueue'].put(['saveControlInfo', controls])  # This will also turn on video

    keepRunning = True

    while keepRunning:

        # We only want to read video data if the camera is in videoCapture mode because we use an infinite wait for data
        if cameraIsInVideoCapture:
            try:
                flat_image = camera.get_video_data(timeout=None, buffer_=buffer)  # noqa (buffer might not be intialized)
                frameNumber += 1
                if timeOfLastFrame is None:
                    timeOfLastFrame = time.perf_counter_ns()
                    numFramesTimed = 0
                    # Set a default value for avgFrameTime in case it is needed during file writing of FITS header info
                    # The default value is the requested frame time - this will be close to correct anyway
                    avgFrameTime = camera.get_control_value(asi.ASI_EXPOSURE)[0] * 1_000
                else:
                    currentTime = time.perf_counter_ns()
                    delta = currentTime - timeOfLastFrame
                    if numFramesTimed < 1000:
                        cum = avgFrameTime * numFramesTimed
                        new_cum = cum + delta
                        numFramesTimed += 1
                        avgFrameTime = new_cum / numFramesTimed  # units: ns
                        # print(f'numFramesTimed: {numFramesTimed}  cum: {cum:0.1f}  delta: {delta}  new_cum: {new_cum:0.1f}  '
                        #       f'avgFrameTime: {avgFrameTime:0.1f}')
                    else:
                        cum = avgFrameTime * (numFramesTimed - 1)
                        new_cum = cum + delta
                        avgFrameTime = new_cum / numFramesTimed
                        # print(
                        #     f'numFramesTimed: {numFramesTimed}  cum: {cum:0.1f}  delta: {delta}  new_cum: {new_cum:0.1f}  '
                        #     f'avgFrameTime: {avgFrameTime:0.1f}')


                    # print(f'frame: {frameNumber:>6d}  frame delta: {delta/1_000_000:10.3f} ms  avgFrameTime: '
                    #       f'{avgFrameTime/1_000_000:10.3f} ms')
                    timeOfLastFrame = currentTime
                if numBytes == 2:
                    uint16_image = array.array('H', flat_image)[:]  # convert byte pairs to uint16
                    image = np.reshape(uint16_image, (imageHeight, imageWidth))  # noqa
                else:
                    image = np.reshape(flat_image, (imageHeight, imageWidth))  # noqa
            except Exception as e:  # noqa
                print(f'Exception: {e}')
                pass

            # We send every frame to the display routine. It will discard frames that arrive too quickly to display.
            droppedFrames = camera.get_dropped_frames()
            GLOBAL['cameraIsRunning'].value = True
            GLOBAL['displayQueue'].put_nowait([frameNumber, droppedFrames,
                                               image, time.perf_counter_ns(),  # noqa (image reference)
                                               avgFrameTime, datetime.datetime.utcnow()])

        if GLOBAL['UTCstartArmed'].value and UTCstartTime is not None:
            currentUTCtime = datetime.datetime.now(timezone.utc)
            if currentUTCtime  > UTCstartTime:  # noqa
                GLOBAL['guiCmdQueue'].put(['disableButtons'])
                currentWriteFrame = 0
                sendImagesToTheWriteQueue = True
                GLOBAL['UTCstartArmed'].value = False
                GLOBAL['guiCmdQueue'].put(['utcButtonGreen'])

        if sendImagesToTheWriteQueue:  # We are writing images to disk
            if currentWriteFrame == 0:  # We are just starting - this is the first image to be written
                GLOBAL['guiCmdQueue'].put(['disableButtons'])
                firstFrameID = frameNumber  # We need firstFrameID to be able to calculate a frame number that is 'write' relative

            if currentWriteFrame == 0:  # At start of recording, turn flash off (should already be off)
                GLOBAL['guiCmdQueue'].put(['flashOFF'])
            elif currentWriteFrame == FLASH_OFF_FRAME_COUNT - 1:  # Turn on first flash
                GLOBAL['guiCmdQueue'].put(['flashON'])
            elif currentWriteFrame == FLASH_FRAMES - 1: # Turn off first flash
                GLOBAL['guiCmdQueue'].put(['flashOFF'])

            elif currentWriteFrame == GLOBAL['numFramesToRecord'].value - 1:  # Turn on terminal flash
                GLOBAL['guiCmdQueue'].put(['flashON'])
            elif currentWriteFrame == GLOBAL['numFramesToRecord'].value + FLASH_ON_FRAME_COUNT - 1: # Turn off terminal flash
                GLOBAL['guiCmdQueue'].put(['flashOFF'])

            GLOBAL['imageWriteQueue'].put([frameNumber - firstFrameID, droppedFrames, image, time.perf_counter_ns(),  # noqa
                                           avgFrameTime, datetime.datetime.utcnow()])
            currentWriteFrame += 1
            # GLOBAL['numFramesWritten'].value = frameNumber - firstFrameID
            if currentWriteFrame >= GLOBAL['numFramesToRecord'].value + FLASH_FRAMES:
                print(f"camProc finished because numFramesToRecord: {GLOBAL['numFramesToRecord'].value}")
                sendImagesToTheWriteQueue = False
                lastFrameID = frameNumber
                # print(f"imageWriteQueue size: {GLOBAL['imageWriteQueue'].qsize()}")
                # print(f"framesToRecord: {GLOBAL['numFramesToRecord'].value}")
                GLOBAL['framesAcquired'].value = lastFrameID - firstFrameID + 1  # noqa (firstFrameID maybe referenced before assignment)

                GLOBAL['guiCmdQueue'].put(['enableButtons'])

                GLOBAL['guiCmdQueue'].put(
                    ['captureReport',
                     f"{GLOBAL['numFramesToRecord'].value + FLASH_FRAMES} images have been captured to RAM.\n\n"
                     f"This includes {FLASH_FRAMES} frames added at the end for the terminating flash.\n\n",
                     f"Dropped frames: {GLOBAL['framesAcquired'].value - (GLOBAL['numFramesToRecord'].value + FLASH_FRAMES)}"
                     ]
                )

        while not GLOBAL['camCmdQueue'].empty():
            try:
                camCmdList = GLOBAL['camCmdQueue'].get()

                camCmd = camCmdList[0]
                if camCmd == 'quit':
                    print('camProc() is shutting down\n')
                    camera.close()
                    keepRunning = False
                elif camCmd == 'getAvgFrameTime':
                    GLOBAL['guiCmdQueue'].put(['avgFrameTime', avgFrameTime/1_000_000])
                elif camCmd == 'startRecording':
                    sendImagesToTheWriteQueue = True
                    currentWriteFrame = 0
                elif camCmd == 'startVideo':
                    imageWidth, imageHeight, binSize, imageType = camera.get_roi_format()
                    if imageType == 0:
                        numBytes = 1
                    elif imageType == 1:
                        numBytes = 3
                    elif imageType == 2:
                        numBytes = 2
                    else:
                        numBytes = 1

                    bufSize = imageWidth * imageHeight * numBytes
                    if not numBytes == 3:
                        buffer = bytearray(np.zeros(bufSize, dtype=np.int8))
                    else:
                        keepRunning = False  # Abort - We don't know how to handle color

                    camera.start_video_capture()
                    resetFrameTimeAverage()
                    cameraIsInVideoCapture = True
                elif camCmd == 'stopVideo':
                    cameraIsInVideoCapture = False
                    camera.stop_video_capture()
                    camera.stop_exposure()
                    timeOfLastFrame = None
                    GLOBAL['cameraIsRunning'].value = False
                elif camCmd == 'settingsDone':
                    GLOBAL['guiCmdQueue'].put(['settingsDone', ''])
                elif camCmd == 'getCameraInfo':
                    values = camera.get_camera_property()
                    GLOBAL['guiCmdQueue'].put(['cameraInfo', values])
                elif camCmd == 'getGain':
                    value = camera.get_control_value(asi.ASI_GAIN)
                    GLOBAL['guiCmdQueue'].put(['gain', value])
                elif camCmd == 'getExposure':
                    value = camera.get_control_value(asi.ASI_EXPOSURE)
                    GLOBAL['guiCmdQueue'].put(['exposure', value])
                elif camCmd == 'getBlackLevel':
                    value = camera.get_control_value(asi.ASI_BRIGHTNESS)
                    GLOBAL['guiCmdQueue'].put(['blackLevel', value])
                elif camCmd == 'getGamma':
                    value = camera.get_control_value(asi.ASI_GAMMA)
                    GLOBAL['guiCmdQueue'].put(['gamma', value])
                elif camCmd == 'getRoiSize':
                    value = camera.get_roi_format()
                    GLOBAL['guiCmdQueue'].put(['roiSize', value])
                elif camCmd == 'getRoiCorner':
                    value = camera.get_roi_start_position()
                    GLOBAL['guiCmdQueue'].put(['roiCorner', value])
                elif camCmd == 'getCameraInfo':
                    value = camera.get_camera_property()
                    GLOBAL['guiCmdQueue'].put(['cameraInfo', value])
                elif camCmd == 'getTemperature':
                    value = camera.get_control_value(asi.ASI_TEMPERATURE)
                    GLOBAL['guiCmdQueue'].put(['temperature', value])
                elif camCmd == 'getDroppedFrames':
                    value = camera.get_dropped_frames()
                    GLOBAL['guiCmdQueue'].put(['droppedFrames', value])
                elif camCmd == 'getBandwidth':
                    value = camera.get_control_value(asi.ASI_BANDWIDTHOVERLOAD)
                    GLOBAL['guiCmdQueue'].put(['bandwidth', value])
                elif camCmd == 'getSpeedMode':
                    value = camera.get_control_value(asi.ASI_HIGH_SPEED_MODE)
                    GLOBAL['guiCmdQueue'].put(['speedMode', value])
                elif camCmd == 'getSDKversion':
                    value = "ASICamera2 SDK 2.9  2023-1-11"
                    GLOBAL['guiCmdQueue'].put(['SDKversion', value])
                elif camCmd == 'getFlipStatus':
                    value = camera.get_control_value(asi.ASI_FLIP)
                    GLOBAL['guiCmdQueue'].put(['flipStatus', value])
                elif camCmd == 'setUTCstartTime':
                    print('UTCstartTime', camCmdList[1])
                    UTCstartTime = camCmdList[1]
                elif camCmd == 'setUSB3speed':
                    # TODO Deal with auto= in all other places
                    camera.set_control_value(control_type=asi.ASI_HIGH_SPEED_MODE, value=camCmdList[1], auto=False)
                    resetFrameTimeAverage()
                elif camCmd == 'setUSB3bandwidth':
                    camera.set_control_value(control_type=asi.ASI_BANDWIDTHOVERLOAD, value=camCmdList[1][0],
                                             auto=camCmdList[1][1])
                    resetFrameTimeAverage()
                elif camCmd == 'setFlip':
                    camera.set_control_value(control_type=asi.ASI_FLIP, value=camCmdList[1])
                elif camCmd == 'setGamma':
                    camera.set_control_value(control_type=asi.ASI_GAMMA, value=camCmdList[1])
                elif camCmd == 'setGain':
                    camera.set_control_value(control_type=asi.ASI_GAIN, value=camCmdList[1][0],
                                             auto=camCmdList[1][1])
                elif camCmd == 'setBlackLevel':
                    camera.set_control_value(control_type=asi.ASI_BRIGHTNESS, value=camCmdList[1])
                elif camCmd == 'setExposureTime':
                    camera.set_control_value(control_type=asi.ASI_EXPOSURE, value=camCmdList[1][0],
                                             auto=camCmdList[1][1])
                    resetFrameTimeAverage()
                elif camCmd == 'setRoiFormat':
                    width = camCmdList[1]
                    height = camCmdList[2]
                    binSize = camCmdList[3]
                    imageType = camCmdList[4]
                    camera.set_roi_format(width=width, height=height, bins=binSize, image_type=imageType)
                    resetFrameTimeAverage()
                elif camCmd == 'setRoiStartPos':
                    x_start = camCmdList[1]
                    y_start = camCmdList[2]
                    camera.set_roi_start_position(start_x=x_start, start_y=y_start)
                else:
                    GLOBAL['guiCmdQueue'].put(['Unexpected/unimplemented camCmd:', camCmd])
            except (ValueError, IndexError, TypeError, asi.ZWO_CaptureError, asi.ZWO_Error, asi.ZWO_IOError) as e1:
                GLOBAL['guiCmdQueue'].put(['cameraException', f'{e1}'])


def guiInit():
    global textlbl, imglabel, canvas, image_container, memoryUsageBar
    global fileProgressBar, memoryUsageLabel, startButton, setUtcButton
    global roiXoffsetScale, roiYoffsetScale, setExposureButton, setGammaButton, setUSB3SpeedButton
    global showCameraSettingsButton, gainEntry, scrubCheckbox
    global canvasFrame, pixelValueLabel, ledIntensity, ledIntensityRange
    global ledCurrentSelector, ledCurrentSelectorLabel, ledIntensityScale, cameraControlInfo

    titleMsg = f"{VERSION}"  # This initial title will be updated once camera name info is available

    gui.title(titleMsg)

    gui_width = 1366
    gui_height = 1200

    monitor_pixel_size = pyautogui.size()  # This returns the native pixel counts
    screenWidth = monitor_pixel_size.width
    screenHeight = monitor_pixel_size.height

    # Some elementary math so that we can position the upper left corner of the gui
    # such the gui center is at the monitor center
    screenYcenter = screenHeight // 2
    screenXcenter = screenWidth // 2
    gui_y_corner = screenYcenter - gui_height // 2
    gui_x_corner = screenXcenter - gui_width // 2

    GLOBAL['guiTopCenterX'] = screenXcenter
    GLOBAL['guiTopCenterY'] = gui_y_corner

    # Size and position the gui at the monitor center with the string that tkinter expects
    gui.geometry(f'{gui_width}x{gui_height}+{gui_x_corner}+{gui_y_corner}')

    gui.update()  # Show the gui

    rowToUse = 1
    font_tuple = ("Arial", 12, "bold")
    framePathEntry = ttk.Entry(gui, textvariable=framePath, state='disabled',
                               font=font_tuple, foreground='green')
    framePathEntry.grid(
        column=1, row=rowToUse, columnspan=2, sticky=tk.E+tk.W,
        padx=(2, 2), pady=(5, 5)
    )
    framePath.set('')
    framePathLabel = ttk.Label(gui, text='FITS filepath pattern')
    framePathLabel.grid(column=0, row=rowToUse, sticky='ne', pady=(5, 5))
    framePathLabel.bind('<Button-3>', showHelpFITSfile)
    framePathEntry.bind('<Button-3>', showHelpFITSfile)

    rowToUse += 1
    selectFolderButton = tk.Button(
        gui, command=processSelectParentFolderButtonClick,
        text='Set FITS parent folder', default='active', bg='lightgray'
    )
    selectFolderButton.grid(column=0, row=rowToUse, sticky=tk.N+tk.E+tk.W, padx=(2, 2))
    selectFolderButton.bind('<Button-3>', showHelpParentFolder)

    setTargetFolderButton = tk.Button(
        gui, command=processSetTargetFolderButtonClick,
        text='Set target folder', default='active', bg='lightgray'
    )
    setTargetFolderButton.grid(column=1, row=rowToUse, sticky=tk.N+tk.E+tk.W, padx=(2, 2))
    setTargetFolderButton.bind('<Button-3>', showHelpTargetFolder)

    rowToUse += 1
    separator1 = tk.Frame(gui, bd=10, relief='raised', height=4, bg='black')
    separator1.grid(column=0, columnspan=2, row=rowToUse, sticky='ew', padx=(4, 2))

    rowToUse += 1
    gainEntry = tk.Button(
        gui, command=askForGain,
        text='Set gain', default='active', bg='lightgray'
    )
    gainEntry.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    gainEntry.bind('<Button-3>', showHelpCameraGain)

    runCameraVideo = tk.Button(
        gui, command=askForVideoOnOff,
        text='Video on/off', default='active', bg='lightgray'
    )
    runCameraVideo.grid(column=0, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    runCameraVideo.bind('<Button-3>', showHelpVideoOnOff)

    rowToUse += 1
    setExposureButton = tk.Button(
        gui, command=askForExposureTime,
        text='Set exposure time', default='active', bg='lightgray'
    )
    setExposureButton.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    setExposureButton.bind('<Button-3>', showHelpExposure)

    showHistogramButton = tk.Button(
        gui, command=askForHistogram,
        text='Show histogram', default='active', bg='lightgray'
    )
    showHistogramButton.grid(column=0, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    showHistogramButton.bind('<Button-3>', showHelpHistogram)


    rowToUse += 1
    setGammaButton = tk.Button(
        gui, command=askForGamma,
        text='Set gamma', default='active', bg='lightgray'
    )
    setGammaButton.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    setGammaButton.bind('<Button-3>', showHelpGamma)

    setUSB3SpeedButton = tk.Button(
        gui, command=askUSB3speed,
        text='Select USB3 speed', default='active', bg='lightgray'
    )
    setUSB3SpeedButton.grid(column=0, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    setUSB3SpeedButton.bind('<Button-3>', showHelpUSB3Speed)

    if not 'HighSpeedMode' in cameraControlInfo.keys():
        setUSB3SpeedButton.config(state='disabled')
        print(f"Disabled USB3 speed button")


    rowToUse += 1
    setBlackLevelButton = tk.Button(
        gui, command=askForBlackLevel,
        text='Set black level', default='active', bg='lightgray'
    )
    setBlackLevelButton.grid(column=1, row=rowToUse, sticky='new', padx=(2, 2), pady=(2, 2))
    setBlackLevelButton.bind('<Button-3>', showHelpBlackLevel)

    setUSB3bandwidthButton = tk.Button(
        gui, command=askForUSB3bandwidth,
        text='Set USB3 bandwidth %', default='active', bg='lightgray'
    )
    setUSB3bandwidthButton.grid(column=0, row=rowToUse, sticky='new', padx=(2, 2), pady=(2, 2))
    setUSB3bandwidthButton.bind('<Button-3>', showHelpUSB3bandwidth)

    rowToUse += 1
    showCameraSettingsButton = tk.Button(
        gui, command=askCameraSettings,
        text='Show camera settings', default='active', bg='lightgray'
    )
    showCameraSettingsButton.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    showCameraSettingsButton.bind('<Button-3>', showHelpShowCameraSettings)

    flipImageButton = tk.Button(
        gui, command=askImageFlip,
        text='Flip image', default='active', bg='lightgray'
    )
    flipImageButton.grid(column=0, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    flipImageButton.bind('<Button-3>', showHelpFlipImage)

    rowToUse += 1

    setBinAndImageTypeButton = tk.Button(
        gui, command=askForBinsAndImageType,
        text='Set bin size, image type, and ROI', default='active', bg='lightgray'
    )
    setBinAndImageTypeButton.grid(column=0, row=rowToUse, columnspan=2, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    setBinAndImageTypeButton.bind('<Button-3>', showHelpSetBinsAndImageType)

    rowToUse += 1
    zoomSelector = ttk.OptionMenu(gui, zoomLevel, '0', '1', '2', '4', '8', '16')
    zoomLevel.set('1')
    zoomLabel = tk.Label(gui, text='Image zoom level:')
    zoomLabel.grid(column=0, row=rowToUse, sticky='ew')
    zoomSelector.grid(column=1, columnspan=1, row=rowToUse, sticky='w', padx=(4, 2))

    rowToUse += 1
    separator2 = tk.Frame(gui, bd=10, relief='raised', height=4, bg='black')
    separator2.grid(column=0, columnspan=2, row=rowToUse, sticky='ew', padx=(4, 2))

    rowToUse += 1
    saveSettingsButton = tk.Button(
        gui, command=saveCameraSettings,
        text='Save settings', default='active', bg='lightgray'
    )
    saveSettingsButton.grid(column=0, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    saveSettingsButton.bind('<Button-3>', showHelpSaveSettings)

    restoreSettingsButton = tk.Button(
        gui, command=restoreCameraSettings,
        text='Restore settings', default='active', bg='lightgray'
    )
    restoreSettingsButton.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    restoreSettingsButton.bind('<Button-3>', showHelpRestoreSettings)

    rowToUse += 1
    separator3 = tk.Frame(gui, bd=10, relief='raised', height=4, bg='black')
    separator3.grid(column=0, columnspan=2, row=rowToUse, sticky='ew', padx=(4, 2))

    rowToUse += 1
    framesToCapture = ttk.Entry(gui, textvariable=frameCount)
    framesToCapture.grid(column=1, row=rowToUse, sticky='new', padx=(2, 2), pady=(2, 2))
    frameCountLabel = ttk.Label(gui, text='Frame Count')
    frameCountLabel.grid(column=0, row=rowToUse, sticky='ne', pady=(1, 2))
    framesToCapture.bind('<Button-3>', showHelpFrameCount)

    rowToUse += 1
    startButton = tk.Button(
        gui, command=processStartButtonClick, bg='red',
        text='Start acquisition', default='active'
    )
    startButton.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    startButtonLabel = ttk.Label(gui, text='Manual start/stop')
    startButtonLabel.grid(column=0, row=rowToUse, sticky='e', padx=(4, 2))
    startButtonLabel.bind('<Button-3>', showHelpManualStart)
    startButton.bind('<Button-3>', showHelpManualStart)

    rowToUse += 1
    utcEntry = ttk.Entry(gui, textvariable=utcSetting)
    utcEntry.grid(column=1, row=rowToUse, sticky='new', padx=(2, 2), pady=(2, 2))
    utcLabel = ttk.Label(gui, text='UTC event time')
    utcLabel.grid(column=0, row=rowToUse, sticky='ne', pady=(1, 2))
    # utcSetting.set('not set')
    utcLabel.bind('<Button-3>', showHelpUTC)
    utcEntry.bind('<Button-3>', showHelpUTC)

    rowToUse += 1
    utcDurEntry = ttk.Entry(gui, textvariable=utcDuration)
    utcDurEntry.grid(column=1, row=rowToUse, sticky='new', padx=(2, 2), pady=(2, 2))
    utcDurLabel = ttk.Label(gui, text='Recording length (secs)')
    utcDurLabel.grid(column=0, row=rowToUse, sticky='ne', pady=(1, 2))
    utcDurLabel.bind('<Button-3>', showHelpUTC)
    utcDurEntry.bind('<Button-3>', showHelpUTC)

    rowToUse += 1
    setUtcButton = tk.Button(
        gui, command=processUTCchange,
        text='Arm UTC start', default='active', bg='lightgray'
    )
    setUtcButton.grid(column=1, row=rowToUse, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    setUtcButton.bind('<Button-3>', showHelpUTC)

    rowToUse += 1
    separator4 = tk.Frame(gui, bd=10, relief='raised', height=4, bg='black')
    separator4.grid(column=0, columnspan=2, row=rowToUse, sticky='ew', padx=(4, 2))

    rowToUse += 1
    fileProgressLabel = ttk.Label(gui, text='File writing progress ...')
    fileProgressLabel.grid(column=0, row=rowToUse, columnspan=2, sticky='nw', pady=(6, 0))
    fileProgressLabel.bind('<Button-3>', showHelpFileWriting)

    rowToUse += 1
    fileProgressBar = ttk.Progressbar(gui, orient=tk.HORIZONTAL, mode='determinate')
    fileProgressBar.grid(column=0, row=rowToUse, columnspan=2, sticky='ew', padx=(4, 2))
    fileProgressBar['value'] = 0
    fileProgressBar.bind('<Button-3>', showHelpFileWriting)

    rowToUse += 1
    memoryUsageLabel = tk.Label(gui, text=f'TBD')
    memoryUsageLabel.grid(column=0, row=rowToUse, columnspan=2, sticky='nw', pady=(6, 0))
    memoryUsageLabel.bind('<Button-3>', showHelpMemoryUsage)

    rowToUse += 1
    memoryUsageBar = ttk.Progressbar(gui, orient=tk.HORIZONTAL, mode='determinate')
    memoryUsageBar.grid(column=0, row=rowToUse, columnspan=2, sticky='ew', padx=(4, 2))
    # memoryUsageBar['value'] = memoryPct
    memoryUsageBar.bind('<Button-3>', showHelpMemoryUsage)
    memUsageReport()


    rowToUse += 1
    separator5 = tk.Frame(gui, bd=10, relief='raised', height=4, bg='black')
    separator5.grid(column=0, columnspan=2, row=rowToUse, sticky='ew', padx=(4, 2))

    rowToUse += 1
    ledCurrentSelector = ttk.OptionMenu(gui, ledIntensityRange, '0', 'High', 'Middle', 'Low',
                                        command=processLedRangeChange)
    ledIntensityRange.set('High')
    ledCurrentSelectorLabel = tk.Label(gui, text='flash LED intensity range:')
    ledCurrentSelectorLabel.grid(column=0, row=rowToUse, sticky='e')
    ledCurrentSelector.grid(column=1, columnspan=1, row=rowToUse, sticky='w', padx=(4, 2))

    rowToUse += 1

    ledIntensityScale = tk.Scale(
        gui, orient='horizontal', from_=0, to=255,   # length=200,
        resolution=1, variable=ledIntensity
    )
    ledIntensityScale.bind("<ButtonRelease-1>", processLedIntensityChange)
    ledIntensityScale.bind("<ButtonRelease-3>", processLedIntensityChange)
    ledIntensityScale.grid(column=0, columnspan=2, sticky='ew', padx=(4, 2))

    rowToUse += 1
    setFlashIntensityButton = tk.Button(
        gui, command=setFlashIntensity,
        text='Set flash intensity', default='active', bg='lightgray'
    )
    setFlashIntensityButton.grid(column=0, row=rowToUse, columnspan=1, sticky=tk.N + tk.E + tk.W, padx=(2, 2))
    setFlashIntensityButton.bind('<Button-3>', showHelpSetFlashIntensity)

    rowToUse += 1
    separator6 = tk.Frame(gui, bd=10, relief='raised', height=4, bg='black')
    separator6.grid(column=0, columnspan=2, row=rowToUse, sticky='ew', padx=(4, 2))

    rowToUse += 1
    spacerLabel1 = ttk.Label(gui, text='')
    spacerLabel1.grid(column=0, columnspan=2, row=rowToUse, sticky='w', pady=(1, 2))

    rowToUse += 1
    helpButton = tk.Button(gui, text='Help', command=showHelp, bg='yellow')
    helpButton.grid(column=0, columnspan=2, row=rowToUse,
                    sticky='ew', padx=(4, 2))

    rowToUse += 1
    spacerLabel2 = ttk.Label(gui, text='')
    spacerLabel2.grid(column=0, columnspan=2, row=rowToUse, sticky='w', pady=(1, 2))

    rowToUse += 1
    pixelValueLabel = ttk.Label(gui, text='Video is off')
    pixelValueLabel.grid(column=0, columnspan=2, row=rowToUse, sticky='w', pady=(1, 2))

    rowToUse += 1
    gui.rowconfigure(rowToUse, weight=1)


    # Add contrast controls to right-hand side of GUI
    blackContrast = tk.Scale(
        gui, orient='vertical', from_=1.0, to=0.0, length=200,
        resolution=0.05, variable=contrastLow
    )
    blackContrastLabel = ttk.Label(gui, text='Black\nlevel')
    blackContrastLabel.grid(column=3, row=2, rowspan=2, sticky='n')
    blackContrast.grid(column=3, row=4, rowspan=10,  sticky='n')
    blackContrast.bind('<Button-3>', showHelpBlackLevelContrast)
    blackContrastLabel.bind('<Button-3>', showHelpBlackLevelContrast)

    whiteContrast = tk.Scale(
        gui, orient='vertical', from_=1.0, to=0.0, length=200,
        resolution=0.05, variable=contrastHigh
    )
    whiteContrastLabel = ttk.Label(gui, text='White\nlevel')
    whiteContrastLabel.grid(column=4, row=2, rowspan=2, sticky='n')
    whiteContrast.grid(column=4, row=4, rowspan=10, sticky='n')
    contrastHigh.set(1.0)
    whiteContrast.bind('<Button-3>', showHelpWhiteLevelContrast)
    whiteContrastLabel.bind('<Button-3>', showHelpWhiteLevelContrast)

    canvasFrame = ttk.Frame(gui)
    canvasFrame.grid(column=2, row=2, rowspan=99, sticky='ewns', padx=(4, 4), pady=(0, 8))
    canvasFrame.bind('<Button-3>', showHelpImageDisplay)

    gui.columnconfigure(2, weight=1)


    gui.update()  # update TCL tasks to make window appear

def disableLEDintensityControls():
    global ledCurrentSelector, ledCurrentSelectorLabel, ledIntensityScale

    ledCurrentSelector.config(state='disabled')
    ledIntensityScale.config(state='disabled')

def show_scrollable_list(width=750, height=250, lines=['Line 1', 'Line 2'], title='ScrolledText Widget'):  # noqa mutable argument

    top = tkinter.Toplevel(gui)
    top.withdraw()  # Even with this call, there is a flash of the widget at the upper left of monitor
    center_x = GLOBAL['guiTopCenterX'] - width // 2
    center_y = GLOBAL['guiTopCenterY'] + 40
    top.geometry(f'{width}x{height}+{center_x}+{center_y}')
    top.title(title)
    # top.attributes("-topmost", True)   # This keeps the widget on top of everything permanently
    # Place the toplevel window at the top
    top.wm_transient(gui)

    text_area = scrolledtext.ScrolledText(top, wrap = tk.WORD, width = width, height = height,
                                          font = ("Fixed Width", 10)
                                          )
    text_area.pack(padx=10, pady=10)
    for line in lines:
        if not line.endswith('\n'):
            line += '\n'
        text_area.insert(tk.INSERT, line)

    # Make the text read only ...
    text_area.configure(state='disabled')
    top.deiconify()  # undo the withdraw()
    top.update()

def showHelp():
    showInfo('Reminder about right-click-for-help',
             f'All widgets have an associated\n'
             f'help message that will pop-up if you\n'
             f'right-click on the widget.')


def showHelpTargetFolder(event):  # noqa (event not used)
    showInfo('Set target folder',
             f"Clicking this button brings up a dialog box that\n"
             f"asks for the name of the target folder to be used\n"
             f"for storing the sequence of FITS files that will\n"
             f"result from the frame acquisition process.\n\n"
             f"A folder name should encode date of observation,\n"
             f"target star, and asteroid name.\n\n"
             f"If this folder does not yet exist, it will be created.\n\n"
             f"If the folder already exists and has FITS file\n"
             f"already present, you will have the option of\n"
             f"erasing the FITS files or cancelling.\n\n"
             f"You are also given an opportunity to specify the\n"
             f"prefix to be used in naming the sequence of\n"
             f"FITS files. If the folder name encodes the date\n"
             f"of observation, target star, and asteroid name,\n"
             f"you can give a simple prefix, such as the asteroid name.\n\n"
             f"Ending this string with a dash (-) is recommended.")


def showHelpParentFolder(event):  # noqa (event not used)
    showInfo('Set FITS parent folder',
             f"Clicking this button brings up a 'Select Directory'\n"
             f"dialog which you can use to navigate to the folder\n"
             f"to be used as the parent folder.\n\n"
             f"Note: The parent folder must already exist.\n\n"
             f"'Target folders', which is where the sequence of\n"
             f"FITS files will be written, are nested inside this\n"
             f"'parent folder")


def showHelpFITSfile(event):  # noqa (event not used)
    showInfo('FITS folder to be written',
             f"The is a read-only display of the folder in which the\n"
             f"FITS files resulting from image acquisition will be\n"
             f"stored.\n\n"
             f"This path gets created as a result of clicking on the\n"
             f"'Set FITS parent folder' button and the \n"
             f"'Set target folder' button.\n\n"
             f"The folder structure is:\n\n"
             f"   <FITS parent folder>\n"
             f"    --- <target folder 1>   (contains FITS files)\n"
             f"    --- <target folder 2>\n"
             f"            .\n"
             f"            .\n"
             f"    --- <target folder n>\n\n"
             f"Note: The FITS parent folder is 'sticky' and will be used\n"
             f"the next time this app is run. So usually it will be only\n"
             f"necessary to set/select a new target folder for the next run.")


def showHelpBlackLevelContrast(event):  # noqa (event not used)
    showInfo('Black level (contrast control',
             f"In the image display to the left, displayed pixels\n"
             f"have values in the range of 0 to 255.\n\n"
             f"This slider, together with its mate, the White\n"
             f"level slider, is used to remap (zoom) the real\n"
             f"pixel value to different display values\n"
             f"by expanding pixel values between the Black\n"
             f"level and White level to the display range\n"
             f"of 0 to 255.\n\n"
             )


def showHelpWhiteLevelContrast(event):  # noqa (event not used)
    showInfo('White level (contrast control',
             f"In the image display to the left, displayed pixels\n"
             f"have values in the range of 0 to 255.\n\n"
             f"This slider, together with its mate, the Black\n"
             f"level slider, is used to remap (zoom) the real\n"
             f"pixel value to different display values\n"
             f"by expanding pixel values between the Black\n"
             f"level and White level to the display range\n"
             f"of 0 to 255.\n\n"
             )


def showHelpFrameCount(event):  # noqa (event not used)
    showInfo('Frame count',
             f"For manual control of acquisition, this entry must\n"
             f"be filled in.\n\n"
             f"If UTC scheduling of acquisition is in use, the proper\n"
             f"frame count to use will be calculated from the Duration (secs)\n"
             f"value and the exposure time and placed in the box")

def showHelpSetLedLevel(event):  # noqa (event not used)
    showInfo('Set flash LED intensity',
             f"TBD")

def showHelpUTC(event):  # noqa (event not used)
    showInfo('UTC scheduling',
             f"Frame acquisition can be scheduled to begin at a future UTC\n"
             f"time using UTC start time and Duration (secs)\n"
             f"entry boxes.\n\n"
             f"If you leave the UTC time entry blank, you can run a simple\n"
             f"test of this feature by answering Yes to the dialog that pops up.\n\n"
             f"The format for UTC start time is:\n\n"
             f"\tyyyy-mm-dd hh:mm\n"
             f"\texample: 2022-4-19 13:52\n\n"
             f"\tyyyy-mm-dd hh:mm:ss\n"
             f"\texample: 2023-11-27 3:5:9\n\n"
             f"Fill in the values that you want used, then click the\n"
             f"'Arm UTC start' button to activate (arm) the schedule. The\n"
             f"button will turn yellow to indicate that the 'arming' was successful.\n\n"
             f"UTC time will be taken from the computer clock BUT if\n"
             f"a 'timestamper' is providing GPS accurate time, you will\n"
             f"be given an opportunity to set the computer clock to match.\n"
             f"It would be good practice to accept whenever the \n"
             f"differences are small.\n\n"
             f"If UTC start is armed (the button is yellow), clicking the button\n"
             f"will cancel the scheduled acquisition.")


def showHelpManualStart(event):  # noqa (event not used)
    showInfo('Manual ctrl start button',
             f"When this button is red, it means that no acquisition\n"
             f"is in progress. Clicking this button now will cause\n"
             f"acquisition to start (even if a UTC timed start\n"
             f"has been specified).\n\n"
             f"NOTE: Any FITS files present in the target folder\n"
             f"      will be deleted !!\n\n"
             f"If this button is green, acquisition of frames into RAM\n"
             f"is in progress. Clicking this button now will\n"
             f"terminate (early) the acquisition whether the acquisition\n"
             f"was started manually or by UTC time.")

def showHelpVideoOnOff(event):  # noqa (event not used)
    showInfo('Video On/Off',
             f"This is (likely) only used during development.")
def showHelpCameraGain(event):  # noqa (event not used)
    global cameraControlInfo

    max_gain = cameraControlInfo['Gain']['MaxValue']
    min_gain = cameraControlInfo['Gain']['MinValue']
    # TODO Check the claim that gain can't be changed in video mode
    showInfo('Camera gain',
             f"Camera gain must be in the range {min_gain} to {max_gain}\n\n"
             f"NOTE: It is not possible to change gain setting while\n"
             f"acquisition is in progress. The button is disabled.")


def showHelpExposure(event):  # noqa (event not used)
    showInfo('Exposure time',
             f"Exposure times must be specified in milliseconds.\n\n\n"
             f"The program will calculate the USB3 traffic that\n"
             f"will be produced at the resulting frame rate, taking\n"
             f"into account the ROI size and whether it is an\n"
             f"8 bit or a 16 bit recording.\n\n")
def showHelpHistogram(event):  # noqa (event not used)
    showInfo('Histogram',
             f"Used to show the effect of Black Level setting as an \n"
             f"aid to choosing the proper value.\n\n")
def showHelpUSB3Speed(event):  # noqa (event not used)
    showInfo('USB3 speed',
             f"With some ZWO cameras, the USB3 system can be used at a normal speed and an enhanced speed.\n\n"
             f"For those cameras, we provide the option of using the higher speed.\n\n"
             f"This button is disabled if the camera model in use does need/provide this option.\n")

def showHelpGamma(event):  # noqa
    # TODO Check about the claim that gamma can't be changed while in video mode
    showInfo('Gamma',
             f"gamma_level controls gamma and can be set anywhere in the range 1 to 100\n\n"
             f"A gamma_level of 50 corresponds to a gamma of 1.0\n\n"
             f"For recording an occultation of a very dim star, it can\n"
             f"be useful to set gamma_level to values less than 50. (Tests\n"
             f"have shown that this improves event detectability.)\n\n"
             f"If it is important to get better estimates of\n"
             f"magDrop, set gamma_level to 50\n\n"
             f"Note: it is not possible to change gamma values during\n"
             f"acquisition. The button is disabled.\n"
             )

def showHelpSaveSettings(event):  # noqa (event not used)
    showInfo('Save camera settings',
             f"Use this button to save the current camera settings to file.\n\n"
             f"A file name and location dialog will apear with the default directory "
             f"preset to the current working directory (where src is executed from).\n\n"
             f"All such files have a forced extension of .zwo_cam_set")

def showHelpRestoreSettings(event):  # noqa (event not used)
    showInfo('Restore camera settings',
             f"Use this button to retrieve a saved camera settings file and use those settings "
             f"to reconfigure the camera.\n\n"
             f"Only files with the extension .zwo_cam_set can be used (this is enforced when camera settings "
             f"are saved.")
def showHelpUSB3bandwidth(event):  # noqa (event not used)
    showInfo('USB3 bandwidth utilization',
             f"Set the percentage of available USB3 bandwidth that the camera will attempt to use.")
def showHelpBlackLevel(event):  # noqa (event not used)
    # TODO Fix this help message - it's wrong for ZWO
    showInfo('Black level',
             f"Black level can be set in the range of -5 % to +10 %\n\n"
             f"The camera adds this value to the results of the\n"
             f"A/D conversion for each pixel and then sets any\n"
             f"results that are less than zero to zero - i.e., it clips\n"
             f"at zero. It also clips values that exceed the value\n"
             f"that corresponds to the pixel bit depth max value\n"
             f"by setting all such results to the max value.\n\n"
             f"src defaults this value to 10% because it allows\n"
             f"the background noise to be properly measured. While\n"
             f"this is good for occultations, for just capturing\n"
             f"astronomical photos, darker backgrounds can be achieved\n"
             f"by setting this value lower, or even negative.\n\n"
             f"Note: it is not possible to change black levels during\n"
             f"acquisition. The button is disabled.")

def showHelpSetRoi(event):  # noqa (event not used)
    showInfo('Set ROI',
             f"Set the Region Of Interest (ROI) by entering either of the following strings.\n\n"
             f"To place a centered ROI, use this format: 640 x 480\n\n"
             f"To place the ROI at an upper left corner: 800 x 640 @ 100 100\n\n"
             f"Note: the x dimension must be a multiple of 8 and the y dimension a multiple of 2\n\n"
             f"Note: the corner position is relative to the image after binning.")

def showHelpSetFlashIntensity(event):  # noqa (event notused)
    showInfo('Set flash intensity',
             f"After you have selected the flash LED intensity range and positioned the intensity\n"
             f"slider until the LED brightness is at approximately 50% of saturation, click\n"
             f"this button to save those setting for use when timing flashes are\n"
             f"added during observation recording.")
def showHelpSetBinsAndImageType(event):  # noqa (event not used)
    showInfo('Set bin size, image type, and ROI',
             f"The selection of bin size and image type (8 or 16 bit) must be made "
             f"whenever a new ROI is to be specified. That is why three dialogs appear in "
             f"sequence - to gather the needed selection values.\n\n"
             f"Set the Region Of Interest (ROI) by entering either of the following strings.\n\n"
             f"To place a centered ROI, use this format: 640 x 480\n\n"
             f"To place the ROI at an upper left corner: 800 x 640 @ 100 100\n\n"
             f"Note: the x dimension must be a multiple of 8 and the y dimension a multiple of 2\n\n"
             f"Note: the corner position is relative to the image after binning.")
def showHelpFlipImage(event):  # noqa (event not used)
    showInfo('Flip image',
             f"The image coming from the camera can be flipped around the "
             f"vertical axis (left/right flip), the horizontal axis "
             f"(top/bottom flip), or both.\n\n"
             f"This is typically used to undo something in the "
             f"optics path that produces an unwanted image flip.\n\n"
             f"The 'flipped' image will be written to the output files.")
def showHelpShowCameraSettings(event):  # noqa (event not used)
    # TODO Finish/expand this cryptic help
    showInfo('Show Camera Settings',
             f"Shows current camera settings in scrollable list.")

def showHelpMemoryUsage(event):  # noqa (event not used)
    showInfo('System memory usage',
             f"src uses system RAM to temporarily store images\n"
             f"captured from the camera. These memory images are\n"
             f"written to disk as quickly as possible as FITS files.\n\n"
             f"For high frame rates and/or large image ROIs and 16-bit\n"
             f"pixel depths, the disk writing can fall behind image\n"
             f"acquisition and system RAM usage will then grow until\n"
             f"the requested number of frames have been grabbed\n"
             f"from the camera. This is usually a good thing, but\n"
             f"there is always the possibility that system RAM\n"
             f"will be exhausted with unknown consequences.\n\n"
             f"src protects against this situation by\n"
             f"terminating frame captures if system RAM usage\n"
             f'exceeds 90%.')

def showHelpFileWriting(event):  # noqa (event not used)
    showInfo('Frame writing progress bar',
             f"This progress bar shows the percentage (0 - 100)\n"
             f"of requested frames that have been written to disk.\n\n"
             f"Since src buffers captured image into system RAM,\n"
             f"it is common for the requested number of frames\n"
             f"to have been captured into system RAM but not yet\n"
             f"written as FITS files to disk.\n\n"
             f"Because of this, take care not to close this program\n"
             f"until it reports that all files have been written.\n\n"
             f"This progress bar will let you see what's happening.")


def showHelpImageDisplay(event):  # noqa (event not used)
    showInfo('Image display window',
             f"This image display window has fixed dimensions of \n"
             f"960(W) x 720(H).\n\n"
             f"If the image ROI W x H you selected fits within this area,\n"
             f"the image will be shown in its entirety with the\n"
             f"upper left corner origin set at x=0, y=0\n\n"
             f"Images larger than 960 x 720 are cropped\n"
             f"(only for the display - the entire image\n"
             f"gets written to the file).\n\n"
             f"If the image is cropped, you can control the\n"
             f"origin coordinates with the 'Image X origin' and\n"
             f"'Image Y origin' sliders They allow one to \n"
             f"'scroll' the image so that all regions can be examined.")


# def showHelpRoiXoffset(event):  # noqa (event not used)
#     showInfo('ROI X offset',
#              f"If you select an image format (ROI) that is smaller\n"
#              f"than the native pixel array, this smaller ROI is by default\n"
#              f"centered on the larger native array.\n\n"
#              f"In that case, this control allows you choose a\n"
#              f"a different X position for the ROI.\n\n"
#              f"If this control won't move, it's because the ROI\n"
#              f"is equal to the native pixel array,")


# def showHelpRoiYoffset(event):  # noqa (event not used)
#     showInfo('ROI Y offset',
#              f"If you select an image format (ROI) that is smaller\n"
#              f"than the native pixel array, this smaller ROI is by default\n"
#              f"centered on the larger native array.\n\n"
#              f"In that case, this control allows you choose a\n"
#              f"a different Y position for the ROI.\n\n"
#              f"If this control won't move, it's because the ROI\n"
#              f"is equal to the native pixel array,")


def showHelpImageXoffset(event):  # noqa (event not used)
    showInfo('Image X origin',
             f"When an image won't fit in the 960 x 720\n"
             f"display area, it is cropped (just for display purposes)\n"
             f"to fit. This slider controls the left edge of that crop.\n\n"
             f"If this slider won't move, it is because the image size\n"
             f"selected fits in the 960 x 720 display area.\n\n"
             f"Note: Images written to files are never cropped."
             )


def showHelpImageYoffset(event):  # noqa (event not used)
    showInfo('Image Y origin',
             f"When an image won't fit in the 960 x 720\n"
             f"display area, it is cropped (just for display purposes)\n"
             f"to fit. This slider controls the top edge of that crop.\n\n"
             f"If this slider won't move, it is because the image size\n"
             f"selected fits in the 960 x 720 display area.\n\n"
             f"Note: Images written to files are never cropped."
             )

def showHelpScrubImage(event):  # noqa (event not used)
    showInfo('Scrub image checkbox',
             f"'outlaw pixels' refers to pixels that are stuck at bright\n"
             f"(a hot pixel), or sparkle (fluctuating gain), or do\n"
             f"not respond to light (dark pixels).\n\n"
             f"PyMovie is used to calculate 'outlaw pixel' lists. It\n"
             f"needs a dark field recording at full ROI (1440 x 1080), \n"
             f"max gain, gamma 1.0, and black level 10%. 16 bit \n"
             f"resolution is needed and 100 frames at 1 fps is\n"
             f"recommended. The 1 second exposure helps detect 'sparklers'\n\n"
             f"Scrubbing must be turned off (because recordings\n"
             f"include the effect of scrubbing).\n\n"
             f"Once PyMovie has extracted the 'outlaw pixel' list,\n"
             f"the list must be placed in the directory where \n"
             f"the CameraCapture python script is stored and \n"
             f"most importantly, named: BFS-U3-16S2.\n\n"
             f"If an 'outlaw pixel' list is present, checking this box\n"
             f"will cause each displayed image to be 'scrubbed'.\n\n"
             f"The 'scrubbing' process replaces each 'outlaw pixel'\n"
             f"value with the average of its 8 neighbors. These 8\n"
             f"neighbors are highly likely to be 'healthy', so their\n"
             f"average value is a good/valid replacement value to use.\n\n"
             f"A full 1440 x 1080 'outlaw pixel' list is REQUIRED !!!\n\n"
             )

def processUTCchange():

    if GLOBAL['UTCstartArmed'].value:  # This is a 'cancel' request click
        GLOBAL['UTCstartArmed'].value = False
        setUtcButton.config(bg='lightgray', text='Arm UTC start')
        return

    if flashOnCmdString is None or flashOnCmdString == '':
        showInfo('Setup error',
                 f"\nflash intensity has not been set yet.\n\n\n\n\n\n")
        return

    if fitsFolderPath == "":
        showInfo('Error !!!',
                 f"There is no folder for the FITS files assigned yet.\n\n"
                 f"Use the 'Set FITS parent folder' button and the\n"
                 f"'Set target folder' button to declare the correct path.\n\n")
        return

    try:
        duration = float(utcDuration.get())
    except Exception as err:
        showInfo("Format error in duration", f"{err}")
        return

    if duration <= 0.0:
        showInfo('Error !!!',
                 f"A non-zero duration must be specified before a UTC event time can be processed.\n\n"
                 f"That's because we need that time to properly calculate the start time for the recording from the "
                 f"given event time.\n\n")
        return

    # If a UTC triggered acquisition is scheduled, we test for FITS
    # files are already present in the target folder
    fitsFilesFound = glob.glob(f'{saveFolderRoot}/{folderName}/*.fits')
    numFitsFilesFound = len(fitsFilesFound)
    if numFitsFilesFound > 0:
        msg = (f"{numFitsFilesFound} FITS files are already present in the target folder.\n\n"
               f"Do you wish to delete them?")
        answer = tk.messagebox.askyesno('Confirmation required', msg)
        if answer:  # User requests deletion of the fits files
            for fname in fitsFilesFound:
                os.remove(fname)
        else:
            # Return without arming UTC start
            GLOBAL['UTCstartArmed'].value = False
            setUtcButton.config(bg='lightgray', text='Arm UTC start')

            return

    UTCgiven = utcSetting.get()
    if UTCgiven == '':
        msg = (f"Do you want to run a short test where \n"
               f"the UTC start time is set 15 seconds from now?")
        answer = tk.messagebox.askyesno('UTC start test case', msg)
        if answer:
            timeAdvanced = datetime.datetime.now(timezone.utc) + datetime.timedelta(milliseconds=15000)
            clippedTimeStr = str(timeAdvanced).split('.')[0]  # Get rid of fractional seconds
            utcSetting.set(clippedTimeStr)
            UTCgiven = clippedTimeStr
            GLOBAL['camCmdQueue'].put(['setUTCstartTime', None])
        else:
            pass

    if not UTCgiven.endswith('Z'):
        UTCgiven += 'Z'

    try:
        UTCstartTime = parser.parse(UTCgiven)
        # Interpret the UTC time given as the UTC time of the event. To do this,
        # we subtract one half of the duration provided
        UTCstartTime = UTCstartTime - datetime.timedelta(seconds=duration/2.0)
    except Exception as err:
        showInfo("Error in UTC start time format", f"{err}")
        setUtcButton.config(bg='lightgray', text='Arm UTC start')
        return

    UTCnow = datetime.datetime.now(timezone.utc)

    if UTCnow >= UTCstartTime:
        showInfo("Error", "The combination of UTC event time and duration results in"
                          " a start time that is in the past.\n\n")
        setUtcButton.config(bg='lightgray', text='Arm UTC start')
        return
    else:
        timeDelta = UTCstartTime - UTCnow
        msg = (f"You have scheduled an observation recording start time that is\n"
               f"in the future by\n\n"
               f"\t{timeDelta} seconds\n\n"
               f"Is that okay?")
        answer = tk.messagebox.askyesno("Confirm start time", msg)
        if not answer:
            setUtcButton.config(bg='lightgray', text='Arm UTC start')
            return


    print(cameraState['exposure'][0] / 1_000_000)  # TODO Remove this print
    print(type(UTCstartTime),UTCstartTime)

    numberOfFrames = int(duration / (cameraState['exposure'][0] / 1_000_000))
    msg = (f"Given the specified duration and exposure time,\n"
           f"{numberOfFrames} frames will be acquired.\n\n"
           f"Is that okay?")
    answer = tk.messagebox.askyesno("Confirm number of frames", msg)
    if not answer:
        setUtcButton.config(bg='lightgray', text='Arm UTC start')
        return

    GLOBAL['UTCstartArmed'].value = True
    GLOBAL['numFramesToRecord'].value = numberOfFrames

    # We let camProc set 'frameNumberWritten' to 0 (to start the recording) when UTCstart is exceeded
    GLOBAL['numFramesWritten'].value = -1
    frameCount.set(f'{numberOfFrames}')

    GLOBAL['camCmdQueue'].put(['setUTCstartTime', UTCstartTime])

    setUtcButton.config(bg='yellow', text='UTC start armed')

def askForROI():
    global lastROIinputString, imageZoomScroller

    if not binSizeSet or not imageTypeSet:
        showInfo('Setup error', f"The pair, bin size and image type, have not yet been set.\n\n"
                                f"That is needed for setting up the ROI.")
        return

    if lastROIinputString == '':
        lastROIinputString = f"{cameraState['currentImageWidth']} x {cameraState['currentImageHeight']}"
    roi_str = simpledialog.askstring(
        title='ROI entry',
        prompt=f'Enter ROI with corner at x,y like:\t1024 x 720 @ x = 100 y = 200\t\t\n'
               f'or for centered ROI: \t\t1200 x 800\n\n'
               f'Note: corner values are relative to the binned image!',
        initialvalue=lastROIinputString)
    if roi_str is None or roi_str == '':
        return
    else:
        lastROIinputString = roi_str
        format_ok, x_size, y_size, x_corner, y_corner = parseROIstring(roi_str)

        if format_ok:
            values_ok, msg = validateRoiRequest(x_size, y_size, x_corner, y_corner)
            if not values_ok:
                showInfo('ROI value error', f'{msg}')
                return False
            else:
                cameraState['currentImageWidth'] = x_size
                cameraState['currentImageHeight'] = y_size
                if x_corner is not None:
                    cameraState['xOrigin'] = x_corner
                if y_corner is not None:
                    cameraState['yOrigin'] = y_corner
                return True

def validateRoiRequest(x_size, y_size, x_corner, y_corner):
    bin_size = cameraState['binSize']  # noqa
    sensor_x_size = cameraState['maxImageWidth']
    sensor_y_size = cameraState['maxImageHeight']

    if not x_size % 8 == 0:
        return False, 'ROI x dimension must be a multiple of 8'
    if not y_size % 2 == 0:
        return False, 'ROI y dimension must be a multiple of 2'
    if x_size < 0 or y_size < 0:
        return False, 'ROI size parameters must be positive values'

    if x_corner is not None:
        if x_corner < 0:
            return False, 'ROI x corner cannot be negative'
    if y_corner is not None:
        if y_corner < 0:
            return False, 'ROI y corner cannot be negative'

    if x_size > sensor_x_size / bin_size:
        return False, f'The ROI x size is greater than the sensor x size of {sensor_x_size} at bin size {bin_size}'
    if y_size > sensor_y_size / bin_size:
        return False, f'The ROI y size is greater than the sensor y size of {sensor_y_size} at bin size {bin_size}'

    if x_corner is not None:
        if not x_corner % 8 == 0:
            return False, 'The x corner position must be a factor of 8'
        if (x_corner + x_size) > (sensor_x_size / bin_size):
            return False, 'The x corner position puts part of the ROI outside the sensor area'
    if y_corner is not None:
        if not y_corner % 2 == 0:
            return False, 'The y corner position must be a factor of 2'
        if (y_corner + y_size) > (sensor_y_size / bin_size):
            return False, 'The y corner position puts part of the ROI outside the sensor area'

    return True, 'values are valid'

def parseROIstring(roi_str):

    # Get set for an exit at any time
    x_size = y_size = x_corner = y_corner = None
    format_ok = False

    while True:  # We use a break to jump to the exit
        if '@' in roi_str or '=' in roi_str:
            # print('Parsing an ROI with corner specified')
            parts = roi_str.split('@')
            if len(parts) == 2:
                # print('... valid number of @ symbols')
                left_side = parts[0]
                right_side = parts[1]
                parts = left_side.split('x')
                if len(parts) == 2:
                    # print('left_side format ok')
                    x_size_str = parts[0]
                    y_size_str = parts[1]

                    try:
                        x_size = int(x_size_str)
                    except ValueError as e1:
                        showInfo('Value error', f'{e1}')
                        break

                    try:
                        y_size = int(y_size_str)
                    except ValueError as e1:
                        showInfo('Value error', f'{e1}')
                        break

                    # print(f'|{x_size_str}|={int(x_size_str)}  |{y_size_str}|={int(y_size_str)}')
                    parts = right_side.split('=')
                    if len(parts) == 3:
                        if 'x' in parts[0] and 'y' in parts[1]:
                            # print('right_side format ok')
                            # print(f'|{parts[1]}|  |{parts[2]}|={int(parts[2])}')
                            x_str = parts[1].split('y')[0]
                            try:
                                x_corner = int(x_str)
                            except ValueError as e1:
                                showInfo('Value error', f'{e1}')
                                break
                            try:
                                y_corner = int(parts[2])
                            except ValueError as e1:
                                showInfo('Value error', f'{e1}')
                                break
                            # print(f'|{x_str}|={x_corner}  |{parts[2]}|={y_corner}')
                            format_ok = True
                            cameraState['currentImageWidth'] = x_size
                            cameraState['currentImageHeight'] = y_size
                            cameraState['xOrigin'] = x_corner
                            cameraState['yOrigin'] = y_corner
                            break
                    else:
                        # print('right_side has wrong format')
                        pass
                else:
                    # print('left_side has wrong format' )
                    pass
            else:
                # print('... more than 1 @ symbol found')
                pass
        else:
            # We are processing a centered ROI. We will have to calculate the x and y corners
            # print('Parsing a centered ROI')
            left_side = roi_str
            parts = left_side.split('x')
            if len(parts) == 2:
                # print('left_side format ok')
                x_size_str = parts[0]
                y_size_str = parts[1]

                try:
                    x_size = int(x_size_str)
                except ValueError as e1:
                    showInfo('Value error', f'{e1}')
                    break

                try:
                    y_size = int(y_size_str)
                except ValueError as e1:
                    showInfo('Value error', f'{e1}')
                    break

                # print(f'|{x_size_str}|={x_size}  |{y_size_str}|={y_size}')
                format_ok = True
                break

    return format_ok, x_size, y_size, x_corner, y_corner

def askUSB3speed():
    dlg = USB3SpeedDialog(gui, title="USB3 speed")
    answer = dlg.result
    if answer is None:
        return
    elif answer == 'High':
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['stopVideo'])
            # while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
            #     pass
        GLOBAL['camCmdQueue'].put(['setUSB3speed', 1])
        # while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
        #     pass
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['startVideo'])
        cameraState['speedMode'] = 1
    elif answer == 'Normal':
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['stopVideo'])
            # while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
            #     pass
        GLOBAL['camCmdQueue'].put(['setUSB3speed', 0])
        # while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
        #     pass
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['startVideo'])
        cameraState['speedMode'] = 0
    else:
        showInfo('Program error',
                 f"Unexpected answer returned by USB3SpeedDialog: {answer}")

def askForGamma():

    # The tabs at the end of the prompt make the widget wide enough to show the title properly
    level = simpledialog.askinteger(title='ZWO gamma level (1...100)',
                                    initialvalue=cameraState['gamma'],
                                    prompt='Enter gamma level:\t\t\t\t\t')
    if level is None:
        return
    elif 1 <= level <= 100:
        GLOBAL['camCmdQueue'].put(['setGamma', level])
        cameraState['gamma'] = level
    else:
        showInfo('Out of range error',
                 f'The ZWO "gamma level" must be between 1 and 100 inclusive.\n\n'
                 f'A level of 50 corresponds to the normal gamma = 1.0\n\n')

def askForBinsAndImageType():
    global binSizeSet, bin_size, imageTypeSet, image_type, imageZoomScroller

    bin_size = cameraState['binSize']
    image_type = cameraState['imageType']

    binSizeSet = True
    imageTypeSet = True

    gui.update()  # This solved an issue - the following simpledialog was appearing under the gui
    if not askForROI():
        return

    bin_size = cameraState['binSize']  # noqa
    sensor_x_size = cameraState['maxImageWidth']
    sensor_y_size = cameraState['maxImageHeight']
    x_size = cameraState['currentImageWidth']
    y_size = cameraState['currentImageHeight']
    x_corner = cameraState['xOrigin']
    y_corner = cameraState['yOrigin']

    # The tabs at the end of the prompt make the widget wide enough to show the title properly
    gui.update()  # This solved an issue - the following simpledialog was appearing under the gui
    new_bin_size = simpledialog.askinteger(title='Binning size',
                                       prompt='Enter bin size:\t\t\t\t\t', initialvalue=cameraState['binSize'])
    if new_bin_size is None:
        pass
    elif new_bin_size in cameraInfoDict['SupportedBins']:
        bin_size = new_bin_size
        if x_size > sensor_x_size / bin_size:
            showInfo('Parameter size error',
                     f'The ROI x size is greater than the sensor x size of {sensor_x_size} at bin size {bin_size}\n\n'
                     f'sensor width / bin size = {sensor_x_size // bin_size}')
            return
        if y_size > sensor_y_size / bin_size:
            showInfo('Parameter size error',
                     f'The ROI y size is greater than the sensor y size of {sensor_y_size} at bin size {bin_size}\n\n'
                     f'sensor height / bin size = {sensor_y_size // bin_size}')
            return

        if x_corner is not None:
            if not x_corner % 8 == 0:
                showInfo('Parameter size error',
                         'The x corner position must be a factor of 8')
                return
            if (x_corner + x_size) > (sensor_x_size / bin_size):
                showInfo('Parameter size error',
                         'The x corner position puts part of the ROI outside the sensor area')
                return
        if y_corner is not None:
            if not y_corner % 2 == 0:
                showInfo('Parameter size error',
                         'The y corner position must be a factor of 2')
                return
            if (y_corner + y_size) > (sensor_y_size / bin_size):
                showInfo('Parameter size error',
                         'The y corner position puts part of the ROI outside the sensor area')
                return

        cameraState['binSize'] = bin_size
        cameraState['xOrigin'] = x_corner
        cameraState['yOrigin'] = y_corner

        # Now we can ask for image type
        # First we prepare a list of type names supported by this camera
        video_types = cameraInfoDict['SupportedVideoFormat']
        video_type_names = []
        for type_code in video_types:
            if type_code == 0:
                video_type_names.append('enter 0 for RAW8')
            elif type_code == 1:
                video_type_names.append('enter 1 for RGB24')
            elif type_code == 2:
                video_type_names.append('enter 2 for RAW16')
            elif type_code == 3:
                video_type_names.append('enter 3 for Y8')
            elif type_code == -1:
                pass
            else:
                showInfo('System error',
                         f"Unexpected ASI_IMAGE_TYPE of {type_code} found")
                pass

        gui.update()  # This solved an issue - the following simpledialog was appearing under the gui
        title = f'{video_type_names}'
        new_image_type = simpledialog.askinteger(title=title,
                                             prompt='Enter image type number:\t\t\t\t\t\t\t',
                                             initialvalue= cameraState['imageType'])
        if new_image_type is None:
            pass
        elif image_type in video_types:
            cameraState['imageType'] = new_image_type
        else:
            showInfo('Invalid setting',
                     f"{image_type} is not an image type number that is supported by this camera.")
            return

        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['stopVideo'])
            while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
                pass
        GLOBAL['camCmdQueue'].put(['setRoiFormat', cameraState['currentImageWidth'],
                                   cameraState['currentImageHeight'], cameraState['binSize'],
                                   cameraState['imageType']])
        GLOBAL['camCmdQueue'].put(['setRoiStartPos', cameraState['xOrigin'], cameraState['yOrigin']])

        # We need to force the image scroller to close so that the scroll bars get removed.
        if imageZoomScroller is not None:
            imageZoomScroller.close()  # noqa
            gui.update()
        imageZoomScroller = None  # Force recontruction of imageZoomScroller when correct shape video frame arrives

        # If camera was supposed to be running, restart it
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['startVideo'])
    else:
        showInfo('Invalid setting',
                 f"This camera only supports the following bin sizes:\n\n"
                 f"{cameraInfoDict['SupportedBins']}\n\n"
                 f"You requested a bin size of {bin_size}")

def askForUSB3bandwidth():
    dlg = SliderDialog(gui, title="USB3 % bandwidth used by camera",
                       initialValue=cameraState['bandwidth'][0],
                       length=400,
                       minVal=cameraControlInfo['BandWidth']['MinValue'],
                       maxVal=cameraControlInfo['BandWidth']['MaxValue'])
    answer = dlg.result
    if answer is None:
        return
    elif 0 <= answer <= 100:
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['stopVideo'])
            while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
                pass
        GLOBAL['camCmdQueue'].put(['setUSB3bandwidth', [answer, False]])
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['startVideo'])
        cameraState['bandwidth'] = [answer, False]
    else:
        showInfo('Program error',
                 f"Unexpected answer returned by USB3bandwidthDialog: {answer}")
def askForBlackLevel():
    dlg = SliderDialog(gui, title="Black level",
                       initialValue=cameraState['blackLevel'],
                       length=400,
                       minVal=cameraControlInfo['Offset']['MinValue'],
                       maxVal=cameraControlInfo['Offset']['MaxValue'])
    black_level = dlg.result

    if black_level is None:
        return
    else:
        GLOBAL['camCmdQueue'].put(['setBlackLevel', black_level])
        cameraState['blackLevel'] = black_level

def askForExposureTime():
    # ZWO uses microseconds as the units for exposure time. We prefer milliseconds, so factors of 1000 will
    # appear frequently as we convert back and forth.
    # The tabs at the end of the prompt make the widget wide enough to show the title properly
    exposure_time = simpledialog.askfloat(
        title='Exposure time entry',
        initialvalue= cameraState['exposure'][0] / 1000,
        prompt='Enter exposure time (milliseconds):\t\t\t\t\t')

    max_exposure_time = cameraControlInfo['Exposure']['MaxValue'] / 1000  # Convert to milliseconds
    min_exposure_time = cameraControlInfo['Exposure']['MinValue'] / 1000
    if exposure_time is None:
        return
    elif min_exposure_time <= exposure_time <= max_exposure_time:
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['stopVideo'])
            while not GLOBAL['camCmdQueue'].empty():  # Wait for camera to get the stopVideo command
                pass
        GLOBAL['camCmdQueue'].put(['setExposureTime', [int(exposure_time * 1000), False]])  # Convert to microseconds
        if cameraState['videoOn']:
            GLOBAL['camCmdQueue'].put(['startVideo'])
        cameraState['exposure'] = [int(exposure_time * 1000), False]
    else:
        showInfo('Out of range error',
                 f'The exposure time must be between {min_exposure_time} and {max_exposure_time} milliseconds.\n\n')

def askForHistogram():
    global rawImage, gui, cameraState, ledIntensityRange, ledIntensityScale, histogramStack


    def plot(parent, data):
        global lastROIinputString

        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
        from matplotlib.figure import Figure

        if len(histogramStack) == 10:  # 10 is the number of histograms that will display at the same time.
            old_parent = histogramStack.pop()
            old_parent.destroy()
            gc.collect()

        histogramStack.insert(0, parent)

        # The pylab figure manager will be bypassed in this instance.
        # This means that `fig` will be garbage collected as you'd expect.
        fig = Figure(figsize=(10, 5))
        _ = FigureCanvas(fig)
        axes = fig.add_subplot(111)

        if not data.dtype == np.uint8:
            std = np.std(data / 16)    # noqa (None nag)
            mean = np.mean(data / 16)  # noqa (None nag)
        else:
            std = np.std(data)
            mean = np.mean(data)  # noqa (None nag)

        # snr = mean / std
        if lastROIinputString == '':
            lastROIinputString = f"{cameraState['currentImageWidth']} x {cameraState['currentImageHeight']}"
        msg = f"Black level: {cameraState['blackLevel']}   gain: {cameraState['gain'][0]}  "\
              f"exposure: {cameraState['exposure'][0] / 1000:0.3f} ms  " \
              f"gamma: {cameraState['gamma']}\n" \
              f"ROI: {lastROIinputString}  bin size: {cameraState['binSize']}  mean: {mean:0.2f}  std: {std:0.3f}\n" \
              f"{ledIntensityRange.get()} current range flash LED: @ level {ledIntensityScale.get()}  mean: {mean:0.2f}"
        axes.set_title(f"Histogram of pixel values for {cameraState['cameraName']}\n" + msg)
        if data.dtype == np.uint8:
            axes.set_xticks([i for i in range(0,251,10)])
        else:
            axes.set_xticks([i for i in range(0,4091,250)])
        axes.grid(axis='x')
        if data.dtype == np.uint8:
            bin_count = 256
        else:
            bin_count = 4096
            data //= 16
        y, x = np.histogram(data, range=(0, bin_count-1), bins=bin_count, density=False)
        axes.plot(x[:-1],y, drawstyle='steps')
        axes.set_xlabel('pixel value')
        axes.set_ylabel('number of pixels')

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        local_canvas = FigureCanvasTkAgg(fig, master=parent)
        local_canvas.draw()

        # Place the canvas on the Tkinter window
        local_canvas.get_tk_widget().pack()

    def create_window():
        newwindow = tk.Toplevel()
        return newwindow

    if rawImage is None:
        showInfo('Image not available',
                 f"There is no image available yet.\n\n"
                 f"Try again after video is running")
        return

    plot(create_window(), rawImage)  # noqa
def saveCameraSettings():
    filename_to_use = tk.filedialog.asksaveasfilename(
        defaultextension='.zwo_cam_set'
    )

    if filename_to_use is None or filename_to_use == '':
        return
    else:
        print(f'filename_to_use: {filename_to_use}')
        head, tail = os.path.split(filename_to_use)
        parts = []
        if '.' in tail:
            parts = tail.split('.')
        if not filename_to_use.endswith('.zwo_cam_set'):
            showInfo('Filename error', f'.{parts[-1]} is an invalid extension. Required extension is:\n\n'
                                       f'\t.zwo_cam_set\n\n'
                                       f'This is the extension provided by default.')
            return
        with open(filename_to_use, 'wb') as file_to_use:
            pickle.dump(cameraState, file_to_use)
        showInfo('Camera settings saved to:', f"{filename_to_use}\t\t\t\t\t\t")


def restoreCameraSettings():
    global cameraState
    filetypes = (
        ('cam_set files', '*.zwo_cam_set'),
        ('All files', '*.*')
    )
    filename = tk.filedialog.askopenfilename(
        title='Select camera settings file',
        initialdir='./',
        filetypes=filetypes
    )
    if filename == '':
        return
    else:
        with open(filename, 'rb') as file_to_read:
            new_cameraState = pickle.load(file_to_read)
            reconfigureCamera(new_cameraState)
            pass

def reconfigureCamera(newState):  # noqa
    GLOBAL['camCmdQueue'].put(['setGain', newState['gain']])
    x_size = newState['currentImageWidth']
    y_size = newState['currentImageHeight']
    # print(f'x_size: {x_size}  y_size: {y_size}  bin_size: {newState["binSize"]}  image_type: {newState["imageType"]}')
    GLOBAL['camCmdQueue'].put(['setRoiFormat', x_size, y_size, newState['binSize'], newState['imageType']])
    # print(f'xOrigin: {newState["xOrigin"]}  yOrigin: {newState["yOrigin"]}')
    GLOBAL['camCmdQueue'].put(['setRoiStartPos', newState['xOrigin'], newState['yOrigin']])
    GLOBAL['camCmdQueue'].put(['setExposureTime', newState['exposure']])
    GLOBAL['camCmdQueue'].put(['setBlackLevel', newState['blackLevel']])
    GLOBAL['camCmdQueue'].put(['setUSB3bandwidth', newState['bandwidth']])
    GLOBAL['camCmdQueue'].put(['setUSB3speed', newState['speedMode']])
    GLOBAL['camCmdQueue'].put(['setGamma', newState['gamma']])
    pass

def askImageFlip():
    global cameraState

    flip_request = tk.simpledialog.askstring(
        title='Image flip request',
        prompt='Enter h for a horizontal flip (left becomes right)\n'
               'or enter v for a vertical flip (top becomes bottom)\n'
               'or both'
    )
    if flip_request is None or flip_request == '':
        return

    current_flip_state = cameraState['flipStatus']

    flips_wanted = 0
    if 'h' in flip_request:
        flips_wanted += 1
    if 'v' in flip_request:
        flips_wanted += 2

    new_flip_state = current_flip_state ^ flips_wanted

    cameraState['flipStatus'] = new_flip_state

    GLOBAL['camCmdQueue'].put(['setFlip', new_flip_state])

def askCameraSettings(show_settings=True):
    global cameraInfoDict, cameraState, gui

    cameraInfoDict = {}

    start_time = time.perf_counter_ns()
    GLOBAL['camCmdQueue'].put(['getCameraInfo'])
    GLOBAL['camCmdQueue'].put(['getGain'])
    GLOBAL['camCmdQueue'].put(['getAvgFrameTime'])
    GLOBAL['camCmdQueue'].put(['getExposure'])
    GLOBAL['camCmdQueue'].put(['getBlackLevel'])
    GLOBAL['camCmdQueue'].put(['getGamma'])
    GLOBAL['camCmdQueue'].put(['getRoiSize'])
    GLOBAL['camCmdQueue'].put(['getRoiCorner'])
    GLOBAL['camCmdQueue'].put(['getTemperature'])
    GLOBAL['camCmdQueue'].put(['getDroppedFrames'])
    GLOBAL['camCmdQueue'].put(['getBandwidth'])
    GLOBAL['camCmdQueue'].put(['getSpeedMode'])
    GLOBAL['camCmdQueue'].put(['getSDKversion'])
    GLOBAL['camCmdQueue'].put(['getFlipStatus'])

    if show_settings:
        # The 'settingsDone' command gets returned by camProc to guiCmdQueue as 'settingsDone'
        # which causes a scrolled list of camera settings to appear
        GLOBAL['camCmdQueue'].put(['settingsDone'])
    end_time = time.perf_counter_ns()
    if DEV_MODE:
        print(f'askCameraSettings: {end_time - start_time} ns')

def calcBandwidthRequirements():
    global cameraState

    frameRate = 1.0 / (cameraState['exposure'][0] / 1_000_000)

    numBytes = [1 ,3, 2, 1]  # Used to convert ZWO image type codes into number of bytes involved

    bytesPerPixel = numBytes[cameraState['imageType']]

    bytesPerSecRequired = frameRate * cameraState['currentImageWidth'] * cameraState['currentImageHeight'] * bytesPerPixel

    mBytesPerSecRequired = bytesPerSecRequired / 1_000_000

    return mBytesPerSecRequired

    # cameraMBytesPerSec = 8 * 60.0  # Spec for the camera according to SpinView  (480 MBytes per second)
    # perCentThroughputUsed = (mBytesPerSecRequired / cameraMBytesPerSec) * 100
    #
    # if perCentThroughputUsed > 100:
    #     msg = f'At the requested exposure time, image size, and pixel bit depth,\n\n' \
    #           f'the camera throughput will be exceeded.'
    #     messageBox.showerror('Camera throughput max exceeded', msg)
    #     return
    #
    # if perCentThroughputUsed >= 70:
    #     msg = f'The required throughput is greater than 70 %\n\n' \
    #           f'At this level, dropped frames are likely.'
    #     messageBox.showwarning('Throughput is high', msg)

def askForVideoOnOff():
    global imageZoomScroller, pixelValueLabel
    dlg = ButtonAnswerDialog(gui, title='Select video state', buttonOneText='ON', buttonTwoText='OFF')
    answer = dlg.result
    if answer is None:
        return
    elif answer == 'ON':
        GLOBAL['camCmdQueue'].put(['startVideo', time.perf_counter_ns()])
        cameraState['videoOn'] = True
        pixelValueLabel.configure(text='Video turned on')  # noqa
    elif answer == 'OFF':
        GLOBAL['camCmdQueue'].put(['stopVideo', time.perf_counter_ns()])
        cameraState['videoOn'] = False
        pixelValueLabel.configure(text='Video turned off')  # noqa
    else:
        showInfo('Unexpected button answer', f'Button answer: {answer}')

def askForGain():
    dlg = SliderDialog(gui, title="Camera gain",
                       initialValue=cameraState['gain'][0],
                       length=600,
                       minVal=cameraControlInfo['Gain']['MinValue'],
                       maxVal=cameraControlInfo['Gain']['MaxValue'])
    gain_level = dlg.result

    if gain_level is None:
        return
    else:
        GLOBAL['camCmdQueue'].put(['setGain', [gain_level, False]])
        cameraState['gain'] = [gain_level, False]

def processSetTargetFolderButtonClick():
    global fitsFolderPath, fitsRoot, folderName

    if saveFolderRoot == '':
        showInfo('Procedure error',
                 f"You must select a parent folder first!")
        return

    myDialog = TargetFolderDialog(
        gui,
        title='Name the target folder  -  Supply file prefix (optional)',
        folder=folderName,
        rootName=fitsRoot
    )
    if myDialog.myAnswer == 'Create folder':
        folderName = myDialog.textVariable.get()
        fitsRoot = myDialog.fitsRoot.get()
        fullPath = f'{saveFolderRoot}/{folderName}'
        fitsFolderPath = fullPath
        if not os.path.exists(fullPath):
            os.mkdir(fullPath)
        else:
            fitsFilesFound = glob.glob(f'{saveFolderRoot}/{folderName}/*.fits')
            numFitsFilesFound = len(fitsFilesFound)
            if numFitsFilesFound > 0:
                msg = (f"{numFitsFilesFound} FITS files are already present.\n\n"
                       f"Do you wish to delete them?")
                answer = tk.messagebox.askyesno('Confirmation required', msg)
                if answer:  # User requests deletion of the fits files
                    for fname in fitsFilesFound:
                        os.remove(fname)

        frameNamePattern = f'{fullPath}/{fitsRoot}nnnnnnn.fits'
        framePath.set(frameNamePattern)
    else:
        return


def processSelectParentFolderButtonClick():
    global gui, saveFolderRoot

    directory = fd.askdirectory(
        title='Select FITS top-level folder',
        initialdir='/'
    )

    if directory:
        framePath.set(directory)
        saveFolderRoot = directory
        iniDict['saveFolderRoot'] = directory
    else:
        showInfo('FITS parent folder chosen:', 'User cancelled - no choice made')
    gui.update()


def showInfo(title, msg, non_modal=True):
    if non_modal:
        _ = NonModalInfoDialog(
            gui,
            title=f'{title}',
            text=f'{msg}\t\t\t'
        )
    else:
        messageBox.showinfo(title, msg)

def formCommandToSendForLedIntensityChange(brightness=None):
    if brightness is None:
        intensity = ledIntensity.get()
    else:
        intensity = brightness

    if ledIntensityRange.get().startswith('H'):
        return f'setLED( high, {intensity})\n'

    if ledIntensityRange.get().startswith('M'):
        return f'setLED( mid, {intensity})\n'

    if ledIntensityRange.get().startswith('L'):
        return f'setLED( low, {intensity})\n'

    showInfo('Error',
             f"An unexpected value of {ledIntensityRange.get()} as LED intensity range was found.")

def processLedRangeChange(value):  # noqa (value not used)
    sendLedIntensityCommandToArduino()
def processLedIntensityChange(value):  # noqa (value not used)
    global lastLedIntensity, arduinoPort

    # level = ledIntensityScale.get()
    # showInfo('Alert',f'processLedIntensityChange() entered with level: {level}')

    # if value == lastLedIntensity:  # A slide movement has started, but the value has not changed yet
    #     return
    # else:
    #     lastLedIntensity = value

    sendLedIntensityCommandToArduino()

def setFlashIntensity():
    global flashOffCmdString, flashOnCmdString

    flashOnCmdString = formCommandToSendForLedIntensityChange()
    flashOffCmdString = formCommandToSendForLedIntensityChange(brightness=0)

    ledIntensity.set(0)

    sendLedIntensityCommandToArduino(flashOffCmdString)

    # showInfo('Flash commands',
    #          f"flash ON  command: {flashOnCmdString}\n\n"
    #          f"flash OFF command: {flashOffCmdString}")
def sendLedIntensityCommandToArduino(cmd=None):
    global arduinoPort

    if cmd is None:
        arduinoCommand = formCommandToSendForLedIntensityChange()
    elif cmd == 'ON':
        arduinoCommand = flashOnCmdString
    elif cmd == 'OFF':
        arduinoCommand = flashOffCmdString
    else:
        arduinoCommand = cmd

    # print(arduinoCommand)  # TODO Remove this print

    try:
        if arduinoPort is not None:
            try:
                arduinoPort.write(bytes(arduinoCommand, encoding='ascii'))  # noqa (didn't like None for initial value)

            except win_serial.SerialTimeoutException as e:  # noqa
                _ = NonModalInfoDialog(
                    gui,
                    title=f'Arduino timeout exception:',
                    text= f'{e}\t\t\t'
                )
    except Exception as e:  # noqa  (e shadows)
        print(f'In sendLedIntensityCommandToArduino(): {e}')
        showInfo('Arduino error',
                 f"In sendLedIntensityCommandToArduino(): {e}")


def processStartButtonClick():
    global flashOnCmdString

    if fitsFolderPath == "":
        showInfo('Error !!!',
                 f"There is no folder for the FITS files assigned yet.\n\n"
                 f"Use the 'Set FITS parent folder' button and the\n"
                 f"'Set target folder' button to declare the correct path.\n\n")
        return

    if flashOnCmdString is None or flashOnCmdString == '':
        showInfo('Setup error',
                 f"\nflash intensity has not been set yet.\n\n\n\n\n\n")
        return

    try:
        if not cameraState['videoOn']:
            GLOBAL['fileWritingInProgress'].value = False
            GLOBAL['numFramesWritten'].value = 0
            currentFrameNum = 0
            if frameCount.get() == '':
                showInfo('Setup error',
                         f"\nThe number of frames to capture has not been set.\n\n\n\n")
                return
            GLOBAL['numFramesToRecord'].value = int(frameCount.get())  # noqa

            GLOBAL['camCmdQueue'].put(['startVideo'])
            cameraState['videoOn'] = True
            while not GLOBAL['cameraIsRunning'].value:
                pixelValueLabel.configure(text='Waiting for video to turn on')  # noqa
            pixelValueLabel.configure(text='Video turned on')  # noqa
            GLOBAL['camCmdQueue'].put(['startRecording'])

        else:
            GLOBAL['numFramesToRecord'].value = int(frameCount.get())  # noqa
            currentFrameNum = GLOBAL['numFramesWritten'].value
            GLOBAL['camCmdQueue'].put(['startRecording'])


        if currentFrameNum > 0:
            # We're being asked to stop acquisition
            GLOBAL['numFramesWritten'].value = 0
            GLOBAL['fileWritingInProgress'].value = True
            # Set new upper limit so that file write progress bar works properly
            GLOBAL['numFramesToRecord'].value = currentFrameNum + 1

            startButton.config(bg='red', text='Start acquisition')
            return

        # We're about to start frame acquisition. But first we check for any fits files
        # that are already present.

        fitsFilesFound = glob.glob(f'{saveFolderRoot}/{folderName}/*.fits')
        numFitsFilesFound = len(fitsFilesFound)
        if numFitsFilesFound > 0:
            msg = (f"{numFitsFilesFound} FITS files are already present in the target folder.\n\n"
                   f"Do you wish to delete them?")
            answer = tk.messagebox.askyesno('Confirmation required', msg)
            if answer:  # User requests deletion of the fits files
                for fname in fitsFilesFound:
                    os.remove(fname)
            else:
                # Return without triggering acquisition start
                return

        # We're about to manually start acquisition. Clear UTC start first.
        GLOBAL['UTCstartArmed'].value = False
        setUtcButton.config(text='Arm UTC start', bg='lightgray')

        GLOBAL['numFramesWritten'].value = 0
        GLOBAL['fileWritingInProgress'].value = True  # This the indicator that a manual start has been done


        startButton.config(bg='green', text="Stop acquisition")

    except ValueError as err:
        showInfo('Input error', f'Error in Frame Count entry: {err}')


def memUsageReport():
    global memoryUsageBar, memoryUsageLabel

    memoryPct = psutil.virtual_memory().percent
    memoryTotal = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GigaBytes
    memoryFree = psutil.virtual_memory().free / (1024 ** 3)    # Convert to GigaBytes
    memoryUsageBar['value'] = memoryPct
    memoryUsageLabel.config(text=f'Free mem: {memoryFree:0.1f} GB  '
                                 f'Total mem: {memoryTotal:0.1f} GB Used: {memoryPct:0.1f} %')  # noqa
    return memoryPct


def displayThread():
    global contrastLow, contrastHigh
    global saveFolderRoot, doNotAskForTimeCorrectionAgain, okToCorrectComputerUTCtime
    global canvasFrame, imageZoomScroller, pixelValueLabel, rawImage

    # Grab the sticky stuff from the ini file
    if 'saveFolderRoot' in iniDict.keys():
        saveFolderRoot = iniDict['saveFolderRoot']
        framePath.set(saveFolderRoot)
    else:
        saveFolderRoot = ''

    try:
        if DEV_MODE:
            print('')
        while True:
            got_an_image = False
            while GLOBAL['displayQueue'].qsize() > 0:
                got_an_image = True
                time_rcvd = time.perf_counter_ns()
                frameNumber, droppedFrames, imageToDisplay, time_sent, *_ = GLOBAL['displayQueue'].get()  # noqa
                numpyImage = imageToDisplay
                if DEV_MODE:
                    print(f'image rcvd: {time_rcvd - time_sent} ns')
                start_display_time = time.perf_counter_ns()
            if not got_an_image:
                time.sleep(0.1)
                continue


            # imageType = cameraState['imageType']
            # if imageType == UINT8:
            #     numBytes = 1
            # elif imageType == RAW16:
            #     numBytes = 2
            # else:
            #     showInfo(title='Camera state error', msg=f'Invalid imageType found: {imageType}')

            # timeStamp = f"timestamp: {imageToDisplay[2]['Serial Data:']}"

            # For debug - we add Frame ID to timestamp
            # timeStamp = imageToDisplay[2]['Serial Data:'] + "  " + imageToDisplay[2]['Frame ID:']

            # try:
            #     if not doNotAskForTimeCorrectionAgain:
            #         tsData = timeStamp[10:].strip()
            #         if tsData:
            #             mostCurrentTimestamp = tsData + 'Z'
            #             # print(f'ts str: {mostCurrentTimestamp}')
            #             mostCurrentUTCtime = parser.parse(mostCurrentTimestamp) + \
            #                 datetime.timedelta(milliseconds=int(GLOBAL['exposureTime']))
            #             computerUTCtime = datetime.datetime.now(timezone.utc)
            #
            #             setUTCfailed = True
            #             if okToCorrectComputerUTCtime:
            #                 # try:
            #                 #     win32api.SetSystemTime(
            #                 #         mostCurrentUTCtime.year,
            #                 #         mostCurrentUTCtime.month,
            #                 #         mostCurrentUTCtime.isoweekday(),
            #                 #         mostCurrentUTCtime.day,
            #                 #         mostCurrentUTCtime.hour,
            #                 #         mostCurrentUTCtime.minute,
            #                 #         mostCurrentUTCtime.second,
            #                 #         int(mostCurrentUTCtime.microsecond / 1000)
            #                 #     )
            #                 #     setUTCfailed = False
            #                 # except Exception as e:  # noqa
            #                 #     setUTCfailed = True
            #                 #     messageBox.showerror('Computer time', e)
            #                 #     # print(e)
            #                 okToCorrectComputerUTCtime = False
            #                 doNotAskForTimeCorrectionAgain = True
            #                 if not setUTCfailed:
            #                     showInfo("Computer clock",
            #                              'The CPU clock was reset to match timestamp UTC time.\n')
            #                 else:
            #                     messageBox.showwarning(
            #                         "Computer clock",
            #                         'The CPU clock could not be reset because of error')
            #             else:
            #                 timeDelta = computerUTCtime - mostCurrentUTCtime
            #                 msg = f"The computer UTC setting and the 'timestamper'\n" \
            #                       f"UTC setting are within {abs(timeDelta)} seconds.\n\n" \
            #                       f"If this is too large, restart the program and grant\n" \
            #                       f"permission to automatically reset the computer clock\n" \
            #                       f"to match the 'timestamper' UTC time."
            #                 messageBox.showinfo('Computer UTC setting', msg)
            #                 okToCorrectComputerUTCtime = False
            #                 doNotAskForTimeCorrectionAgain = True
            #     GLOBAL['timestampReport'].set(timeStamp)  # noqa
            #
            # except Exception as e:  # noqa
            #     messageBox.showerror('Unexpected exception', repr(e))

            # memoryPct = memUsageReport()  # Give memory stats update

            # if memoryPct > MAX_RAM_USAGE_PCT and GLOBAL['numFramesWritten'].value >= 0:
            #     GLOBAL['numFramesToRecord'].value = GLOBAL['numFramesWritten'].value
            #     GLOBAL['numFramesWritten'].value = -1
            #     showInfo('Critical message',
            #              f'Image capture terminated because system RAM usage\n'
            #              f'exceeded {MAX_RAM_USAGE_PCT} %\n\n'
            #              f"{GLOBAL['numFramesWritten'].value - 1} frames were captured and are being written to disk.")

            lowScaleValue = int(contrastLow.get() * 255)
            highScaleValue = int(contrastHigh.get() * 255)

            if lowScaleValue == highScaleValue:
                highScaleValue += 1  # To avoid a divide by zero condition during contrast scaling.

            rawImage = numpyImage[:]  # noqa (reference before assignment possible)
            if cameraState['imageType'] == asi.ASI_IMG_RAW16:
                numpyImage = numpyImage / 256  # Changes type from uint16 to float64
                numpyImage = numpyImage - lowScaleValue
                np.clip(numpyImage, 0, 255, out=numpyImage)
                numpyImage = numpyImage * (255 - lowScaleValue) / (highScaleValue - lowScaleValue)
            else:
                numpyImage = numpyImage / 1  # Changes type from uint8 to float64
                numpyImage = numpyImage - lowScaleValue
                np.clip(numpyImage, 0, 255, out=numpyImage)
                numpyImage = numpyImage * (255 - lowScaleValue) / (highScaleValue - lowScaleValue)

            try:
                if imageZoomScroller is None:
                    previous_zoom_factor = 1
                    height, width = numpyImage.shape
                    if not height == cameraState['currentImageHeight'] or not width == cameraState['currentImageWidth']:
                        pass
                        # print(f'In display thread: received unexpected image shape of {width} x {height}')
                    else:
                        imageZoomScroller = A_ScollableCanvas(canvasFrame, width, height,
                                                              pixelValueDisplay=pixelValueLabel, zoom_factor=1)
                        imageZoomScroller.set_new_image(numpyImage, rawImage)

                else:
                    # zoom_factor = imageZoomScroller.zoom_factor()
                    zoom_factor = int(zoomLevel.get())

                    if not zoom_factor == previous_zoom_factor:  # noqa previous_zoom_factor maybe not set
                        height, width = numpyImage.shape
                        if not height == cameraState['currentImageHeight'] or not width == cameraState['currentImageWidth']:
                            pass
                            # print(f'In display thread: received unexpected image shape of {width} x {height}')
                        else:
                            previous_zoom_factor = zoom_factor
                            zoomedImage = np.repeat(np.repeat(numpyImage, zoom_factor, axis=0), zoom_factor, axis=1)
                            zoomedRawImage = np.repeat(np.repeat(rawImage, zoom_factor, axis=0), zoom_factor, axis=1)
                            height, width = zoomedImage.shape
                            imageZoomScroller = A_ScollableCanvas(canvasFrame, width, height,
                                                                  pixelValueDisplay=pixelValueLabel, zoom_factor=zoom_factor)
                            imageZoomScroller.set_new_image(zoomedImage, zoomedRawImage)
                    else:
                        height, width = numpyImage.shape
                        if not height == cameraState['currentImageHeight'] or not width == cameraState['currentImageWidth']:
                            pass
                            # print(f'In display thread: received unexpected image shape of {width} x {height}')
                        else:
                            zoomedImage = np.repeat(np.repeat(numpyImage, zoom_factor, axis=0), zoom_factor, axis=1)
                            zoomedRawImage = np.repeat(np.repeat(rawImage, zoom_factor, axis=0), zoom_factor, axis=1)
                            imageZoomScroller.set_new_image(zoomedImage, zoomedRawImage)
            except Exception as e1:
                print(f'{e1}')

            gui.update()     # update on screen (this must be called from main thread)
            end_display_time = time.perf_counter_ns()
            if DEV_MODE:
                print(f'frame {frameNumber:06d}   display time: {end_display_time - start_display_time}')  # noqa (reference before assignment possible)

    except Exception as e:  # noqa  if user hits Ctrl-C, everything should end gracefully
        print(e)
        pass

    print('Done!')
    sys.exit(0)


class BitDepthDialog(simpleDialog.Dialog):
    def __init__(self, parent, title):
        self.myLabel = None
        self.myAnswer = None
        super().__init__(parent, title)

    def body(self, frame):
        self.myLabel = tk.Label(frame, width=25, text='Choose bits per pixel desired:')
        self.myLabel.pack()

        return frame

    def buttonOnePressed(self):
        self.myAnswer = '16 bit'
        self.destroy()

    def buttonTwoPressed(self):
        self.myAnswer = '8 bit'
        self.destroy()

    def buttonbox(self):
        buttonOne = tk.Button(self, text='16 bit', width=14, command=self.buttonOnePressed)
        buttonOne.pack(side='left', padx=6, pady=10)
        buttonTwo = tk.Button(self, text='8 bit', width=14, command=self.buttonTwoPressed)
        buttonTwo.pack(side='right', padx=6, pady=10)

class TargetFolderDialog(simpleDialog.Dialog):
    def __init__(self, parent, title, folder='', rootName=''):
        self.myLabel = None
        self.rootLabel = None
        self.myAnswer = None
        self.myEntry = None
        self.rootEntry = None
        self.textVariable = tk.StringVar()
        self.textVariable.set(folder)
        self.fitsRoot = tk.StringVar()
        self.fitsRoot.set(rootName)
        super().__init__(parent, title)

    def body(self, frame):
        self.myLabel = tk.Label(frame, text='target folder name', justify=tk.LEFT)
        self.myEntry = tk.Entry(frame, width=100, textvariable=self.textVariable)
        self.myLabel.pack()
        self.myEntry.pack()
        self.myEntry.bind('<Map>', self.on_map)  # <--- ADDED.
        self.myEntry.bind('<Return>', self.buttonTwoPressed)
        self.rootLabel = tk.Label(
            frame, justify=tk.LEFT,
            text='<prefix> for naming the fits file sequence. Example: <prefix>0000257.fits'
        )
        self.rootEntry = tk.Entry(frame, width=100, textvariable=self.fitsRoot)
        self.rootEntry.bind('<Return>', self.buttonTwoPressed)
        self.rootLabel.pack(pady=(20, 0))
        self.rootEntry.pack(pady=(0, 20))

        return frame

    # ADDED METHOD.
    def on_map(self, event):  # noqa (event not used)
        self.myEntry.focus_force()

    def buttonOnePressed(self):
        self.myAnswer = 'Cancel'
        self.destroy()

    def buttonTwoPressed(self, event=None):  # noqa (event not used)
        self.myAnswer = 'Create folder'
        self.destroy()

    def buttonbox(self):
        self.buttonOne = tk.Button(self, text='Cancel', width=14, command=self.buttonOnePressed)
        self.buttonTwo = tk.Button(self, text='Create folder', width=14, command=self.buttonTwoPressed)
        self.buttonOne.pack(side='left', padx=(10, 10), pady=(10, 10))
        self.buttonTwo.pack(side='left', padx=(10, 10), pady=(10, 10))
        self.buttonTwo.bind('<Return>', self.buttonTwoPressed)


class RoiDialog(simpleDialog.Dialog):
    def __init__(self, parent, title):
        self.myLabel = None
        self.myAnswer = None
        self.myListbox = None
        super().__init__(parent, title)

    def body(self, frame):
        self.myLabel = tk.Label(frame, width=25, text='Choose ROI:')
        self.myLabel.pack()
        self.myListbox = tk.Listbox(frame, selectmode='single', font='Courier')
        self.myListbox.insert(0, '1440 x 1080')
        self.myListbox.insert(1, ' 960 x 720')
        self.myListbox.insert(2, ' 720 x 540')
        self.myListbox.insert(3, ' 600 x 400')
        self.myListbox.insert(4, ' 504 x 504')
        self.myListbox.insert(5, ' 400 x 400')
        self.myListbox.pack()

        return frame

    def buttonOnePressed(self):
        self.myAnswer = self.myListbox.curselection()
        self.destroy()

    def buttonbox(self):
        buttonOne = tk.Button(self, text='Apply', width=14, command=self.buttonOnePressed)
        buttonOne.pack(padx=6, pady=10)


def on_close():

    try:
        GLOBAL['camCmdQueue'].put(['quit'])
        numCamCmds = GLOBAL['camCmdQueue'].qsize()
        numDisplayItems = GLOBAL['displayQueue'].qsize()
        numGuiCmds = GLOBAL['guiCmdQueue'].qsize()
        print(f'\nAfter gui.quit() in on_close():  numCamCmds={numCamCmds}  numDisplayItems={numDisplayItems}  '
              f'numGuiCmds={numGuiCmds}')

        while GLOBAL['camCmdQueue'].qsize() > 0:
            _ = GLOBAL['camCmdQueue'].get()
        while GLOBAL['displayQueue'].qsize() > 0:
            _ = GLOBAL['displayQueue'].get()
        # while GLOBAL['quiCmdQueue'].qsize() > 0:  # This throws an exception, so we don't work further with this one.
        #     _ = GLOBAL['guiCmdQueue'].get()

        numCamCmds = GLOBAL['camCmdQueue'].qsize()
        numDisplayItems = GLOBAL['displayQueue'].qsize()
        # numGuiCmds = GLOBAL['guiCmdQueue'].qsize()

        print(f'\nAfter reading display and camCmd queues dry:  numCamCmds={numCamCmds}  numDisplayItems={numDisplayItems}  '
              f'numGuiCmds={numGuiCmds}')

        gui.quit()  # This causes mainloop() to exit

    except Exception as e1:
        print(f'!!!!! While tryng to quit gui got: {e1} !!!!!')

    # Write the initialization dictionary (holds things that are to be sticky)
    pickle.dump(iniDict, open('PyZwoCapture.ini.p', 'wb'))


def getTkWindow():
    tempWin = tk.Tk()
    tempWin.withdraw()  # Hide the parent

    # Now compute a reasonable center position
    screenHeight = tempWin.winfo_screenheight()
    screenWidth = tempWin.winfo_screenwidth()
    positionTop = int(screenHeight / 2 - 100)
    positionRight = int(screenWidth / 2 - 100)
    tempWin.geometry(f'{screenWidth}x{screenHeight}+{positionRight}+{positionTop}')
    tempWin.update()
    return tempWin


# GUI globals #################################################################

def buildGui(GLOBAL):  # noqa
    global frameCount, framePath, contrastLow, contrastHigh
    global xOffsetRoi, yOffsetRoi, blackSetting
    global utcSetting, utcDuration, roiSetting, imageXoffset, imageYoffset
    global gui, zoomLevel, ledIntensity, ledIntensityRange

    # Get our GUI parent
    gui = tk.Tk()

    frameCount = tk.StringVar()
    framePath = tk.StringVar()
    contrastLow = tk.DoubleVar()
    contrastHigh = tk.DoubleVar()
    xOffsetRoi = tk.IntVar()
    yOffsetRoi = tk.IntVar()
    utcSetting = tk.StringVar()
    utcDuration = tk.DoubleVar()
    roiSetting = tk.StringVar()
    imageXoffset = tk.IntVar()
    imageYoffset = tk.IntVar()
    zoomLevel = tk.StringVar()
    ledIntensity = tk.IntVar()
    ledIntensityRange = tk.StringVar()

    guiInit()


saveThread: threading.Thread     # For writing images to filess
imageDisplayThread: threading.Thread     # For producing the display of images
guiCmdThread: threading.Thread   # For camProc to send commands to the gui


def run():
    global GLOBAL
    global iniDict, saveThread, imageDisplayThread, guiCmdThread, outlawList, zoomLevel
    global leapSeconds

    # Restore the iniDict (dictionary of items that are to be persisted across app invocation)
    # For a new installation, there will be no src.ini.p file, so we test for that.
    # src.ini.p is created the first time the app is closed
    try:
        iniDict = pickle.load(open('PyZwoCapture.ini.p', 'rb'))
    except FileNotFoundError:
        pass

    buildGui(GLOBAL)

    # Create separate thread for FITS file writing
    saveThread = threading.Thread(target=writeFilesThread)
    saveThread.daemon = True  # Needed so that thread stops when program exits
    saveThread.start()

    imageDisplayThread = threading.Thread(target=displayThread)
    imageDisplayThread.daemon = True  # Needed so that thread stops when program exits
    imageDisplayThread.start()

    gui.protocol("WM_DELETE_WINDOW", on_close)

    guiCmdThread = threading.Thread(target=guiCmdHandler)
    guiCmdThread.daemon = True  # Needed so that thread stops when program exits
    guiCmdThread.start()

    try:
        # Run the GUI
        gui.mainloop()
    except Exception as e1:
        print(f'While trying to exit got: {e1}')

    print(f'\n\nmain() reports: gui.mainloop() has exited so I will exit now too.\n')


def main():
    homeDir = os.getcwd()
    print(f'Home directory: {homeDir}')
    try:
        GLOBAL['cameraControls'] = []
        camProc = Process(
            target=camCaptureProc,
            args=[GLOBAL],
            daemon=True
        )
        camProc.start()

        try:
            run()  # This builds the gui then sets up the image display, file write thread, and the gui command threads
        except Exception as e:
            print(f'While trying to exit got: {e}')

        print('main() has quit running.\n')
        GLOBAL['camCmdQueue'].put(['quit'])
        time.sleep(1)
        camProc.terminate()
        print('Now waiting for camProc.join() to finish.\n')
    finally:
        print('Finally was reached')
        pass


if __name__ == '__main__':

    main()
    