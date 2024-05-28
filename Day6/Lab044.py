class LoginPage:
    
    
    def __init__(self,pageName):
        self.page_name = pageName
        
    def display(self):
        print(self.page_name)
        

loginPage = LoginPage("loginPage")
print(loginPage.display())