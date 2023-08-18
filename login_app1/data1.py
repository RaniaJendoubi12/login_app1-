from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


# ==================================================================================================<<<<<<<<<<<<<<<<<<<<<========

def freshservice(email, password, Ticket_ID):
    try:
        chrome_options = Options()

        chrome_options.add_extension('buster.crx')

        driver = webdriver.Chrome(chrome_options)
        driver.maximize_window()
        action = ActionChains(driver)

        driver.get(Ticket_ID)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-o1ejds'))).click()
        WebDriverWait(driver, 60).until(EC.url_changes(driver.current_url))

        WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located)

        time.sleep(5)
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        # =========================================================================================priority

        elements_priority = soup.find_all(class_="ember-power-select-selected-item priority-value")
        priority = elements_priority[0].text.strip()

        # =========================================================================================contact
        elements_contact = soup.find_all('span', id='primary_email')
        contact = elements_contact[0].text.strip()

        # =========================================================================================subject
        elements_subject = soup.find_all('h3', attrs={'class': 'subject-text'})
        subject = elements_subject[0].text.strip()

        # =========================================================================================group
        elements_group = soup.find_all(class_="ember-power-select-selected-item has-clear")
        group = elements_group[0].text.strip()

        # =========================================================================================description
        elements_description = soup.find_all(class_="view-more-body")
        description = elements_description[0].text.strip()

        # =========================================================================================agent
        elements_agent = soup.find_all(class_="ember-power-select-selected-item has-clear")
        agent = elements_agent[1].text.strip()

        # ==========================================================================================create_new_change
        driver.get("https://tunisia828.freshservice.com/itil/changes/new")

        # =========================================================================================e-mail

        element_mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'itil_change_email')))
        element_mail.send_keys(contact)

        # =========================================================================================subject

        elements_subject = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'itil_change_subject')))
        elements_subject.send_keys(subject)

        # =========================================================================================periority

        driver.find_element(By.ID, "select2-chosen-15").click()
        if priority == 'Low':
            action.send_keys(Keys.ENTER)
            action.perform()
        if priority == 'Medium':
            action = ActionChains(driver)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ENTER)
            action.perform()
        if priority == 'High':
            action = ActionChains(driver)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ENTER)
            action.perform()
        if priority == 'Urgent':
            action = ActionChains(driver)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ARROW_DOWN)
            action.send_keys(Keys.ENTER)
            action.perform()

        # ===============================================================================================Group

        elm = driver.find_element(By.XPATH, '//*[@id="s2id_itil_change_group_id"]/a')
        action.move_to_element(elm)
        time.sleep(1)
        action.click()
        time.sleep(1)
        action.send_keys(group)
        action.send_keys(Keys.ENTER)
        action.perform()

        # ==============================================================================================Agente
        elements_agent = driver.find_element(By.ID, "itil_change_owner_id")
        time.sleep(2)
        select = Select(elements_agent)
        time.sleep(2)
        select.select_by_visible_text(agent.strip())

        # =============================================================================================description
        script_reason = 'document.querySelector("#analysis_type_change_reason > div.redactor_box > div.redactor_editor > p").innerHTML = "' + subject + '"'
        driver.execute_script(script_reason)

        my_desc = str(description.strip())
        script_description = 'document.querySelector("#NewChange > ul > li.html_paragraph.default_description.field > div.redactor_box > div.redactor_editor > p").innerHTML = "' + my_desc + '"'
        driver.execute_script(script_description)

        # =============================================================================================start_time
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime('%Y-%m-%d')

        script_start_date = 'document.querySelector("#itil_change_planned_start_date_date").value = "' + formatted_date + '"'
        driver.execute_script(script_start_date)
        driver.find_element(By.ID, "itil_change_planned_start_date_time").click()
        action2 = ActionChains(driver)
        action2.send_keys(Keys.ARROW_DOWN)
        action2.send_keys(Keys.ENTER)
        action2.perform()

        # =============================================================================================end_time
        script_start_end = 'document.querySelector("#itil_change_planned_end_date_date").value = "' + formatted_date + '"'
        driver.execute_script(script_start_end)
        driver.find_element(By.ID, "itil_change_planned_end_date_time").click()
        action3 = ActionChains(driver)
        action3.send_keys(Keys.ARROW_DOWN)
        action3.send_keys(Keys.ENTER)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.perform()

        # =========================================================================================e-mail

        element_mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'itil_change_email')))
        element_mail.send_keys(contact)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)
        action3.send_keys(Keys.TAB)

        action3.perform()

        driver.find_element(By.ID, "itil_change_submit").click()

        time.sleep(15)
        driver.quit()
        return 'done'
    except:
        return 'filed'


