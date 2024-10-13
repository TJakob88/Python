from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
chrome_driver_path = r"C:\Users\David\Downloads\chromedriver-win64\chromedriver.exe"

# Set up Chrome options to use your Profile 1
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:\Users\FIBI\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r'--profile-directory=default')

# Set up the WebDriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# List of restaurants with "Restaurant" added before "Phuket"
restaurants = [
    "A Pong Mae Sunee Restaurant Phuket", "Acquat Restaurant Phuket", "Blue Elephant Restaurant Phuket", "Chom Chan Restaurant Phuket", 
    "Chuan Chim Restaurant Phuket", "Go Ang Seafood Restaurant Phuket", "Go Benz Restaurant Phuket", "Go La Restaurant Phuket", 
    "Gorjan Restaurant Phuket", "Heh Restaurant Phuket", "Hom Restaurant Phuket", "Hong Khao Tom Pla Restaurant Phuket", 
    "Jadjan Restaurant Phuket", "Jampa Restaurant Phuket", "Jaras Restaurant Phuket", "Jongjit Kitchen Restaurant Phuket", 
    "Kha Mu Boran (Kathu) Restaurant Phuket", "Khao Tom Thanon Di Buk Restaurant Phuket", "Khrua Ohm Restaurant Phuket", 
    "Kin-Kub-Ei Restaurant Phuket", "Krua Baan Platong Restaurant Phuket", "Krua Kao Kuk Restaurant Phuket", 
    "Krua Praya Restaurant Phuket", "Kruvit Raft (Ban Laem Hin) Restaurant Phuket", "La Gaetana Restaurant Phuket", 
    "L'Arôme by the Sea Restaurant Phuket", "Lertrod Restaurant Phuket", "Loba Bang Niao Restaurant Phuket", 
    "Meesapam Khun Yai Chian Restaurant Phuket", "Mook Manee Restaurant Phuket", "Mor Mu Dong Restaurant Phuket", 
    "Mu Krop Chi Hong (Vichitsongkhram Road) Restaurant Phuket", "Naam Yoi Restaurant Phuket", "Nitan Restaurant Phuket", 
    "Niyom Salt Grilled Duck Restaurant Phuket", "O Cha Rot Restaurant Phuket", "O Tao Bang Niao Restaurant Phuket", 
    "One Chun Restaurant Phuket", "Pathongko Mae Pranee Restaurant Phuket", "Peang-Prai Restaurant Phuket", "PRU Restaurant Phuket", 
    "Roti Chaofa Restaurant Phuket", "Roti Thaew Nam Restaurant Phuket", "Royd Restaurant Phuket", "Salaloy Restaurant Phuket", 
    "Samut Restaurant Phuket", "Sang Ka Sri Restaurant Phuket", "Shrimp Noodles Ao Kae Restaurant Phuket", "Suay Restaurant Phuket", 
    "Surf & Turf by Soul Kitchen Restaurant Phuket", "Ta Khai Restaurant Phuket", "Talung Thai Restaurant Phuket", 
    "The Charm Dining Gallery Restaurant Phuket", "The Smokaccia Laboratory Restaurant Phuket", "The Thai Library Restaurant Phuket", 
    "Ton Mayom Restaurant Phuket", "Tu Kab Khao Restaurant Phuket", "Wagyu Steakhouse Restaurant Phuket"
]


# Open Google Maps
driver.get('https://www.google.com/maps/')
time.sleep(5)  # Wait for the page to load

# Step 1: Open side menu
menu_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Menu"]'))
)
menu_button.click()
time.sleep(2)

# Step 2: Wait for and click on "Saved"
saved_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@role="menuitem"]//label[text()="Saved"]'))
)
saved_button.click()
time.sleep(2)

# Step 3: Click "+ New list" to create a new list
new_list_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="New list"]'))
)
new_list_button.click()

# Step 4: Enter "Phuket Restaurants" as the new list name
list_name_input = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//input[@aria-label="List name"]'))
)
list_name_input.send_keys("Phuket Restaurants")
time.sleep(1)

# Step 5: Click the "Create" button to confirm the new list creation
create_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@jsname="McfNlf" and text()="Create"]'))
)
create_button.click()
time.sleep(2)

# Step 6: Add each restaurant to the new list
for restaurant in restaurants:
    try:
        # Click "+ Add a place"
        add_place_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add a place"]'))
        )
        add_place_button.click()

        # Step 7: Search for the restaurant in the search bar
        search_bar = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search for a place to add"]'))
        )
        search_bar.clear()
        search_bar.send_keys(restaurant)

        # Wait for 3 seconds to let the search results populate
        time.sleep(3)

        # Step 8: Select the first result from the dropdown
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@role="gridcell"])[1]'))
        )
        first_result.click()
        time.sleep(3)

    except Exception as e:
        print(f"Could not add {restaurant}: {e}")

# Close the browser after completing the task
driver.quit()
