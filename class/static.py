class UserInfo:
    #cls(class) 변수 == static변수
    adminUser = {
        "username": "root",
        "password": "1q2w3e4r"
    }

    #생성자.
    #self == this -> 자기자신의 주소(생성된 주소)
    #self를 쓰는 순간, 생성된 객체의 변수가 생긴다.
    #
    def __init__(self):
        self.adminUser = {
            "username": "user1",
            "password": "1234"
        }

    @classmethod
    def showAdminUser(cls):
        print("[showAdminUser]")
        print(cls.adminUser) #맨 위의 adminUser의미


#멤버변수 정의하는 방법
class User:

    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print("그냥 실행할 수 있는 메소드")

if __name__ == "__main__":
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(UserInfo.adminUser)
    # static 생성한 후의 참조..?

    userInfo.showAdminUser()
    # 생성되어야지만 호출할 수 있다.
    # 호출하려면 @classmethod와 매개변수 cls
    UserInfo.showAdminUser()

    #staticmethod를 붙이면, 생성없이도 가능
    User.showUserClassInfo()

