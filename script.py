from time import sleep
from unittest.mock import DEFAULT

from mouseinfo import POINT
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from screeninfo import get_monitors
from collections import namedtuple
import pyperclip
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyautogui
import time

Point = namedtuple('Point', 'x y')
Screen = namedtuple('Screen', 'width height')

def findPrimaryMonitor():
    monitors = get_monitors()

    primary_monitor = next((m for m in monitors if m.is_primary), None)

    if primary_monitor:
        return scale_point(Screen(primary_monitor.width_mm, primary_monitor.height_mm));
    else:
        print("Nenhum monitor primário encontrado.")

def scale_point(new_screen):
    print(new_screen)
    reference_point = Point(1031, 945)
    #reference_point = Point(1058, 989)
    original_screen = Screen(344, 194)

    scale_x = new_screen.width / original_screen.width
    scale_y = new_screen.height / original_screen.height

    # Escala o ponto original para a nova tela
    new_x = reference_point.x * scale_x
    new_y = reference_point.y * scale_y

    return Point(new_x, new_y)

PASSWORD = "freggi1505"
USER = "03906455670"
URL = "https://cruzeiro.futebolcard.com/login"
DEFAULT_TIMEOUT = 12
POINT =findPrimaryMonitor()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get(URL)

cookie = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='setCookies']")))

cookie.click()

input_user = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div/form/div/div[1]/div[2]/input")))

input_password = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='pass']")))


input_user.send_keys(USER)
input_password.send_keys(PASSWORD)

login_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div/form/div/div[3]/div/div/input[2]")))

login_button.click()

buy_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/div[2]/div/div/div/div/div/div[1]/div/a")))

buy_button.click()

buy_button2 = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[3]/div[5]/a")))

buy_button2.click()

canvas = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='fc-map-canvas']")))

# Cria uma cadeia de ações para mover o cursor e clicar no ponto específico
# drawing = ActionChains(driver)\
#     .move_to_element_with_offset(canvas, x_offset, y_offset)\
#     .click()\
#     .release()
#
# # Executa as ações
# drawing.perform()

x_offset = POINT.x
y_offset = POINT.y

pyautogui.moveTo(x_offset, y_offset)

sleep(6)
pyautogui.click()

select_quantity = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_quantity']")))

select_quantity.click()

quantity2 = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='ticket_quantity']/option[2]")))

quantity2.click()

ok_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='alert-confirm']")))

ok_button.click()

#AQUI CAGOU
select_buyer = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[1]/td[4]/select")))

select_buyer.click()

select_buyer_fabiano = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[1]/td[4]/select/option[2]")))

select_buyer_fabiano.click()

#SEGUNDO INGRESSO
select_buyer = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[2]/td[4]/select")))

select_buyer.click()

select_buyer_fabiano = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[4]/div/div/table/tbody/tr[2]/td[4]/select/option[3]")))

select_buyer_fabiano.click()

select_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[6]/div/div[2]/div/div[5]/div/input")))

select_input.click()

sleep(6)
# Localiza o elemento antes de fazer o scroll
accept_terms = driver.find_element(By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/input")

# Faz o scroll para o elemento, sem esperar que ele esteja clicável
driver.execute_script("arguments[0].scrollIntoView(true);", accept_terms)
driver.execute_script("window.scrollBy(0, -150);")
sleep(2)
# Agora espera que o elemento esteja clicável
accept_terms_clickable = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/label"))
)

# Finalmente, clica no elemento
accept_terms_clickable.click()

next_terms = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div[2]/div/div/div/div[2]/div[2]/button"))
)

# Rolar até o elemento com JavaScript


# Agora o elemento está visível e pode ser clicado
next_terms.click()

pix = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/section/main/section[2]/div[1]/div/div[2]/div[2]/a/div")))

pix.click()

entry_modal = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='alert-modal']/div/div/div[2]/div/select")))

entry_modal.click()

entry_select = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='alert-modal']/div/div/div[2]/div/select/option[2]")))

entry_select.click()

sleep(6)
pix = driver.find_element(By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div/div[2]/div/div[1]/a")

# Faz o scroll para o elemento, sem esperar que ele esteja clicável
driver.execute_script("arguments[0].scrollIntoView(true);", pix)
driver.execute_script("window.scrollBy(0, -150);")

pix = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/main/section/div/div/div/div/div[2]/div/div[1]/a")))

pix.click()
driver.quit()

msg = MIMEMultipart()

password = ""
msg['From'] = "aplicacaofabianocruzeiro@gmail.com"
msg['To'] = "gustavo.riegert@evoluaenergia.com.br"
msg['Subject'] = "Pix para pagamento jogo do cruzeiro"
msg.attach(MIMEText(pyperclip.paste()))

# create server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)


server.sendmail(msg['From'], msg['To'], msg.as_string())
print('Email enviado')

server.quit()

# Configurações de e-mail

# Envia o e-mail
