from secrets import username, password
from selenium import webdriver
from time import sleep

class BadooBot():
    def __init__(self):
        self.driver = webdriver.Chrome("./Driver/chromedriver")
        self.driver.get("https://badoo.com/fr/")

        sleep(2)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div[2]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')
        fb_btn.click()

        sleep(2)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(2)
        try:
            log_btn = self.driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button')
            log_btn.click()
        except Exception:
            sleep(2)
            self.driver.switch_to_window(base_window)


        

    def like(self):
        self.driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')\
            .click()
    
    def close_popup1(self):
        self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/div/div[1]')\
            .click()

    def close_popup2(self):
        self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[3]/span')\
            .click()
    def close_popup3(self):
        self.driver.find_element_by_xpath('//*[@id="simple-page"]/div[3]/section/div[2]/div')\
            .click()
    def autolike(self):
        go = True
        while go:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                sleep(2)
                try:
                    self.close_popup1()
                except Exception:
                    try:
                        self.close_popup2()
                    except Exception:
                        self.close_popup3()

if __name__ == "__main__":
    bot = BadooBot()
    sleep(5)
    bot.autolike()