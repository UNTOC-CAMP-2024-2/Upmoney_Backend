from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_scholarships(limit=30):

    url = "https://onestop.pusan.ac.kr/page?menuCD=000000000000062#popup"
    driver = webdriver.Chrome()
    driver.get(url)

    # "50���� ����" �ɼ� ����
    select = Select(driver.find_element(By.ID, "pageSel"))
    select.select_by_value("20")

    # �����Ͱ� ������ �ε�� ������ ���
    WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "tr")) >= 15
    )

    results = []
    links = driver.find_elements(By.CSS_SELECTOR, "td.text-left a")  # <td class="text-left"> ������ <a> �±� ã��

    count = 0  # ó���� �׸� ��
    for index, link in enumerate(links):
        if count >= limit:  # ���ѵ� ���� ó��
            break
        if index < 5:  # ù 5�� �ǳʶٱ�
            continue

        link_text = link.text.strip()
        link.click()
        time.sleep(2)  # ������ �ε� ���
        current_url = driver.current_url

        results.append({"name": link_text, "link": current_url, "page_id": 0})
        count += 1

        # �ڷΰ���
        driver.back()
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.text-left a"))
        )
        links = driver.find_elements(By.CSS_SELECTOR, "td.text-left a")  # �ٽ� ��ũ�� ������

    driver.quit()
    return results
