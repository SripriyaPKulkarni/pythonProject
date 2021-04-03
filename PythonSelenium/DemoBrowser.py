from selenium import webdriver
#to invoke chrome browser
#driver = webdriver.Chrome(executable_path="C:\\Users\\Sri Priya P Kulkarni\\Softwares\\chromedriver.exe")

#driver=webdriver.Firefox(executable_path="C:\\Users\\Sri Priya P Kulkarni\\Softwares\\geckodriver-v0.29.0-win64\\geckodriver.exe")

driver=webdriver.Ie(executable_path="C:\\Users\\Sri Priya P Kulkarni\\Softwares\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")

driver.get("https://softwaretestingcafe.blogspot.com/")

driver.maximize_window()
print(driver.title)

print(driver.current_url)

driver.back()

driver.refresh()

print(driver.close())