from selenium import webdriver

driver = webdriver.Chrome('/home/s0umyajit/Downloads/chromedriver')
driver.get('https://web.whatsapp.com/')
print('Scan the QR code')


def send_msg():
    name = input("Enter the User Name or Group Name \t")
    msg = input("Enter the message \t")
    count = input("Enter the the number of times you want to send message \t")
    count = int(count)
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')
    for i in range(count):
        msg_box.send_keys(msg)
        btn = driver.find_element_by_class_name('_3M-N-')
        btn.click()


send_msg()
