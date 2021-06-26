from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

# Change this to your own chromedriver path!
chromedriver_path = 'C:\Program Files\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)
facebook = webdriver.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[5]/button")
facebook.click()

username = webdriver.find_element_by_id('email')
username.send_keys('email_facebook')
password = webdriver.find_element_by_id('pass')
password.send_keys('password_here')

button_login = webdriver.find_element_by_id('loginbutton')
button_login.click()
# print(button_login)
sleep(10)

Not_Now = webdriver.find_element_by_xpath(
    "/html/body/div[4]/div/div/div/div[3]/button[2]")
Not_Now.click()
# notnow = webdriver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications


# # Pt2
hashtag_list = ['website', 'pythoncode', 'googleintern']

prev_user_list = []
# - if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' +
                  hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')

    first_thumbnail.click()
    sleep(randint(1, 2))
    try:
        # for x in range(1, 200):
        username1 = webdriver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
        print(username1, end=" ")
        if username not in prev_user_list:
            #     # If we already follow, do not unfollow
            # print("line 65")
            if webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                webdriver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                print("line 66")
                new_followed.append(username)
                followed += 1

        #         # Liking the picture
                button_like = webdriver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')

                button_like.click()
                likes += 1
                sleep(randint(18, 25))
                # sleep(5)
                # Comments and tracker
                # comm_prob = randint(1, 10)
                # print('{}_{}: {}'.format(hashtag, x, comm_prob))
                if comm_prob > 7:
                    comments += 1
                    webdriver.find_element_by_xpath(
                        '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                    comment_box = webdriver.find_element_by_xpath(
                        '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send("Awesome!!")

                    # if (comm_prob < 7):
                    #     comment_box.send_keys('Really cool!')
                    #     sleep(1)
                    # elif (comm_prob > 6) and (comm_prob < 9):
                    #     comment_box.send_keys('Nice work :)')
                    #     sleep(1)
                    # elif comm_prob == 9:
                    #     comment_box.send_keys('Nice gallery!!')
                    #     sleep(1)
                    # elif comm_prob == 10:
                    #     comment_box.send_keys('So cool! :)')
                    #     sleep(1)
        #             # Enter to post comment
                    webdriver.find_element_by_xpath(
                        "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()
                    sleep(randint(22, 28))
                    # sleep(5)

            # Next picture
            webdriver.find_element_by_link_text('Next').click()
            sleep(randint(25, 29))
        else:
            webdriver.find_element_by_link_text('Next').click()
            sleep(randint(20, 26))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        print("Except")
        continue

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv(
    '{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
