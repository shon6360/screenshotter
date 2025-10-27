import time
import os
import pyautogui
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playwright.sync_api import sync_playwright

# Define screenshot region: (left, top, width, height)
REGION = (400, 165, 1015-400, 1845-165)
FOLDER = "screenshots"
PDF_NAME = "screenshots.pdf"


def main():
    # Step 1: Start browser
    driver = webdriver.Chrome()  # make sure you have ChromeDriver installed
    driver.get("https://rutgers.instructure.com")  # replace with the actual login page

    print(">>> Please log in manually, then press Enter here...")

    # Step 2: Navigate to page with the input field
    driver.get("https://rutgers.instructure.com")  # starter website
    input("Enter to continue")
    driver.get("https://reader2.yuzu.com/reader/books/9781119773535/epubcfi/6/2[%3Bvnd.vst.idref%3Dxcover]!/4/2[c00-cover]/2")  # change to the real page
    
    # Step 3: Extract the input value
    time.sleep(5)

    os.makedirs(FOLDER, exist_ok=True)
    value = ""
    images = []
    page = 0
    while value != "I-24":
        try:
            element = driver.find_element(By.CLASS_NAME, "InputControl__input-fbzQBk")
            value = element.get_attribute("value")
            print("Extracted value:", value)
        except:
            input("couldnt find value")
        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='status' and text()='Book Page Loaded']"))
            )
            time.sleep(0.1)

            img = pyautogui.screenshot(region=REGION)
            path = os.path.join(FOLDER, f"shot_{page}_{value}.png")
            img.save(path)
            images.append(path)
            time.sleep(.5)

        except Exception as e: 
            print(e)
            print("couldnt or something")
            input("continue...")
        pyautogui.press("right")
        page+=1
    
    
    pil_images = [Image.open(p).convert("RGB") for p in images]
    first, rest = pil_images[0], pil_images[1:]
    first.save(PDF_NAME, save_all=True, append_images=rest)


if __name__ == "__main__":
    main()
