from selenium import webdriver
from time import sleep

# Stworzenie instancji klasy Chrome - otwarcie przegląądarki
driver = webdriver.Chrome()
# Otwarcie strony
driver.get("https://www.kozminski.edu.pl/pl")
# Maksymalizacja okna
driver.maximize_window()
sleep(5)
driver.quit()
