from tkinter import *
from tkinter import scrolledtext

import PIL.Image
import PIL.ImageTk
import cv2
from time import time

class monitor:
    
    # Parameter: bit_mess: bit seqence to be sent (in string form)

    def __init__(self, master, bit_mess):
        '''
        Defines the monitor window.

        :param master: root window
        :type master: Tk
        :param bit_mess: the bit sequence to be sent
        :type bit_mess: string
        '''
        # Variable declaration

        self.flag = False
        self.bit_mess = bit_mess

        self.master = master
        self.master.resizable(False, False)

        # Frame1
        # Content: label1          : Label
        #          transmitted_bits: ScrolledText

        self.frame_1 = Frame(self.master)

        self.label1 = Label(self.frame_1, text = 'Transmitted bits : ')
        self.label1.pack()

        self.transmitted_bits = scrolledtext.ScrolledText(self.frame_1)
        self.transmitted_bits.config(state = 'normal')
        self.transmitted_bits.delete("1.0","end")
        self.transmitted_bits.insert('insert', bit_mess) # bit_mess is shown here
        self.transmitted_bits.config(state = 'disabled', height = 8, width = 80)
        self.transmitted_bits.pack()

        self.frame_1.pack()

        # Frame2
        # Content: label2       : Label
        #          received_bits: ScrolledText

        self.frame_2 = Frame(self.master)

        self.label2 = Label(self.frame_2, text = 'Received bits : ')
        self.label2.pack()

        self.received_bits = scrolledtext.ScrolledText(self.frame_2)
        self.received_bits.config(state = 'disabled', height = 8, width = 80)
        self.received_bits.pack()

        self.frame_2.pack()

        # Frame3
        # Content: label3    : Label
        #          error_bits: ScrolledText

        self.frame_3 = Frame(self.master)

        self.label3 = Label(self.frame_3, text = 'Error bits : ')
        self.label3.pack()

        self.error_bits = scrolledtext.ScrolledText(self.frame_3)
        self.error_bits.tag_config('error',foreground="red") # Tag config for error bits
        self.error_bits.config(state = 'disabled', height = 8, width = 80)
        self.error_bits.pack()

        self.frame_3.pack()

        # Frame4
        # Content: vid_play: Button

        self.frame_4 = Frame(self.master)

        self.vid_play = Button(self.frame_4, text = 'Play Video', width = 10, command = self.button_toggle)
        self.vid_play.pack(side = 'left')

        self.frame_4.pack()

# Parameter: bit_seq: string
    def update_recv(self, bit_seq):
        '''
        Update the received and error bits textbox upon call.

        :param bit_seq: the bits that are collected from the receiver
        :type master: string

        '''
        self.received_bits.config(state = 'normal')
        self.received_bits.insert('insert', bit_seq) # Print bit_seq in received_bits
        self.received_bits.config(state = 'disabled')

        for i in range(len(bit_seq)):
            err = str(int(self.bit_mess[i] != bit_seq[i])) # Return 1 if error occurs
            self.error_bits.config(state = 'normal')
            if self.bit_mess[i] != bit_seq[i]:
                self.error_bits.insert('insert', err, 'error') # Print 1 in red in error_bits
            else:
                self.error_bits.insert('insert', err) # Print 0 in black  in error_bits
            self.error_bits.config(state = 'disabled')

        self.bit_mess = self.bit_mess[len(bit_seq):] # Slice the original bit_mess

    def button_toggle(self):
        '''
        Switch the status of the button to True, which indicates it has been pressed.
        '''
        self.flag = True # Set the state of the play button to PRESSED

    def get_button_status(self):
        '''
        Return the status of the button.
        
        :return: the status of the button, whether it has been pressed
        :rtype: bool
        '''
        return self.flag # Return the state of the play button
    def close_windows(self):
        '''
        destroy the root window
        '''
        self.master.destroy()


class VidCap:
    def __init__(self, scale, vidsource=0):
        '''
        Defines the video to be played and its porperty.

        :param scale: the scale of which the video is being played. The higher the number, the bigger the video
        :type scale: integer
        :param vidsource: the file path of the video
        :type vidsource: string
        '''
        self.vid = cv2.VideoCapture(vidsource)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)
        self.dim = (int(self.width * scale), int(self.height * scale))

    def get_fps(self):
        '''
        Return the fps of the video.

        :return: the fps of the video
        :rtype: integer
        '''
        return self.fps

    def get_height(self):
        '''
        Return the height of the video.

        :return: the height of the video
        :rtype: integer
        '''
        return self.height

    def get_width(self):
        '''
        Return the width of the video.

        :return: the width of the video
        :rtype: integer
        '''
        return self.width

    def get_frame(self):
        '''
        Get one frame from the video.

        :returns ret, frame: whether a frame is successfully grabbed; the image from the video, None otherwise.
        :rtype: bool, image
        '''
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, self.dim, interpolation = cv2.INTER_AREA)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (False, None)

    def reset(self, vidsource=0):
        '''
        Reset the video source and start from the beginning.
        '''
        self.vid = cv2.VideoCapture(vidsource)

    def __del__(self):
        '''
        Release the video when the window is closed.
        '''
        if self.vid.isOpened():
            self.vid.release()

class player:
    def __init__(self, master, scale, vidsource=0):
        '''
        Defines the video player window.

        :param master: root window
        :type master: Tk
        :param scale: the scale of which the video is being played. The higher the number, the bigger the video
        :type scale: integer
        :param vidsource: the file path of the video
        :type vidsource: string
        '''
        # Variable declaration

        self.master = master
        self.master.resizable(False, False)

        self.video_source = vidsource
        self.vid = VidCap(scale, self.video_source)

        # Frame
        # Content: canvas : Canvas
        #          restart: Button

        self.frame = Frame(self.master)
        self.canvas = Canvas(self.frame, width = self.vid.get_width() * scale, height = self.vid.get_height() * scale) # Set video canvas and apply scaling
        self.canvas.pack()
        
        self.restart = Button(self.frame, text = 'Replay', width = 15, command = self.restart_vid) # Set button for restartng the video 
        self.restart.pack()

        self.update()

        self.frame.pack()

    def update(self):
        '''
        Update the video canvas to display the next frame.
        '''
        start = time() # Record start time
        ret = False
        for i in range(int(self.vid.get_fps())):
            ret, frame = self.vid.get_frame()
        if ret:
            self.canvas.delete("all")
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
            self.process_time = round(1000*(time() - start)) # Calculate process time
        self.master.after(1000 - self.process_time, self.update)
        # Recall itself every slide, i.e. one second, including process time
        # Reduce the effect of lag from processing by reducing process time from the wait time

    def restart_vid(self):
        '''
        Replay the video.
        '''
        self.vid.reset(self.video_source) # Reset the video

    def close_windows(self):
        '''
        Destroy the root window.
        '''
        self.master.destroy()