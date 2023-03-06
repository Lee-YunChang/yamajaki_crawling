from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from slack_sdk import WebhookClient
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(3)

driver.get('https://www.suntory.co.jp/factory/yamazaki/')
driver.find_element(By.ID, 'tour_reserve').click()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, r'//*[@id="main_contents_r"]/article[1]').click()
driver.implicitly_wait(50)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data1 = soup.select('#calendarTable-body-2 > tr > td > a > span')
data = soup.select_one('#calendarTable-body-2 > tr:nth-child(2) > td:nth-child(6) > a > span')

webhook_url = 'https://hooks.slack.com/services/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'
slack_webhook = WebhookClient(url=webhook_url)
slack_webhook.send(text="yamajaki crawling test")

