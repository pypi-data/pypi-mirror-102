import glob
import multiprocessing
import numpy as np
import os
import segno
import sys
import tempfile
import moblabpy.moblabgui as mgui
import tkinter as tk
from ctypes import c_bool, c_char, c_wchar_p, c_int
from cv2 import cv2
from math import ceil, floor, sqrt
from pyzbar.pyzbar import decode, ZBarSymbol
from time import time
from PIL import Image, ImageDraw, ImageFont

class PROPS():
    '''
    A class which contains all the properities for :class:`MobLabPy` object
    '''
    FPS = 15
    BPS = 16
    ROW = COL = int(sqrt(BPS))
    INFO_BIT_SIZE = 200 // ROW
    START_BIT = END_BIT = "0"
    VID_SOURCE = f'./{BPS}bps.mp4'
    SCALE = 2

    def set_BPS(bps):
        '''
        Set the bps property of the video and other related properties. 

        :param bps: the bps want to set. It must be able to be perfect squared, such as 16, 25, 36...
        :type bps: integer
        '''
        PROPS.BPS = bps
        PROPS.ROW = PROPS.COL = int(sqrt(bps))
        PROPS.INFO_BIT_SIZE = 200 // PROPS.ROW
        

class MobLabPy:
    '''
    A moblabpy object allows users to connect their ip camera with the program to simulate a telecommunication system.

    :param ip_address: the ip address of the IP camera
    :type ip_address: string
    :param bit_mess: the transmitted bit sequence
    :type bit_mess: string
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    '''
    def __init__(self, ip_address, bit_mess, props = PROPS):
        self.__sender, self.__recver = multiprocessing.Pipe()
        self.ip_adress = ip_address
        self.bit_mess = "".join(map(str, bit_mess))
        self.vid_source = props.VID_SOURCE
        self.is__pilot_bit_found = multiprocessing.Value(c_bool, False)
        self.is__button_pressed = multiprocessing.Value(c_bool, False)
        self.__fps = multiprocessing.Value(c_int, 0)
        self.__bit_seq = multiprocessing.Value(c_wchar_p, "")
        self.__sender_func = multiprocessing.Process(target = send_frame, args = (self.__fps, self.is__pilot_bit_found, self.__sender, self.ip_adress))
        self.__vid_player = multiprocessing.Process(target = vid_player, args = (self.vid_source, self.is__button_pressed))
    
    def start(self):
        '''
        Start to get frame from the ip camera and send it to a decoding function.
        '''
        self.__sender_func.start()
        self.__vid_player.start()

        recv_frame(self.__fps, self.is__pilot_bit_found, self.__recver, self.__bit_seq, self.is__button_pressed, self.bit_mess)

        self.__sender_func.join()
    
    def get_bit_seq(self):
        '''
        Return the bit sequence of the MobLabPy class.

        :returns bit_seq: the received bit sequence
        :rtype: list
        '''
        # bit_arr = np.array(list(self.__bit_seq.value), dtype = int)
        bit_seq = list(self.__bit_seq.value)
        return bit_seq

def img_to_bit_seq(frame, pt1 = (), pt2 = (), props = PROPS):
    '''
    Convert black and white color to "0" and "1" respectively.

    :param frame: Image.
    :type frame: ndarray
    :param pt1: vertex of the area bounded by qr codes.
    :type pt1: tuple, defaults to ()
    :param pt2: vertex of the area bounded by qr codes opposite to pt1.
    :type pt2: tuple, defaults to ()
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    :returns bit_seq, pt1, pt2: Decoded bit sequence and vertices of the area bounded by qr codes in opposite direction.
    :rtype: string, tuple, tuple
    :raises IndexError: fail to calculate the mean of the RGB of the color matrix
    '''
    bit_seq = ""
    grey_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, pt1, pt2 = find_corner(grey_scale)
    try:
        crop_img = grey_scale[pt1[1]-10:pt2[1]+10, pt1[0]-10:pt2[0]+10]
        # color_img = cv2.cvtColor(crop_img, cv2.COLOR_GRAY2BGR)
        ### decode color bits one by one
        height, width = crop_img.shape
        th = 120
        info_bit_size = ceil(max(height/(props.ROW*2), width/(props.COL*2)))
        offset = ceil(max(height/4, width/4))
        for i in range(props.ROW):
            for j in range(props.COL):
                ### decode color bits
                info_bits_area = crop_img[offset + info_bit_size * i:offset + info_bit_size * (i + 1), offset + info_bit_size * j:offset + info_bit_size * (j + 1)]
                # cv2.rectangle(color_img, (offset + info_bit_size * j, offset + info_bit_size * i), (offset + info_bit_size * (j + 1), offset + info_bit_size * (i + 1)), (0, 255, 0), 1)
                _, th1 = cv2.threshold(info_bits_area, th, 255, cv2.THRESH_BINARY)
                try:
                    if np.mean(th1) >= th:
                        bit_seq += "1"
                    else:
                        bit_seq += "0"
                except TypeError:
                        bit_seq += "0"
        # cv2.imwrite(f"./detection/{bit_seq}.png", color_img)
        # bit_arr = np.array(list(bit_seq))
        return bit_seq, pt1, pt2
    except IndexError:
        print("Synchronization failed. Please restart the program")
        exit(0)

def check_orientation(frame, pt1, pt2):
    '''
    Check the orientation of the image according to the qr codes in the corner.

    :param frame: image
    :type frame: ndarray
    :param pt1: vertex of the area bounded by qr codes.
    :type pt1: tuple
    :param pt2: vertex of the area bounded by qr codes opposite to pt1.
    :type pt2: tuple
    :return result: number of rotation needed to be performed
    :rtype: integer
    :raises IndexError: fail to find the qr codes
    '''
    size = ceil(max((pt2[1]-pt1[1])/4, (pt2[0]-pt1[0])/4))
    height, width, _ = frame.shape
    finder_pattern_order = np.zeros(4, dtype = int)
    ### decode top left corner
    qr_codes = decode(frame[0:pt1[1]+size*2, 0:pt1[0]+size*2, :], symbols=[ZBarSymbol.QRCODE])
    if (len(qr_codes) == 1):
        finder_pattern_order[0] = qr_codes[0].data.decode("utf-8")
    else:
        finder_pattern_order[0] = 10
    ### decode bottom left corner
    qr_codes = decode(frame[pt2[1]-size*2:height, 0:pt1[0]+size*2, :], symbols=[ZBarSymbol.QRCODE])
    if (len(qr_codes) == 1):
        finder_pattern_order[1] = qr_codes[0].data.decode("utf-8")
    else:
        finder_pattern_order[1] = 10
    ### decode bottom right
    qr_codes = decode(frame[pt2[1]-size*2:height, pt2[0]-size*2:width, :], symbols=[ZBarSymbol.QRCODE])
    if (len(qr_codes) == 1):
        finder_pattern_order[2] = qr_codes[0].data.decode("utf-8")
    else:
        finder_pattern_order[2] = 10
    ### decode top right
    qr_codes = decode(frame[0:pt1[1]+size*2, pt2[0]-size*2:width, :], symbols=[ZBarSymbol.QRCODE])  
    if (len(qr_codes) == 1):
        finder_pattern_order[3] = qr_codes[0].data.decode("utf-8")
    else:
        finder_pattern_order[3] = 10
    
    result = np.where(finder_pattern_order == 1)
    try:
        return ((4 - result[0][0]) % 4)
    except IndexError:
        return 0

def point_rotation(pt1, pt2, width, rotation):
    '''
    Perform the rotation of vertices of the color matrix area.

    :param pt1: vertex of the color matrix
    :type pt1: tuple
    :param pt2: vertex of the color matrix opposite to pt1
    :type pt2: tuple
    :param width: width of the image that contains the color matrix
    :type: integer
    :param rotation: number of rotation that needed to be performed
    :type rotation: integer
    :returns pt1, pt2: vertices of the color matrix area after rotation
    :type: tuple
    '''
    for _ in range(rotation):
        pt1 = (pt1[1], width - pt2[0])
        pt2 = (pt2[1], width - pt1[0])
    return pt1, pt2

# Parameters: frame: array-like
#             pt1, pt2: tuples
# Returns:    size: int
#             pt1, pt2: tuples
def find_corner(frame, pt1 = (), pt2 = ()):
    '''
    Find the vertex of the color matrix surrounded by but exclude qr codes.

    :param frame: image
    :type frame: ndarray
    :param pt1: vertex of the area include qr codes
    :type pt1: tuple, defaults to ()
    :prarm pt2: vertex of the area include qr codes opposite to pt1
    :type pt2: tuple, defaults to ()
    :returns size, pt1, pt2: size of the color matrix area and its vertices in opposite direction
    :rtype: integer, tuple, tuple
    '''
    qr_codes = decode(frame, symbols = [ZBarSymbol.QRCODE])
    size = 0
    if qr_codes:
        pt1 = min(qr_codes[0].polygon)
        pt2 = max(qr_codes[0].polygon)
        ### find the area surronded by the four qr codes
        for qrCode in qr_codes:
            (pt1x, pt1y), (pt2x, pt2y) = find_min_and_max(qrCode.polygon, pt1, pt2)
            pt1 = (pt1x, pt1y)
            pt2 = (pt2x, pt2y)
            size = max(size, (pt2x - pt1x), (pt2y - pt1y))
    return size, pt1, pt2

def find_min_and_max(points, min_pt, max_pt):
    '''
    Find the minimum and maximum xy-points in a list and the provides points.

    :param points: a list of points
    :type points: list
    :param min_pt: the minimum points provided
    :type min_pt: list
    :param max_pt: the maximum points provided
    :type max_pt: list
    :returns min_pt, max_pt: the minimum and maximum xy-points
    :rtype: tuple, tuple
    '''
    min_pt = np.array(min_pt)
    max_pt = np.array(max_pt)

    for point in points:
        if min_pt[0] > point[0]:
            min_pt[0] = point[0]
        elif max_pt[0] < point[0]:
            max_pt[0] = point[0]
        if min_pt[1] > point[1]:
            min_pt[1] = point[1]
        elif max_pt[1] < point[1]:
            max_pt[1] = point[1]
    return min_pt, max_pt

def all_zeros_or_ones(bit_seq):
    '''
    Check if the bit sequence contains only 0 or 1.

    :param bit_seq: the bit sequence needed to be checked
    :type bit_seq: string
    :return: "True" if the bit sequence only contains 0 or 1, "False" otherwise
    :rtype: bool
    :raises ValueError: input contains non numerical values
    '''
    try:
        bit_seq = np.array(list(bit_seq), dtype = int)
        if (np.count_nonzero(bit_seq) == 0) or (np.count_nonzero(bit_seq) == bit_seq.shape[0]):
            return True
        return False
    except ValueError:
        bit_seq = np.array(list(bit_seq), dtype = c_char)
        _, count = np.unique(bit_seq, return_counts = True)
        if count == bit_seq.shape[0]:
            return True
        return False

def str_to_ascii_seq(my_str = "Apple"):
    '''
    Convert each character in a string to its corresponding ascii code.

    :param my_str: the string wanted to be converted
    :type my_str: string, defaults to Apple
    :return ascii_arr: a list of integer that contains all the ascii code of each character in my_str
    :rtype: list
    '''
    ascii_arr = np.zeros(len(my_str), dtype=int)
    i = 0
    # convert char by char
    for ch in my_str:
        ascii_arr[i] = ord(ch)
        i += 1
    # return all the corresponding ascii code
    return ascii_arr

def ascii_seq_to_bit_seq(ascii_arr):
    '''
    Convert a list of ascii code to its binary representation.

    :param ascii_arr: a list that contains ascii code
    :type ascii_arr: list
    :return bit_arr: an integer binary list
    :rtype: list
    '''
    bit_str = ""
    # convert decimal ascii code to binary one by one
    for num in range(len(ascii_arr)):
        info_bits = np.binary_repr(ascii_arr[num]).zfill(8)
        bit_str += info_bits
    bit_arr = np.array(list(bit_str), dtype=int)
    return bit_arr

def bit_seq_to_ascii_seq(bit_arr):
    '''
    Perform byte conversion of an array.

    :param bit_arr: an integer binary array
    :type bit_arr: list
    :return ascii_arr: a list contains all the corresponding ascii code
    :rtype: list
    '''
    bit_arr = "".join(map(str, bit_arr))
    if (len(bit_arr) < 8):
        byte_size = len(bit_arr)
    else:
        byte_size = 8
    ascii_arr = np.empty(int(len(bit_arr)/byte_size), dtype=int)
    num_of_byte = int(len(bit_arr) / byte_size)
    for i in range(num_of_byte):
        try:
            ascii_arr[i] = int(bit_arr[i*byte_size: (i+1)*byte_size], 2)
        except ValueError:
            a = bit_arr[i*byte_size: (i+1)*byte_size].replace("e", "0")
            ascii_arr[i] = int(a, 2)
    return ascii_arr

def ascii_seq_to_str(ascii_arr):
    '''
    Convert a list of ascii code to its corresponding character.

    :param ascii_arr: a list that contains ascii code
    :type ascii_arr: list
    :return my_str: the character format of the ascii list
    :rtype: string
    '''    
    my_str = ""
    for ascii_code in ascii_arr:
        my_str += chr(ascii_code)
    return my_str

def append_zeros(bit_seq, props = PROPS):
    '''
    Append zeros until the length of the input equals to the products of desired length.

    :param bit_seq: integer binary array
    :type bit_seq: list
    :param props: the PROPS object that contains the properties of the program.
    :type props: :class:`PROPS`
    :return bit_arr: an integer binary array which length is the product of the second parameter
    :rtype: list(int)
    '''  
    remain = props.BPS - len(bit_seq) % props.BPS
    bit_seq = "".join(map(str, bit_seq))
    if len(bit_seq) % props.BPS != 0:
        for _ in range(remain):
            bit_seq += "0"
    bit_arr = np.array(list(bit_seq), dtype = int)
    return bit_arr

def generate_img(dir_name, my_str = "Hello World", if_bin = False, props = PROPS):
    '''
    Generate images that contain color matrix of my_str parameter, with black represents 0 and white represents 1, and
    paste them with the qr codes (finder patterns) together. The generated images will be saved at the dir_name 
    directory.

    :param dir_name: the directory name used to save the image generated
    :type dir_name: string
    :param my_str: the integer binary array which will be convert to color code formats
    :type my_str: string, list, defaults to "Hello World"
    :param if_bin: "True" if my_str is an integer binary array, "False" otherwise
    :type if_bin: bool, defaults to False
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    '''
    # generate a temp file and store in the temp dir
    try:
        os.makedirs(dir_name)
    except FileExistsError:
        # print("Directory already exists")
        pass

    if if_bin:
        bit_seq = append_zeros(my_str)
    else:
        ascii_seq = str_to_ascii_seq(my_str)
        bit_seq = ascii_seq_to_bit_seq(ascii_seq)
        bit_seq = append_zeros(bit_seq)

    for i in range(int(len(bit_seq) / props.BPS)):
        width = height = 400
        img = np.zeros([width, height, 3])
        info_bits_area = np.zeros([width//2, height//2, 3])
        # append finder pattern
        finder_pattern_list = []
        for _ in range(4):
            finder_pattern = cv2.imread(f"./res/finderPattern{_ + 1}.png")
            finder_pattern_list.append(finder_pattern)
        size = finder_pattern_list[0].shape[0]
        img[0:size, 0:size, :] = finder_pattern_list[0]
        img[height - size:height, 0:size, :] = finder_pattern_list[1]
        img[height - size:height, height - size:height, :] = finder_pattern_list[2]
        img[0:size, width - size:width, :] = finder_pattern_list[3]
        for j in range(props.ROW):
            for k in range(props.COL):
                info_bit = np.ones([props.INFO_BIT_SIZE, props.INFO_BIT_SIZE, 3], dtype=int) * int(bit_seq[i * props.BPS + props.ROW * j + k]) * 255
                info_bit = np.array(info_bit, np.uint8)
                info_bits_area[props.INFO_BIT_SIZE * j: props.INFO_BIT_SIZE * (j + 1), props.INFO_BIT_SIZE * k:props.INFO_BIT_SIZE * (k + 1), :] = info_bit
        img[height // 4: height * 3 // 4, width // 4: width * 3 // 4, :] = info_bits_area
        cv2.imwrite(f"{dir_name}/{i}.png", img)

def generate_res():
    '''
    Generate the res folder which contains all the head and end messages, start and end signals and finder patterns.
    '''
    try:
        os.makedirs("./res")
    except FileExistsError:
        pass
    # generate finder patterns
    for i in range(4):
        finder_pattern = segno.make(f"{i + 1}", micro=False, error="H")
        finder_pattern.save(f"./res/finderPattern{i + 1}.png", border = 2, scale = 4)
    # generate start and end signal
    pilot_bit = segno.make("0", micro=False, error="H")
    pilot_bit.save("./res/pilotBit.png", border = 2, scale = 16)
    # generate head message
    text = "Transmission starting..."
    unicode_font = ImageFont.truetype("arial.ttf", 34)
    index_font = ImageFont.truetype("arial.ttf", 102)
    width, height = unicode_font.getsize(text)
    for i in range(4):
        index_w, index_h = index_font.getsize(str(i))
        im = Image.new("RGB", (400,400), (255,255,255))
        draw = ImageDraw.Draw(im)
        draw.text(((400 - width)//2, (400 - height)//2), text, font=unicode_font, fill=(0,0,0))
        draw.rectangle(((120, (400 + height)//2), (280, (400 + height)//2 + 160)), outline=(0,0,0), width=3)
        draw.text(((400 - index_w)//2, (((400 + height)//2 + 160 + (400 + height)//2)-index_h)//2), str(i), font=index_font, fill=(0,0,0))
        im.save(f"./res/Head-{i}.png")
    # generate tail message
    text = "Transmission finished"
    im = Image.new("RGB", (400,400), (255,255,255))
    draw = ImageDraw.Draw(im)
    draw.text(((400 - width)//2, (400 - height)//2), text, font=unicode_font, fill=(0,0,0))
    im.save(f"./res/Tail.png")

def generate_video(video_name = f"{PROPS.BPS}bps.mp4", mystr = "Hello World", if_bin = False, props = PROPS):
    '''
    Generate a video which contains start and end messages, start and end signals, finder patterns and color matrix
    of the mystr parameter, with desired fps.

    :param video_name: The name of the generated video in mp4 format
    :type video_name: string
    :param mystr: the message that will be converted to color code
    :type mystr: string, defaults to "Hello World"
    :param if_bin: "True" if mystr is an integer binary array, "False" otherwise
    :type if_bin: bool, defaults to False
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    '''
    if (video_name.find(".mp4") == -1):
        video_name = "video.mp4"

    generate_res()
    props.VID_SOURCE = video_name
    width = height = 400
    size = (width, height)

    # create a temp dir to store the temp img generated
    temp_dir = tempfile.TemporaryDirectory(dir = "./")

    # generate qr code for the whole string
    generate_img(temp_dir.name, mystr, if_bin)

    info_bit_list = sorted(glob.glob(temp_dir.name + "/*.png"), key = os.path.getmtime)

    # videoWriter set up
    ### .mp4
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(video_name, fourcc, props.FPS, size)

    ### get head img
    head = []
    for filename in glob.glob("./res/Head-*.png"):
        img = cv2.imread(filename)
        head.append(img)

    ### add head img
    for i in range(4):
        for _ in range(props.FPS):
            out.write(head[i])

    ### add start bit
    pilot_bit = cv2.imread("./res/pilotBit.png")
    for _ in range(props.FPS * 2):
        out.write(pilot_bit)

    ### add info bits
    for filename in info_bit_list:
        info_bit = cv2.imread(filename)
        for _ in range(props.FPS):
            out.write(info_bit)

    ### add end bit
    for _ in range(props.FPS * 2):
        out.write(pilot_bit)

    ### add tail img
    tail = cv2.imread("./res/Tail.png")
    for _ in range(props.FPS):
        out.write(tail)

    # generate the video and clean up the temp dir
    out.release()
    temp_dir.cleanup()

def recv_frame(fps, is_pilot_bit_found , recver, bit_seq, flag, bit_mess, props = PROPS):
    '''
    Funtion that received frames from the sender function. It does all the manipulation of the captured iamge
    here, such as detecting start and end signals, checking rotations and decoding color codes back to 0 and 1.

    :param fps: a :class:`multiprocessing.sharedctypes.Synchronized` object which represents the fps of the camera
    :type fps: :class:`multiprocessing.sharedctypes.Synchronized`
    :param is_pilot_bit_found: a :class:`multiprocessing.sharedctypes.Synchronized` object which is `True` if the start signal is detected, `False` otherwise
    :type is_pilot_bit_found: :class:`multiprocessing.sharedctypes.Synchronized`
    :param recver: a :class:`multiprocessing.Pipe()` object that received images sent from the sender function
    :type recver: :class:`multiprocessing.Pipe()`
    :param bit_seq: a :class:`multiprocessing.sharedctypes.Synchronized` object whcih is the decoded bit sequence of received images 
    :type bit_seq: :class:`multiprocessing.sharedctypes.Synchronized`
    :param flag: a :class:`multiprocessing.sharedctypes.Synchronized` object which is the state of the play video button
    :type flag: :class:`multiprocessing.sharedctypes.Synchronized`
    :param bit_mess: the transmitted bit sequence
    :type bit_mess: list
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    '''
    frame_count = 0
    idx_info_bit = 0
    is_info_bit_detected = False

    root = tk.Tk()
    root.title("moblab monitor")
    gui = mgui.monitor(root, bit_mess)


    while not(is_pilot_bit_found.value):
        flag.value = gui.get_button_status()
        root.update()
        root.update_idletasks()

    while is_pilot_bit_found.value:
        frame = recver.recv()
        # if info bit is not detected
        if not(is_info_bit_detected):
            qr_codes = decode(frame, symbols = [ZBarSymbol.QRCODE])
            if qr_codes and qr_codes[0].data.decode("utf-8") != props.START_BIT:
                is_info_bit_detected = True
                _, pt1, pt2 = img_to_bit_seq(frame)
                idx_info_bit = 0
        elif idx_info_bit % fps.value == floor(fps.value / 2):
            qr_codes = decode(frame, symbols=[ZBarSymbol.QRCODE])
            if qr_codes and qr_codes[0].data.decode("utf-8") == props.END_BIT:
                recver.close()
                is_pilot_bit_found.value = False
                break
            else:
                _, pt1, pt2 = img_to_bit_seq(frame, pt1, pt2)
                rotation_time = check_orientation(frame, pt1, pt2)
                _, width, _ = frame.shape
                pt1, pt2 = point_rotation(pt1, pt2, width, rotation_time)
                frame = np.rot90(frame, rotation_time)
                # cv2.imwrite(f"./frame/{frame_count}.png", frame)
                decoded_bit_seq, pt1, pt2 = img_to_bit_seq(frame, pt1, pt2)
                if all_zeros_or_ones(decoded_bit_seq):
                    is_pilot_bit_found.value = False
                    break
                bit_seq.value += decoded_bit_seq
                gui.update_recv(decoded_bit_seq)

        flag.value = gui.get_button_status()
        root.update()
        root.update_idletasks()
        frame_count += 1
        idx_info_bit += 1

    # ascii_seq = bit_seq_to_ascii_seq(bit_seq.value)
    # my_str = ascii_seq_to_str(ascii_seq)
    # print(f"bit_seq: {bit_seq.value}")
    # print(f"ascii_seq: {ascii_seq}")
    # print(f"my_str: {my_str}")
    root.mainloop()

def vid_player(vid_source, flag, props = PROPS):
    '''
    A video player will be appeared if the play video button is clicked

    :param vid_source: the name of the video to pe played
    :type vid_source: string
    :param flag: a :class:`multiprocessing.sharedctypes.Synchronized` object which is the state of the play video button
    :type flag: :class:`multiprocessing.sharedctypes.Synchronized`
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    '''
    root = tk.Tk()
    root.title("moblab video player")
    while not(flag.value):
        pass
    _ = mgui.player(root, props.SCALE, vid_source)
    root.mainloop()

def send_frame(fps, is_pilot_bit_found, sender, ip_address, props = PROPS):
    '''
    A sender function which gets images from the connected camera and send it to the receiver function.

    :param fps: a :class:`multiprocessing.sharedctypes.Synchronized` object which represents the fps of the camera
    :type fps: :class:`multiprocessing.sharedctypes.Synchronized`
    :param is_pilot_bit_found: a :class:`multiprocessing.sharedctypes.Synchronized` object which is `True` if the start signal is detected, `False` otherwise
    :type is_pilot_bit_found: :class:`multiprocessing.sharedctypes.Synchronized`
    :param sender: a :class:`multiprocessing.Pipe()` object that send images captured by the connected camera
    :type sender: :class:`multiprocessing.Pipe()`
    :param ip_address: ip address of the camera that is going to be connected
    :type ip_address: string
    :param props: the PROPS object that contains the properties of the program
    :type props: :class:`PROPS`
    '''
    cam = cv2.VideoCapture(ip_address)
    print("IP camera is connected")

    start = time()
    end = time()
    num_frames = 0

    while (end - start < 3):
        _, _ = cam.read()
        end = time()
        num_frames += 1

    seconds = end - start
    calculated_fps = num_frames / seconds
    print(f"{num_frames} frames are taken in {seconds}s")
    print(f"FPS is {round(calculated_fps)}")
    fps.value = round(calculated_fps)

    print("Detecting start signal")
    while not(is_pilot_bit_found.value):
        _, frame = cam.read()
        qr_codes = decode(frame, symbols = [ZBarSymbol.QRCODE])
        if qr_codes and qr_codes[0].data.decode("utf-8") == props.START_BIT:
            is_pilot_bit_found.value = True
    print("Start signal is detected. Start transmittion...")

    count = 0
    while is_pilot_bit_found.value:
        _, frame = cam.read()
        try:
            sender.send(frame)
        except BrokenPipeError:
            break
        # cv2.imwrite(f"./recordFrame/{count}.png", frame)
        count += 1

    print("\nTransmission finished")
    cam.release()

def encode(D, G):
    '''
    Perform matrix multiplication on parameter D and G, which is D x G.

    :param D: a 1 x k matrix
    :type D: list
    :param G: a generator matrix
    :type G: ndarray
    :return C: a 1 x n matrix
    :rtype: ndarray
    :raises ValueError: The number of columns in the first matrix must be equal to the number of rows in the second matrix
    :raises np.core._exceptions.UFuncTypeError: Both parameters must be integer ndarray
    '''
    G = np.array(G, dtype = int)
    C = np.zeros((G.shape[1] * len(D)//G.shape[0]), dtype = int)
    try:
        for i in range(len(D)//G.shape[0]):
            C[i * G.shape[1]: (i + 1) * G.shape[1]] = np.matmul(D[i * G.shape[0]: (i + 1) * G.shape[0]], G, dtype = int) % 2
        return C
    except ValueError:
        raise Exception("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
    except np.core._exceptions.UFuncTypeError:
        raise Exception("Both parameters must be integer ndarray")

# Parameters: R, H: integer ndarray
# Returns:    S: integer ndarray
def syndrome(R, H):
    '''
    Calculate the syndrome of the received bit sequence.

    :param R: a 1 x n matrix
    :type R: list
    :param H: a parity check matrix
    :type H: ndarray
    '''
    R = np.array(R, dtype = int)
    H_T = np.transpose(H)
    S = np.zeros((H_T.shape[1] * len(R)//H_T.shape[0]), dtype = int)
    try:
        for i in range(len(R)//H_T.shape[0]):
            S[i * H_T.shape[1]: (i + 1) * H_T.shape[1]] = np.matmul(R[i * H_T.shape[0]: (i + 1) * H_T.shape[0]], H_T, dtype = int) % 2
        return S
    except ValueError:
        raise Exception("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
    except np.core._exceptions.UFuncTypeError:
        raise Exception("Both parameters must be integer ndarray")

if __name__ == "__main__":
    # message = "University of Science and Technology"
    # ascii_seq = str_to_ascii_seq(message)
    # bit_seq = ascii_seq_to_bit_seq(ascii_seq)
    # bit_mess = append_zeros(bit_seq, PROPS)
    # # generate_video(mystr=bit_mess, if_bin=True)
    # cam = MobLabPy("http://192.168.3.24:8081", bit_mess)
    # cam.start()
    # recv_bit_seq = cam.get_bit_seq()
    # recv_ascii_seq = bit_seq_to_ascii_seq(recv_bit_seq)
    # recv_message = ascii_seq_to_str(recv_ascii_seq)
    # print(recv_message)
    print(sys.path)
    pass