from selenium import webdriver

# important: specifiy path to 'chromedriver' as an argument for webdriver 
driver = webdriver.Chrome('/Applications/chromedriver')
# opening Google Chrome
driver.get('https://web.whatsapp.com/')

# welcome message
print('\n')
print('\n')
print('Welcome to BotsApp SpamBot Ver1.2!')
print('\n')
print('\n')
name = 'Counting' # test group for whatsapp script
print('Ready to start counting? ;-D')
number = int(input('Enter starting number: ')) # number line_input
input('Scan QR code and press ENTER/RETURN to run BotsApp SpamBot')
print('\n')
print('\n')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')
while True:
    number = int(input('Enter starting number: ')) # number line_input
    if number == -1:
        break
    for num_to_print in range(number, number+100):
        msg = str(num_to_print)
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()

# exit message
print('\n')
print('\n')
print('Thanks for using BotsApp Ver1.2!')
print('Returning to MacOS terminal ...')
print('\n')
print('\n')
