import time
from threading import TIMEOUT_MAX
from time import sleep
from collections import namedtuple
from screeninfo import get_monitors
import pyperclip
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

Point = namedtuple('Point', 'x y')
Screen = namedtuple('Screen', 'width height')

PASSWORD = "freggi1505"
USER = "03906455670"
URL = "https://cruzeiro.futebolcard.com/login"
DEFAULT_TIMEOUT = 12
TIMEOUT_MAX = 28800


import subprocess
import sys

# Código para instalar dependências
def install_dependencies():
    try:
        import selenium
        import pyautogui
        import pyperclip
        import screeninfo
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium', 'pyautogui', 'pyperclip', 'screeninfo'])

def find_primary_monitor():
    monitors = get_monitors()
    primary_monitor = next((m for m in monitors if m.is_primary), None)
    if primary_monitor:
        return scale_point(Screen(primary_monitor.width_mm, primary_monitor.height_mm))
    else:
        print("Nenhum monitor primário encontrado.")


def scale_point(new_screen):
    reference_point = Point(1031, 945)
    original_screen = Screen(344, 194)
    scale_x = new_screen.width / original_screen.width
    scale_y = new_screen.height / original_screen.height
    new_x = reference_point.x * scale_x
    new_y = reference_point.y * scale_y
    return Point(new_x, new_y)


def login(driver):
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='setCookies']"))
    ).click()

    driver.find_element(By.XPATH,
                        "/html/body/div[3]/section/main/section/div/div/div/div/form/div/div[1]/div[2]/input").send_keys(
        USER)
    driver.find_element(By.XPATH, "//*[@id='pass']").send_keys(PASSWORD)
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/section/main/section/div/div/div/div/form/div/div[3]/div/div/input[2]").click()


def purchase_tickets(driver, point):
    WebDriverWait(driver, TIMEOUT_MAX).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/div[2]/div/div/div/div/div/div[1]/div/a"))
    ).click()

    WebDriverWait(driver, TIMEOUT_MAX).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[3]/div[5]/a"))
    ).click()

    pyautogui.moveTo(point.x, point.y)
    sleep(6)
    pyautogui.click()

    select_quantity = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_quantity']"))
    )
    select_quantity.click()
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_quantity']/option[2]"))
    ).click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='alert-confirm']"))
    ).click()


def select_buyers(driver):
    select_buyer = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[1]/td[4]/select")))

    select_buyer.click()

    select_buyer_fabiano = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[1]/td[4]/select/option[2]")))

    select_buyer_fabiano.click()

    # SEGUNDO INGRESSO
    select_buyer = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[2]/td[4]/select")))

    select_buyer.click()

    select_buyer_fabiano = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[2]/td[4]/select/option[3]")))

    select_buyer_fabiano.click()

    select_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section[6]/div/div[2]/div/div[5]/div/input")))

    select_input.click()

    sleep(6)


def accept_terms_and_proceed(driver):
    accept_terms = driver.find_element(By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/input")

    # Faz o scroll para o elemento, sem esperar que ele esteja clicável
    driver.execute_script("arguments[0].scrollIntoView(true);", accept_terms)
    driver.execute_script("window.scrollBy(0, -150);")
    sleep(2)

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/label"))
    ).click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div[2]/div/div/div/div[2]/div[2]/button"))
    ).click()



def complete_payment(driver):
    pix = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/section/main/section[2]/div[1]/div/div[2]/div[2]/a/div"))
    )
    pix.click()

    entry_modal = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='alert-modal']/div/div/div[2]/div/select"))
    )
    entry_modal.click()

    entry_select = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='alert-modal']/div/div/div[2]/div/select/option[2]"))
    )
    entry_select.click()

    sleep(6)
    pix_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div/div[2]/div/div[1]/a"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", pix_button)
    driver.execute_script("window.scrollBy(0, -130);")
    pix_button.click()
    sleep(4)

def send_email():
    msg = MIMEMultipart()
    msg['From'] = "aplicacaofabianocruzeiro@gmail.com"
    msg['To'] = "gustavo.riegert@evoluaenergia.com.br"
    msg['Subject'] = "Pix para pagamento jogo do cruzeiro"
    msg.attach(MIMEText(pyperclip.paste()))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], "saqa cbhi sqjc xvgv")  # Considere usar variáveis de ambiente
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def main():
    point = find_primary_monitor()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    login(driver)
    purchase_tickets(driver, point)
    select_buyers(driver)
    accept_terms_and_proceed(driver)
    complete_payment(driver)
    send_email()
    driver.quit()




if __name__ == "__main__":
    install_dependencies()
    main()
