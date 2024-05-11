# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import pandas as pd

# class OddsPortal:
    
#     def __init__(self) -> None:
#         self.driver = webdriver.Chrome()

#     def scroll_to_load_games(self):
#         for _ in range(5):
#             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)

#     def append_if_not_duplicate(self, row_data, excel_path, sheet_name='Sheet1'):
#         try:
#             df_existing = pd.read_excel(excel_path, sheet_name=sheet_name)
#         except FileNotFoundError:
#             df_existing = pd.DataFrame(columns=row_data.keys())
        
#         if not df_existing[df_existing['Page_URL'] == row_data['Page_URL']].empty:
#             print("Data for this Page_URL already exists in the Excel sheet. Skipping duplicate.")
#         else:
#             df_existing = pd.concat([df_existing, pd.DataFrame([row_data])], ignore_index=True)
#             df_existing.to_excel(excel_path, index=False, sheet_name=sheet_name)
#             print("Data appended successfully.")

#     def get_page_list(self):
#         Orig_urls = '/html/body/div[1]/div[1]/div[1]/div/main/div[3]/div[3]/div/div[2]/a'
#         Orig_URLs = self.driver.find_elements(By.XPATH, Orig_urls)
#         return [orig_result.get_attribute('href') for orig_result in Orig_URLs]

#     def get_data_from_page(self, page):
#         self.driver.get(page)
#         time.sleep(5)
#         data = {}
#         try:
#             data['bookmark'] = self.driver.find_element(By.XPATH, bookmark_path).text
#             data['odd1_value'] = self.driver.find_element(By.XPATH, odd1).text
#             data['odd2_value'] = self.driver.find_element(By.XPATH, odd2).text
#             # ... add all the other data extractions here ...
#         except Exception as e:
#             print(f"Error extracting data from page: {e}")
#         return data

#     def scrape(self, ori_url):
#         self.driver.get(ori_url)
#         time.sleep(5)
#         self.scroll_to_load_games()
#         pages_list = self.get_page_list()
#         print(f'pages_list : {pages_list}')
#         print(f'lenght of pages_list : {len(pages_list)}')
        
#         for page in pages_list:
#             row_data = self.get_data_from_page(page)
#             if row_data:
#                 self.append_if_not_duplicate(row_data, 'scraped_data.xlsx')

#         print("Done")

# def main():
#     scraper = OddsPortal()
#     scraper.scrape("https://www.oddsportal.com/tennis/argentina/atp-buenos-aires/results/")

# if __name__ == "__main__":
#     main()
