from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os.path import exists as ex
import os
import zipfile as zp


TESTDIR = '/home/pi/iolink_tests/'
CSS_SELECTOR1 = """datatable-row-wrapper.datatable-row-wrapper:nth-child(1) > 
datatable-body-row:nth-child(1) > div:nth-child(2) > datatable-body-cell:nth-child(1) > 
div:nth-child(1) > div:nth-child(1)"""
CSS_SELECTOR2 = '.btn-default-ioddfinder'
WEBDRIVER = "https://ioddfinder.io-link.com/productvariants/search?page=0&vendorName=Festo&productName="
CHECKING_FOLDER = '/home/pi/Downloads/iodd.zip'

def get_iodd(product_name):
    with webdriver.Firefox() as driver:

        driver.get(WEBDRIVER + product_name)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR1))).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR2))).click()
        wait = WebDriverWait(driver, 120, 1)
        driver.close()


def rename_and_move_file(product_name):
    if ex() == True:
        
        os.rename(CHECKING_FOLDER, f'{TESTDIR}test_data/{product_name}.zip')


def unzip_and_delete_zip_file(product_name):
    ZIPFILE = f"{TESTDIR}test_data/{product_name}.zip"
    
    with zp.ZipFile(f'{TESTDIR}test_data/{product_name}.zip', 'r') as zip_ref:
       
       zip_ref.extractall(f"{TESTDIR}test_data/{product_name}")
    
    os.remove(ZIPFILE)
