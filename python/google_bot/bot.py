from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

# Kullanıcıdan arama terimi al
query = input("Ne arayayım?: ")

# Chrome loglarını gizle
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

# Chrome'u başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver, 10)

    # Arama kutusunu bul ve arama yap
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Arama sonuçlarını bekle
    results_locator = (By.XPATH, "//div[@id='search']//a[h3]")
    wait.until(EC.presence_of_all_elements_located(results_locator))

    # Sonuçları al
    results = driver.find_elements(*results_locator)
    titles = []
    for el in results:
        try:
            h3 = el.find_element(By.TAG_NAME, "h3")
            title = h3.text.strip()
            if title:
                titles.append(title)
        except Exception:
            continue

    # Dosyaya yaz
    out_path = os.path.abspath("sonuclar.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        for i, t in enumerate(titles, start=1):
            f.write(f"{i}. {t}\n")

    print(f"\nBulunan başlık sayısı: {len(titles)}")
    print(f"Sonuçlar kaydedildi: {out_path}\n")

    input("Tarayıcıyı kapatmak için Enter'a bas...")
finally:
    driver.quit()
