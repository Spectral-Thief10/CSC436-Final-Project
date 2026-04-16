from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://theresasimmonsbrown.long-realty.com/testimonials.php"

# Configure Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Modern headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"
)

# Reduce detection as an automated browser
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Initialize WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Further mask automation signals
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)

def RunScraper():
    try:
        # Open the webpage
        driver.get(url)

        # Wait for the page content to load
        wait = WebDriverWait(driver, 15)
        body = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Extract testimonials
        testimonials = []

        # Collect text from relevant elements
        elements = driver.find_elements(By.XPATH, "//p | //blockquote | //td")

        # adding text from the testimonial to the list but stopping once it reaches legal text
        for element in elements:
            text = element.text.strip()
            if ("Should you require assistance in navigating our website" in text
                or "Arizona Regional Multiple Listing Service" in text
                or "Internet Data Exchange (IDX)" in text):
                    break
            
            elif len(text) > 60:  # Filter likely testimonial content
                testimonials.append(text)

        # Remove duplicates while preserving order
        unique_testimonials = list(dict.fromkeys(testimonials))

        # Save to file
        with open("testimonials.txt", "w", encoding="utf-8") as file:
            for i, testimonial in enumerate(unique_testimonials, 1):
                file.write(f"{i}. {testimonial}\n\n")

        print("Testimonials saved to testimonials.txt")

    finally:
        # Close the browser
        driver.quit()
    return unique_testimonials
test = RunScraper()


