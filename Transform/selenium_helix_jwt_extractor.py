
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_helix_jwt_token(username, password, start_url="https://aramco-private-dev.qa.sps.secops.bmc.com/"):
    options = Options()
    # options.add_argument('--headless')  # Uncomment if you want headless
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(start_url)

    try:
        # Wait for redirection to the RSSO login page
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        username_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "username"))
        )
        username_input.clear()
        username_input.send_keys(username)

        password_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_input.clear()
        password_input.send_keys(password)

        # Wait until the final admin dashboard URL loads
        WebDriverWait(driver, 30).until(
            EC.url_contains("/admin/#/landing")
        )

        # Extract cookies and find the helix_jwt_token
        cookies = driver.get_cookies()
        for cookie in cookies:
            if cookie["name"] == "helix_jwt_token":
                jwt = cookie["value"]
                print("✅ JWT Token Found!")
                print(jwt)

                # Optionally write to file
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
