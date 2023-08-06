from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class JoinHandler:
    def __init__(self, pin):
        self.op = Options()

        self.op.add_argument('--headless --no-sandbox --disable-gpu --disable-dev-shm-usage')

        self.drv = webdriver.Chrome(options=self.op)
        self.pin = pin

        self.drv.get('https://kahoot.it')

    def create_clients(self, num):
        for i in range(1,num+1):
            self.drv.execute_script('window.open("https://kahoot.it")')

        self.tabs = self.drv.window_handles

    def join_clients(self, name, onerror=None):
        num = 0
        
        for idr in self.tabs:
            num+=1
            self.drv.switch_to.window(idr)
            time.sleep(0.3)
            gameid = self.drv.find_element_by_xpath('//*[@id="game-input"]')
            gamebutton = self.drv.find_element_by_xpath('//*[@id="root"]/div[1]/div/main/div[2]/main/div/form/button')

            gameid.send_keys(self.pin)
            gamebutton.click()
            time.sleep(0.8)
            try:
                nick = self.drv.find_element_by_xpath('//*[@id="nickname"]')
                nickbutton = self.drv.find_element_by_xpath('//*[@id="root"]/div[1]/div/main/div[2]/main/div/form/button')
                nick.send_keys(f'{name}{num - 1}')
                nickbutton.click()
            except:
                if onerror == None:
                    pass
                else:
                    onerror()
                    pass
                

    def leave(self):
        for idr in self.tabs:
            self.drv.switch_to.window(idr)
            self.drv.close()
            
        self.drv.quit()
