from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

class Gender:
    MALE = 0
    FEMALE = 1

# Dane testowe
DATA_EMAIL = "erfeerf@sdcsd.dd"
DATA_GENDER = Gender.MALE

# Stworzenie instancji klasy Chrome - otwarcie przegląądarki
driver = Chrome()
# Otwarcie strony
driver.get("https://automationpractice.techwithjatin.com/")
# Maksymalizacja okna
driver.maximize_window()

# Znajdź element Sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
# Kliknij w odnaleziony element
sign_in_a.click()

# Wpisz email
driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)
# Kliknij Create account
driver.find_element(By.ID, "SubmitCreate").click()

driver.implicitly_wait(5)
# Kliknij swoją płeć
if DATA_GENDER == Gender.FEMALE:
    driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
else:
    driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()

sleep(5)
driver.quit()
