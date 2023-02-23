from random import randint
from time import sleep
import math
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_path = ".//chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data")
prefs = {"profile.managed_default_content_settings.images": 2}
options.page_load_strategy = 'normal'
page = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)

user_given_keywords = []
user_given_keywords_sample = ["bachelor of ce", "gpa of 4", "two years of work experience", "TA of data mining course",
                              "my research interests are : RL and NLP", "android developer"]
fetched_keywords = ["university of Bonn", "high quality of teaching", "ranked 155", "master of cs"]


def sleep_random(v: int):
    sleep(randint(0, math.ceil(v)))


def submit():
    page.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("~~ performing submit action by css selector...")
        div = WebDriverWait(page, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            "#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.framer-dTOAf.framer-v-lkt6l4")))
        sleep_random(.8)
        page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        submit = WebDriverWait(div, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "framer-lkt6l4")))
        # submit = div.find_element_by_class_name("framer-lkt6l4")
        # submit.send_keys(Keys.RETURN)
        sleep_random(.4)
        # submit= page.find_element_by_css_selector("#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.framer-dTOAf.framer-v-lkt6l4 > button")
        submit.click()
    except:
        print("~~UNEXPEXTED: performing submit action...")
        action = webdriver.ActionChains(page)
        element = page.find_element_by_class_name('framer-lkt6l4')  # or your another selector here
        action.move_to_element(element)
        action.click()
        action.perform()
    finally:
        sleep_random(1.5)


def finish():
    page.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("~~ performing finish action by css selector...")
        div = WebDriverWait(page, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        "#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.grid.gap-4.auto-rows-auto > div:nth-child(2)")))
        sleep_random(.8)
        submit = div.find_elements_by_class_name("framer-lkt6l4")[-1]
        submit.send_keys(Keys.RETURN)
        sleep_random(.4)
        submit.click()
    except:
        print("~~UNEXPEXTED: performing finish action...")
        action = webdriver.ActionChains(page)
        element = page.find_elements_by_class_name('framer-lkt6l4')[-1]  # or your another selector here
        action.move_to_element(element)
        action.click()
        action.perform()
    finally:
        sleep_random(1.5)


def fetch_keywords_from_dataset(university, program):
    pass


if __name__ == '__main__':
    university_name = input("please enter name of the university : \n ")
    program_name = input("please enter name of the program : \n ")
    fetch_keywords_from_dataset(university_name, program_name)

    page.get("https://app.gomoonbeam.com/headstart/template?collection=student")
    print("starting ... ")
    sleep_random(2)
    try:
        myElem = WebDriverWait(page, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'px-4')))
    except TimeoutException:
        print("\n could not.")

    essay = page.find_element_by_css_selector(
        "#modal-root > div:nth-child(1) > div > div > div.w-full.lg\:w-\[80\%\].h-full.relative.z-10 > div > div > div.mx-auto.mt-10 > div > button:nth-child(1)")
    sleep_random(1)
    essay.click()
    sleep_random(1)
    while not page.current_url.__contains__("/details"):
        sleep_random(1)

    title = page.find_element_by_css_selector(
        "#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.relative.w-full > div.h-auto.min-h-16.mb-16 > div > h1")
    sleep_random(.5)
    title.click()
    title.send_keys("Statement of the purpose")
    sleep_random(1)

    towhom = page.find_element_by_css_selector(
        "#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.relative.w-full > div:nth-child(4) > div > p")
    sleep_random(.5)
    towhom.click()
    towhom.send_keys("Admission committee")
    sleep_random(1.2)

    keyword = page.find_element_by_css_selector(
        "#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.relative.w-full > div:nth-child(6) > div > ul > li > p")
    sleep_random(.2)
    keyword.click()
    keyword.send_keys("")
    keyword.send_keys(Keys.ENTER)
    sleep_random(.4)
    ul = page.find_element_by_css_selector(
        "#modal-root > div.max-w-7xl.mx-auto.px-4.sm\:px-6.lg\:px-8.pb-12 > div > div > div.relative.w-full > div:nth-child(6) > div > ul")

    lastli = None
    keywords = user_given_keywords_sample

    for k in keywords:
        page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        lis = ul.find_elements_by_tag_name("li")
        li = lis[-1]
        li.send_keys(k)
        li.send_keys(Keys.ENTER)
        sleep_random(1.3)
        lastli = li
    # lastli.send_keys(Keys.RETURN)
    sleep_random(2)
    submit()
    sleep_random(1)

    while not page.current_url.__contains__("/outline"):
        sleep_random(1)
    sleep_random(3)
    submit()
    sleep_random(1)
    while not page.current_url.__contains__("/points"):
        sleep_random(1)
    sleep_random(3.5)
    finish()
    sleep_random(1)

    while not page.current_url.__contains__("/editor"):
        sleep_random(1)
    sleep_random(2.3)
    content = page.find_element_by_css_selector(
        "#modal-root > div.w-full.lg\:max-w-screen-2xl.mx-auto > div > div.w-full.editor.relative.lg\:max-w-screen-lg.mx-auto.transition.duration-200 > div > div.mt-28.sm\:mt-16 > div").text

    sleep_random(1)
    print("your SOP is ready : \n \n ")
    print(content)
    sleep_random(1)
