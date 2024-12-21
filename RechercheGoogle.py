from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Utilisation du chemin correct pour ChromeDriver
driver_path = r'C:\Program Files\Python313\Scripts\chromedriver.exe'  # Utilisation de la chaîne brute

# Création de l'objet Service pour spécifier le chemin de chromedriver
service = Service(driver_path)

# Initialisation du WebDriver en utilisant l'objet Service
driver = webdriver.Chrome(service=service)

# Ouvrir Google
driver.get("https://www.google.com")

# Attendre que la page soit complètement chargée
time.sleep(2)

# Trouver la barre de recherche Google
search_box = driver.find_element(By.NAME, "q")

# Effectuer une recherche
search_query = "Python programming"
search_box.send_keys(search_query)  # Tapez la requête dans la barre de recherche
search_box.send_keys(Keys.RETURN)  # Appuyez sur "Entrée" pour lancer la recherche

# Attendre quelques secondes pour voir les résultats
time.sleep(5)

# Fermer le navigateur
driver.quit()
