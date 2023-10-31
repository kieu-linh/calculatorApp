from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)


browser.get('https://kieu-linh.github.io/calculatorApp/')
# toi có một ví dụ test case như sau:
# browser.find_element(By.ID, "5").click()
# browser.find_element(By.ID, ".").click()
# browser.find_element(By.ID, "3").click()
# browser.find_element(By.ID, "*").click()
# browser.find_element(By.ID, "2").click()
# browser.find_element(By.ID, "equals").click()
# result_element = browser.find_element(By.ID, "style-3")
# result = result_element.text

# print(result)
# browser.quit()

# tạo 1 list test case
# test_case = ["5", ".", "3", "*", "2", "equals"]
# # duyệt qua từng phần tử trong list test case
# for i in test_case:
#     browser.find_element(By.ID, i).click()
# # lấy kết quả
# result_element = browser.find_element(By.ID, "style-3")
# result = result_element.text
# print(result)
# # browser.quit()
# # tạo 1 list kết quả mong muốn
# result_output = "10.6"
# # tạo 1 list kết quả thực tế
# actual_result = result
# so sánh kết quả mong muốn và kết quả thực tế
# if result_output == actual_result:
#     print("Test case passed")
# else:
#     print("Test case failed")

# ví dụ 2
# tao 1 list test case 2
test_case_2 = [["5", ".", "3", "*", "2", "equals"],
               ["1", ".", "4", "+", "7", "equals"],
               ["9", ".", "3", "-", "2", "equals"],
               ["5", ".", "3", "/", "2", "equals"],
               ["5", "3", "1", "2", "3", "1", "9", "*", "2", "equals"],
               ["equals"]
               # error case
               ]
# ta có 1 list kết quả mong muốn 2
expected_result_2 = {"10.6", "8.4", "7.3", "2.65",
                     "10624638", "Please enter a valid expression"}
# duyệt qua từng phần tử trong list test case 2
actual_result_2 = []
for i in test_case_2:
    for j in i:
        browser.find_element(By.ID, j).click()
    result_element = browser.find_element(By.ID, "style-3")
    actual_result_2.append(result_element.text)

print(actual_result_2),

for i in actual_result_2:
    if i in expected_result_2:
        print("Test case " + str(i) + " passed")
    else:
        print("Test case " + str(i) + " failed")
browser.quit()
