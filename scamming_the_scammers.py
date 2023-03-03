# ----- Connect to chrome browser -----
import random
import time
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# 100 commonly used passwords
passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","696969","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","pussy","superman","1qaz2wsx","7777777","fuckyou","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","fuckme","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","asshole","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","fuck","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","6969","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix"]
# 100 common Indian names
indian_names = ["Muhammad","Sai","Advik","Rudra","Aayansh","Adi","Dhruv","Veer","Ahmed","Viyaan","Shiv","Atharv","Ivaan","Yuvaan","Ishaan","Kabir","Arjun","Shivay","Vihaan","Aarav","Agastya","Rian","Shivansh","Avyaan","Vedansh","Ayaan","Nathan","Riyaan","Anaynew","Emmanuel","Aidan","Aditya","George","Tejas","Advait","Vivaan","Krishna","Raghav","Reyansh","Ibrahim","Aaryan","Zayan","Zayne","Advit","Anand","Omnew","Parth","Rudransh","Vikramaditya","Kiaan","Saatvik","Kanha","Moksh","Krish","Madhav","Aarush","Nihit","Shlok","Adam","Pranav","Priyansh","Viraj","Rishaan","Ritvik","Ethan","Kartikeya","Shaurya","Joseph","Shreshth","Revaan","Aviraj","Jayden","Viransh","Zion","Pranit","Jay","Syed","Elvin","Chris","Ravi","Daksh","Saiyam","Ayman","Benjamin","Siddhant","Dhakshan","Farhan","Kavin","Lakshan","Manas","Aaro","Shravan","Anvit","Srihan","Tanish","Yuvi","Zohaa","Virat","Yohan","Kriyansh"]
# 100 random strings for PAN card
letters = ["VYFGBR","YJHMKY","YTENZA","JWHKGE","TSDALU","QFKSGK","BAYIZU","WJSISS","JLQVEX","WUSXEE","WMEXAP","WFQWPM","IDXEBA","PWIYRA","EELXVM","VNUIIK","OUUHRO","KREYSJ","QIHUMD","ETDAEE","JIPCID","CZVITE","YFTUDK","ZFEUSS","INBVWC","UJCNGK","AIFQPS","VDIYKQ","MXWTKP","QZMPYD","FVYJQW","RFAJUO","ZUOJNX","VIETNE","PWLEUM","SZMZRE","UNMGWT","LCXITJ","BRBHDK","YVGUUD","UBNGYF","XJYOYK","QSBJWH","IGRMTG","SHMHGX","UHYWUE","JWPSJX","CGCSEU","FQJEOY","SOLYGT","ZDGBTK","HKWMOO","TVAINB","TMVKAR","RYOPRO","PNZBRI","VIRNSE","HHOOBQ","ARZUXN","IMVWDH","APGEUF","MANKJQ","TEWRIR","MHCEFQ","NJWEMX","KSZKJT","SDGWAC","UJTSGO","OEQBLM","UCAMNL","CZHMEV","QVIMLQ","HZLKOI","XNQGTD","WMQCDS","XDERBK","DNSKTE","RRKTJC","ZDGZRX","GSGLRV","CVGWHG","YMUKBJ","BWEIWG","LGLVTV","PWUIEF","JQVDIO","NQJDKG","RANVNT","JHQLPB","JWPVZJ","JOOINR","GJPMHF","LXPHRV","VPKKHI","JOUHMU","KSYUJM","IUUIBQ","AXZWAQ","KJBQJW","AOZIBU"]
# scammers personal numbers
phone = ["<add scammers numbers here>"]

# loop for 3 times (testing)
for i in range(100):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    service = Service(executable_path=PATH)

    # ----- Wrote to get rid of bluetooth not there....something error -----
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # starts the browser
    driver = webdriver.Chrome(options=options, executable_path=PATH)


    # ----- navigating to a web page -----
    driver.get("https://nmxvxkyc.herokuapp.com/")

    time.sleep(3)

    # ----- filling the details -----
    user_id = driver.find_element(by=By.NAME, value="Usarname")
    cust_id = random.randint(1275836454, 9845634564)
    user_id.send_keys(cust_id)

    password = driver.find_element(by=By.NAME, value="Password")
    pwd = random.choice(passwords)
    password.send_keys(pwd)

    cell_no = driver.find_element(by=By.NAME, value="Mobile_No")
    # no = random.randint(8175836454, 9845634564)
    no = random.choice(phone)
    cell_no.send_keys(str(no) + Keys.ENTER) # --> when we press ENTER in the last field then no need to press 'submit' button later on

    time.sleep(3)

    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="submit")
    # submit_button.click()

    # ------ 2nd form
    pan_name = driver.find_element(by=By.CLASS_NAME, value="form-control")
    pn = random.choice(indian_names)
    pan_name.send_keys(pn)

    pan_no = driver.find_element(by=By.NAME, value="Pancard_No")
    # pattern --> "ABCDE1234E"
    alpha = random.choice(letters)
    num = random.randint(1000, 9999)
    single_letter = random.choice(string.ascii_letters).upper()
    pan = alpha + str(num) + single_letter
    pan_no.send_keys(pan + Keys.ENTER)

    time.sleep(3)

    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="submit")
    # submit_button.click()

    # --- OTP -- > min length 6 and max 8 all numbers
    otp = driver.find_element(by=By.NAME, value="OTP_1")
    otp_no = random.randint(100000, 999999)
    otp.send_keys(str(otp_no) + Keys.ENTER)

    time.sleep(3)

    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="submit")
    # submit_button.click()

    # --- 4th form
    acc_name = driver.find_element(by=By.NAME, value="Account_Holder_Name")
    acc = random.choice(indian_names)
    acc_name.send_keys(acc)

    birth_day = driver.find_element(by=By.NAME, value="DOB")
    day = random.randint(1947, 2010)
    birth_day.send_keys(str(day) + Keys.ENTER)

    time.sleep(3)

    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="submit")
    # submit_button.click()

    # --- otp2 -- min 6,... enter only that much
    otp2 = driver.find_element(by=By.NAME, value="OTP_2")
    otp_no2 = random.randint(100000, 999999)
    time.sleep(1)
    otp2.send_keys(str(otp_no2) + Keys.ENTER)

    time.sleep(3)

    driver.quit()

    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="submit")
    # submit_button.click()