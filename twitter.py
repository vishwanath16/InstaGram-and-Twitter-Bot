from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login/')
        time.sleep(6)
        email = bot.find_element_by_css_selector(".js-username-field")
        print("Passed")
        time.sleep(3)
        email.send_keys(self.username)
        password = bot.find_element_by_css_selector('.js-password-field')
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(10)
        for i in range(1, 30):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements(By.XPATH, '//*[@data-testid="tweet"]//a[@dir="auto"]')
            links = [elem.get_attribute('href') for elem in tweets]
            print(links)
            for link in links:
                bot.get(link)
                time.sleep(3)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(10)

vi = TwitterBot('','') #Enter your email and password
vi.login()
vi.like_tweet('') #Enter the hashtag that you want to search
