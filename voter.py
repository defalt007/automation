import pyautogui
import time

url = ""
no_of_votes =                                     #How many times to vote

#print(pyautogui.position())            #Change the X,Y coordinates accordingly

#Opening the website                    #Three clicks to select the entire url and replace it with this
pyautogui.click(736, 66)                #x,y coordinates of the address bar of your browser (TOR)
pyautogui.click(736, 66)
pyautogui.click(736, 66)
pyautogui.typewrite(url)
pyautogui.typewrite(["enter"])

#loop to do it n times
for i in range(no_of_votes):

    #waiting for the site to load
    time.sleep(15)                     #adjust as per requirement, for staying safe from cloudflare use ~15 sec
    
    #clicking on the vote button
    pyautogui.click(940, 787)          #adjust the x,y coordinates as per the vote button
    time.sleep(5)                      #adjust as per requirement, for staying safe from cloudflare use ~5 sec
    
    #getting a new user id             #TOR creates a new chain for the current site
    pyautogui.click(1896, 62)          #Clicks on the hamburger menu
    time.sleep(0.4)
    pyautogui.click(1896, 182)         #Clicks on generate new chain for the website
