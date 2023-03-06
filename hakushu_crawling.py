from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from slack_sdk import WebhookClient
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.implicitly_wait(3)

driver.get('https://www.suntory.co.jp/factory/hakushu/')
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

slack_webhook.send(text=f"https://www.suntory.co.jp/factory/hakushu/")
for tag in data1:
    if tag.text is None:
        response = slack_webhook.send(text="yamajaki crawling server error")

    if '×' != tag.text:
        response = slack_webhook.send(text=f"하쿠슈 증류소 자리 생겼음 {data.text}"
                                           f"https://www.suntory.co.jp/factory/hakushu/")
