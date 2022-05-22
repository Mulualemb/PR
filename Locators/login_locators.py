class LoginLocators:
    # shortcuts to elements/butons in login section
    login_button = "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]"
    login_enter_mail = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[1]"
    login_enter_pass = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[2]"
    sign_in_button = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/form[1]/input[3]"
    logout_button = "//button[contains(text(),'log out')]"
    h4txt = "//h4[contains(text(),'incorrect Password/Email')]"
