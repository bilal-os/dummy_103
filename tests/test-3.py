import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

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
    # 🧩 Step 1: Navigate to a deliberately invalid URL
    driver.get("https://www.thispagedoesnotexist123456789.com")

    # 🧩 Step 2: Try to get title (this should trigger an HTTP error from browser)
    print("Attempting to get title of non-existent page...")
    page_title = driver.title  # This should fail at WebDriver HTTP call

    print("Unexpected success! Page title was:", page_title)

except WebDriverException as e:
    # 🧠 This exception happens when the WebDriver command (HTTP call) itself fails
    print("❌ Test failed due to HTTP-level error when fetching title.")
    print("Error details:", e)

finally:
    driver.quit()
