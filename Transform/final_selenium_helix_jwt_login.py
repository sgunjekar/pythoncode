
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_helix_jwt_token(username, password, start_url="https://aramco-private-dev.qa.sps.secops.bmc.com/"):
    options = Options()
    # Uncomment the line below to run headless (no visible browser)
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    driver.get(start_url)

    try:
        print("🟡 Waiting for page to load and redirect...")
        time.sleep(3)
        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)

        # Locate username input field correctly by actual <input> ID
        username_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "user_login"))
        )
        username_input.send_keys(username)

        # Find password input field by name or other reliable selector
        password_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_input.send_keys(password)
        password_input.submit()

        print("🟢 Submitted login form, waiting for post-login redirect...")
        WebDriverWait(driver, 30).until(
            EC.url_contains("/admin/#/landing")
        )
        print("✅ Redirected to admin landing page!")

        # Extract helix_jwt_token from cookies
        cookies = driver.get_cookies()
        for cookie in cookies:
            print(f"Cookie: {cookie['name']}")  # Debug all cookie names
            if cookie["name"] == "helix_jwt_token":
                jwt = cookie["value"]
                print("✅ JWT Token Found:")
                print(jwt)
                with open("jwt_token.txt", "w") as f:
                    f.write(jwt)
                return jwt

        print("❌ helix_jwt_token not found in cookies.")
        return None

    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    get_helix_jwt_token("hannah_admin", "Password_1234")
