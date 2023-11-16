import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from market_research.tools import WebDriver


class Amazon():
    def __init__(self, webdriver_path: str, browser_path: str=None, enable_headless=True):
        self.web_driver = WebDriver(executable_path=webdriver_path, browser_path=browser_path, headless=enable_headless)
        self.wait_time = 1


    def get_allcomments(self,url:str="https://www.amazon.com/sony-qd-oled-7-1-4ch-theater-speaker/product-reviews/b0cbdjkr1v/ref=cm_cr_arp_d_paging_btm_2?ie=utf8&pagenumber=2",
                        maker=None, product=None) -> list:
        allcomments_list = []
        page_url = url
        while True:
            driver = self.web_driver.get_chrome()
            page_url = page_url.lower()
            print(f"connecting to {page_url}")
            driver.get(page_url)
            time.sleep(self.wait_time)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            allcomments_list.extend(self._get_comments(soup=soup, url=url, maker=maker, product=product))
            print(f"ppp: {allcomments_list[-1]['Comments']}")
            try:
                time.sleep(1)
                last_element = driver.find_element(By.CLASS_NAME, "a-last")
                last_link = last_element.find_element(By.TAG_NAME, 'a')
                # <a> 요소의 href 속성 값 가져오기
                page_url = last_link.get_attribute("href")
                print(page_url)
                driver.quit()
            except Exception as e:
                driver.quit()
                print("error")
                print(e)
                break  # 만약 다음 페이지가 없으면 반복문을 종료합니다.

        df=pd.DataFrame(allcomments_list)
        df = df.reset_index()
        # print(df.head())
        # print(df.tail())
        df.to_csv('test.csv', index=False)
        return allcomments_list



    def _get_comments(self, soup, url=None, maker=None, product=None) -> list:
        quote_contents = soup.find_all('div', class_='a-row a-spacing-small review-data')
        comments_list = []
        for quote_content in quote_contents:
            comments = quote_content.span.get_text(strip=True)
            comments_list.append({"url":url, 'Maker': maker, 'Product': product, 'Comments': comments})
            # print("comments:", comments)
        return comments_list


    def click_a_last(self, driver):
        try:
            last_element = driver.find_element(By.CLASS_NAME, "a-last")
            self.web_driver.move_element_to_center(last_element)
            # "a-last" 클래스를 가진 <a> 요소의 href 속성 값 가져오기
            last_link_url = last_element.get_attribute("href")

            last_element.click()
            time.sleep(1)
            driver.save_screenshot("sc.png")
            print("click")
        except Exception as e:
            print(f"에러 발생: {e}")
        finally:
            # 작업 완료 후 드라이버 종료
            return driver


