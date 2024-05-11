
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class OddsPortal:
    
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    
    def scrape(self, ori_url):
        try:
            # Open Original URL
            ori_url = "https://www.oddsportal.com/tennis/argentina/atp-buenos-aires/results/"
            self.driver.get(ori_url)
            # Wait for the page to load
            time.sleep(10)

            # Loop through list of pages
            Orig_urls = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[2]/a'
            Orig_URLs = self.driver.find_elements(By.XPATH, Orig_urls)
            for orig_result in Orig_URLs:
                o_href = orig_result.get_attribute('href')
                print(o_href)

            pages = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[4]/div[1]/div[1]/div/div/div/a'
            pages_url = self.driver.find_elements(By.XPATH, pages)
            pages_list = []
            for page in pages_url:
                p_href = page.get_attribute("href")
                print(f'p_href: {p_href}')
                pages_list.append(p_href)
            print(f'pages_list : {pages_list}')

            for page in pages_list:
                    
                self.driver.get(page)
                time.sleep(10)
                bookmark_path = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[1]/a[2]/p'
                bookmark = self.driver.find_element(By.XPATH, bookmark_path).text
                print(f'Bookmark: {bookmark}')

                odd1 = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/p'
                odd2 = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/p'
                odd1_value = self.driver.find_element(By.XPATH, odd1).text
                odd2_value = self.driver.find_element(By.XPATH, odd2).text

                payout = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[4]/span'
                payout_value = self.driver.find_element(By.XPATH, payout).text

                final_result = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div[3]/div[2]'
                final_result_value = self.driver.find_element(By.XPATH, final_result).text

                date_time = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[2]/div[1]'
                date_time_value = self.driver.find_element(By.XPATH, date_time).text


                print(f'Odd1: {odd1_value}')
                print(f'Odd2: {odd2_value}')
                print(f'Payout: {payout_value}')
                print(f'Final Reuslt: {final_result_value}')
                print(f'Data_Time: {date_time_value}')



            
        finally:
            print("Done")



# Example usage
def main():
    scraper_1 = OddsPortal()
    
    scraper_1.scrape("https://www.oddsportal.com/tennis/argentina/atp-buenos-aires/results/")

if __name__ == "__main__":
    main()
