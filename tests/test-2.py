import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

executor_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8888/"
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Remote(command_executor=executor_url, options=chrome_options)

try:
    driver.get("https://www.wikipedia.org")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "searchInput")))

    driver.find_element(By.ID, "searchInput").send_keys("Python (programming language)")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(EC.title_contains("Python"))
    assert "Python" in driver.title, "Wikipedia navigation failed."

    print("Test passed: Navigated to Python (programming language) page successfully.")
except Exception as e:
    print("Test failed:", e)
finally:
    driver.quit()
