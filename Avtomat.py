import webbrowser
import pyautogui

class Config:

    def Get(name_cfg):
        file = open(name_cfg, "r")
        for i in (file.read()).split('\n'):
            st = str(i[0]).split(" ")

            if st[0] == 'open':
                webbrowser.open_new_tab('https://www.google.ru/search?q={}'.format(st[1]))

            if st[0] == 'press':
                pyautogui.keyDown(st[1])
                pyautogui.keyUp(st[1])
            
            if st[0] == '__exit__':
                pyautogui.keyDown('Alt')
                pyautogui.keyDown('F4')
                pyautogui.keyUp('F4')
                pyautogui.keyUp('Alt')

            

