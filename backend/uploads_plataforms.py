from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--enable-chrome-browser-cloud-management')
options.add_argument("user-data-dir=C:\\Users\joaor\\AppData\Local\\Google\\Chrome Beta\\User Data\\")
options.binary_location = r"C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
#options.add_argument('--headless=new')

def upload_to_youtube():
    pathFinal = r'C:\\Users\joaor\\anaconda3\envs\\env\\automacao_youtube\\videos\\video_audio.mp4'

    driver = webdriver.Chrome(options=options)
    driver.get('https://studio.youtube.com/channel/UC5MhzpxIkIvuDK2r_UJE2lQ')
    btnSendVideo = driver.find_element(By.ID,'create-icon')
    WebDriverWait(driver,20).until(EC.element_to_be_clickable(btnSendVideo)).click()
    btnSendVideo2 = driver.find_element(By.XPATH,'//*[@id="text-item-0"]/ytcp-ve')
    WebDriverWait(driver,20).until(EC.element_to_be_clickable(btnSendVideo2)).click()
    inputFile = driver.find_element(By.NAME,'Filedata').send_keys(pathFinal)

    sleep(7)

def upload_to_tiktok():
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.click(751,157)
    sleep(1)
    pyautogui.write('Google Chrome Beta')
    pyautogui.hotkey('enter')
    sleep(3)
    pyautogui.click(438,59)
    pyautogui.write('https://www.tiktok.com/@robtopdagalaxia001')
    sleep(2)
    pyautogui.hotkey('enter')
    sleep(5)
    pyautogui.click(1670,143)
    sleep(1)
    pyautogui.click(1670,143)
    sleep(1)
    pyautogui.click(1670,143)
    
    sleep(5)
    pyautogui.click(1361,530)
    sleep(1)
    pyautogui.click(527,65)
    pyautogui.write("C:/Users/joaor/anaconda3/envs/env/automacao_youtube/videos")
    sleep(1)
    pyautogui.click(458,522)
    pyautogui.write("video_audio.mp4")
    pyautogui.hotkey('enter')
    sleep(2)
    pyautogui.click(1182,1057)