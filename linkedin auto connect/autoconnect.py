#Automatic connection request sender to the search results (LinkedIn)
#as a fallsafe if script goes unresponsive, take your cursor to anycorner of the screen
import sys, subprocess
try:
    import time
    import pyautogui
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    
    import pyautogui

message = '''Hi, Hope you are doing great.
I would love to add you in my professional network.
Thank you'''

while True:

    connectbutlocation = pyautogui.locateOnScreen('connectbut2.PNG', confidence =0.8) #locate the connect button
    connectbutpoint = pyautogui.center(connectbutlocation)     #give the co-ordinates to our variable
    pyautogui.click(connectbutpoint) #click on connect button
    time.sleep(2)  #giving the time to browser to letrender the addnote popup
    notebutpoint = pyautogui.locateCenterOnScreen('notebut.png', confidence =0.8) #locate the add note button
    pyautogui.click(notebutpoint)  #click on add note button button
    time.sleep(1)

    pyautogui.write(message) #to input the designated message
    time.sleep(1)

    sendbutpoint = pyautogui.locateCenterOnScreen('send.PNG', confidence =0.8) #locate the send invitation button
    pyautogui.click(sendbutpoint) #click on send invitation button

    time.sleep(1)   #a one second delay just so that linkedin does not consider you a bot spitting connect requests
                    #also helps in the fallsafe

#defalt007
