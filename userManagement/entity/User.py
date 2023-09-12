class User:

    def __init__(self, userId=None, username=None, password=None, name=None, email=None):
        self.userId = userId
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __str__(self):
        #"""를 사용할 떄 들여쓰기하면 들여쓰기까지 다 적용된다.
        return f"""[User]
userId :{self.userId}
username :{self.username}
password :{self.password}
name :{self.name}
email :{self.email}
        
        """