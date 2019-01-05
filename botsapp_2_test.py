#
# This version of BotsApp sends two messages: one with Dylan Thomas'
# poem and another one specifying that the poem was sent remotely.
#

from selenium import webdriver

driver = webdriver.Chrome('/Applications/chromedriver')
driver.get('https://web.whatsapp.com/')

print('\n Welcome to BotsApp version 2.0! \n')

# list of spam victims
contact_list = [
    # Enter recipients here:
    "Person1",
    "Person2",
    "Person3"
]

input('Press ENTER/RETURN to send spam! <<<SCAN QR CODE FIRST>>>')

for victim in contact_list:
    # sets recipient to victim's name
    name = victim
    msg = "Do not go gentle into that good night " \
        "Old age should burn and rave at close of day " \
        "Rage, rage against the dying of the light " \
        "Though wise men at their end know dark is right " \
        "Because their words had forked no lightning they " \
        "Do not go gentle into that good night " \
        "Good men, the last wave by, crying how bright " \
        "Their frail deeds might have danced in a green bay " \
        "Rage, rage against the dying of the light " \
        "Wild men who caught and sang the sun in flight " \
        "And learn, too late, they grieved it on its way " \
        "Do not go gentle into that good night " \
        "Grave men, near death, who see with blinding sight " \
        "Blind eyes could blaze like meteors and be gay " \
        "Rage, rage against the dying of the light " + 
        "\n A poem by Dylan Thomas, but sent remotely by BotsApp 2.0 automated SpamBot ;-)"

    # selenium wizardry
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()

print('\n BotsApp 2.0 has served its purpose; now it shall rest. \n')
