import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get executor URL from command line
executor_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8888/"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Remote(
    command_executor=executor_url,
    options=chrome_options
)

try:
    driver.get("https://www.example.com")
    WebDriverWait(driver, 10).until(
        EC.visibility_of(driver.find_element(By.CSS_SELECTOR, "h1"))
    )

    # Intentionally incorrect assertion to cause failure
    assert "Not The Correct Title" in driver.title, "Expected incorrect title to fail the test."

    print("Test passed: (unexpectedly)")

except AssertionError as e:
    print("❌ Test failed as expected:", e)

finally:
    driver.quit()
