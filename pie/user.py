'''class User:
    users = 0 #class variable
    user_name = None
    pwd = None
    
    def __init__(self,user_name,pwd):
        self.user_name = user_name #instance variable
        self.pwd = pwd
        User.users += 1
        
    
    def register(self):
        print("Registering " + self.user_name)
    
    def login(self):
        print("Logging In " + self.user_name)
        
              
user1 = User("vishnu","123")
user2 = User("ashish","bot")
user1.register()
user2.register()
user1.login()
user2.login()
print(User.users)'''



        
        
    