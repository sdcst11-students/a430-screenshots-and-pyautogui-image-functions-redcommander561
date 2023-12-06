
import time
import pyautogui
import keyboard

    

    #825,404 is location of cookie
    #1240,573 is location of clicker upgrade
    #1244,633 is location of grandma

    #
#1229, 636
#1231,700




clicks = 0
def click():
    time.sleep(0.3)
    pyautogui.click()
    
    


def clickCookie():
    time.sleep(1)
    print('clicking cookies')
    pyautogui.moveTo(230, 406)

    for i in range(0,6):
        click()


def upgrade():
    print('regular upgrade')
    pyautogui.moveTo(1229,636)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.moveTo(1231,700)
    time.sleep(0.5)
    pyautogui.click()
    
    
    #127,125,116
        



    
    

    
        
        
        
        
def main():
    pyautogui.alert("Ready to play?")
    
main()   
while True:
    
    clickCookie()
    upgrade()
    
    
    


