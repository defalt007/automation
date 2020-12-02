#Automatic recommendation sender to the profile (LinkedIn)
#as a fallsafe if script goes unresponsive, take your cursor to anycorner of the screen
import pyautogui
import time

connectbutpoint = pyautogui.locateCenterOnScreen('plus.png', confidence =0.8)

while True:

    connectbutlocation = pyautogui.locateOnScreen('plus.png', confidence =0.8)
    connectbutpoint = pyautogui.center(connectbutlocation)
    pyautogui.click(connectbutpoint) #click on plus button
    time.sleep(1.4)  #giving the time to browser to render the recommendation popup
    notebutpoint = pyautogui.locateCenterOnScreen('hs.png', confidence =0.8) #locate the highly skilled button
    pyautogui.click(notebutpoint)  #click on highly skilled button
    sendbutpoint = pyautogui.locateCenterOnScreen('sar.png', confidence =0.8) #locate the relation button
    pyautogui.click(sendbutpoint) #click on how do you know button
    sbutpoint = pyautogui.locateCenterOnScreen('workedtogether.png', confidence =0.8) #locate the worked together button
    pyautogui.click(sbutpoint)
    sndbutpoint = pyautogui.locateCenterOnScreen('submit.png', confidence =0.8) #locate the submit button
    pyautogui.click(sndbutpoint)
    time.sleep(1)   #a one second delay just so that linkedin does not consider you a bot spitting connect requests 
                    #also helps in the fallsafe 
     

#defalt007
