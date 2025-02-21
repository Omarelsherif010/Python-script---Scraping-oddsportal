
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

class OddsPortal:
    
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def scroll_to_load_games(self):
        # Scroll down to load more games
        for _ in range(5):  # Adjust the number of scrolls as needed
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for more games to load

    def append_if_not_duplicate(self, row_data, excel_path, sheet_name='Sheet1'):
        # Try to read the existing Excel file
        try:
            df_existing = pd.read_excel(excel_path, sheet_name=sheet_name)
        except FileNotFoundError:
            # If the file does not exist, create a new DataFrame
            df_existing = pd.DataFrame(columns=row_data.keys())
        
        # Check if the 'Page_URL' is already in the DataFrame
        if not df_existing[df_existing['Page_URL'] == row_data['Page_URL']].empty:
            print("Data for this Page_URL already exists in the Excel sheet. Skipping duplicate.")
        else:
            # Append the new row to the DataFrame
            df_existing = pd.concat([df_existing, pd.DataFrame([row_data])], ignore_index=True)
            # Save the updated DataFrame to the Excel file
            df_existing.to_excel(excel_path, index=False, sheet_name=sheet_name)
            print("Data appended successfully.")

    def scrape(self, ori_url):
        try:
            # Open Original URL
            ori_url = "https://www.oddsportal.com/tennis/argentina/atp-buenos-aires/results/"
            self.driver.get(ori_url)
            # Wait for the page to load
            time.sleep(5)
            
            self.scroll_to_load_games()


            # Loop through list of pages
            Orig_urls = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[2]/a'
            Orig_URLs = self.driver.find_elements(By.XPATH, Orig_urls)
            Orig_list = []
            for orig_result in Orig_URLs:
                o_href = orig_result.get_attribute('href')
                # print(o_href)
                Orig_list.append(o_href)
            print(f'Original List: {Orig_list}')
            print(f'lenght of Orig_list : {len(Orig_list)}')


            pages = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[4]/div[1]/div[1]/div/div/div/a'
            pages_url = self.driver.find_elements(By.XPATH, pages)
            pages_list = []
            for page in pages_url:
                p_href = page.get_attribute("href")
                # print(f'p_href: {p_href}')
                pages_list.append(p_href)
            print(f'pages_list : {pages_list}')
            print(f'lenght of pages_list : {len(pages_list)}')
            
            counter = 0

            # scraped_data = []

            for page in pages_list:
                self.driver.get(page)
                time.sleep(5)
                try:
                    bookmark_path = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[1]/a[2]/p'
                    bookmark = self.driver.find_element(By.XPATH, bookmark_path).text

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

                    p1 = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[1]/div[1]/div/div[1]/span'
                    p1_value = self.driver.find_element(By.XPATH, p1).text
                    
                    p2 = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/span'
                    p2_value = self.driver.find_element(By.XPATH, p2).text

                    meta_desc = '/html/head/meta[12]'
                    meta_desc_value = self.driver.find_element(By.XPATH, meta_desc).get_attribute('content')
                    
                    meta_key = '/html/head/meta[11]'
                    meta_key_value = self.driver.find_element(By.XPATH, meta_key).get_attribute('content')

                    ### Desired number of extracted games
                    if counter == 10:
                        break
                    counter += 1
                    print(f'Original_URL: {ori_url}')
                    print(f'Page URL: {page}')
                    print(f'Odd1: {odd1_value}')
                    print(f'Odd2: {odd2_value}')
                    print(f'Payout: {payout_value}')
                    print(f'Final Reuslt: {final_result_value}')
                    print(f'Data_Time: {date_time_value}')
                    print(f'P1: {p1_value}')
                    print(f'P2: {p2_value}')
                    print(f'Meta Description: {meta_desc_value}')
                    print(f'Meta Keywords: {meta_key_value}')
                    print(f"Counter: {counter}")

                    row_data = {
                        'Original_URL': ori_url,
                        'Page_URL': page,
                        'Bookmaker': bookmark,
                        'Odd1': odd1_value,
                        'Odd2': odd2_value,
                        'Payout': payout_value,
                        'Current_time': time.strftime("%Y-%m-%d %H:%M:%S"),
                        'Meta_description': meta_desc_value,
                        'Meta_keywords': meta_key_value,
                        'Date_Time': date_time_value,
                        'Final_Result': final_result_value,
                        'p1': p1_value,
                        'p2': p2_value
                    }
                    self.append_if_not_duplicate(row_data, 'scraped_data.xlsx')
                except Exception:
                    continue
            
            # df = pd.DataFrame(scraped_data)
            # df.to_excel('scraped_data.xlsx', index=False)


 
        finally:
            print("Done")



# Example usage
def main():
    scraper_1 = OddsPortal()
    
    scraper_1.scrape("https://www.oddsportal.com/tennis/argentina/atp-buenos-aires/results/")

if __name__ == "__main__":
    main()
