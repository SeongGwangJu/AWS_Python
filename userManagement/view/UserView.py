import pandas as pd
from userManagement.entity.User import User
from userManagement.controller.UserController import UserController

class UserView:

    @staticmethod
    def showAllUsers():
        print("전체 사용자 목록을 조회합니다.")
        response = UserController.showAllUsers()
        df = pd.DataFrame(response.body)
        print(df)


    @staticmethod
    def findUser():
        print("사용자 이름으로 정보를 조회합니다.")
        username = input("조회할 사용자 이름 >>> ")
        response = UserController.findUserByUsername(username)
        df = pd.Series(response.body)
        print(df)

    @staticmethod #싱글톤 대신
    def register():
        from userManagement.entity.User import User
        print("[사용자 등록화면]")
        username = input("사용자 이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        response = UserController.registerUser(User(
            username=username,
            password=password,
            name=name,
            email=email
        ))

        #
        if not response.__dict__.get("body"):
            print("데이터를 추가하는 중 오류가 발생하였습니다")
            print("다시 시도해주세요.")

    @staticmethod
    def updateUser():
        print("[ 사용자 정보 수정 ]")
        response = UserController.showAllUsers()
        if not bool(response.body):
            print("수정 할 사용자 정보가 없습니다.")
            return
        df = pd.DataFrame(response.body)
        print(df)
        userId = input("수정하실 userId를 입력하세요 >>>")
        # df.index 안에는 내가 찾고자 하는 조건.
        # df["userId"] userId 컬럼 중, 입력받은 userId와 같은 데이터
        # values[0] : 어차피 userId가 같은건 하나니까 첫번째 데이터
        index = df.index[df["userId"] == int(userId)].values[0]
        user = UserView.showUpdateMenu(response.body[index])
        if not bool(user):
            print("수정을 취소하였습니다.")
            return

        response = UserController.updateUser(user)
        if(bool(response.body)):
            print("===============<< 수정 완료 >>===============")

    @staticmethod
    def showUpdateMenu(oldUser):
        # print(oldUser)
        # 깊은 복사를 통해 주소가 아닌 '값'을 복사한다.
        newUser = oldUser.copy()
        print("수정할 데이터를 선택해주세요.")

        while True:
            print("-" * 50)
            df = pd.DataFrame([oldUser, newUser], index=["수정 전", "수정 후"])
            print(pd.DataFrame([oldUser, newUser], index=["수정 전", "수정 후"]))
            print("-" * 50)
            print("1. password 수정 ")
            print("2. name 수정 ")
            print("3. email 수정 ")
            print("s. 저장")
            print("c. 취소")
            select = input("메뉴 선택 >>> ")

            if select == "c":
                return False
            elif select == "s":
                return newUser
            elif select == "1":
                password = input("비밀번호 입력 >>> ")

                if not UserView.isValid(oldUser.get("password"),password):
                    continue

                checkPassword = input("비밀번호 확인 >>> ")

                if checkPassword != password:
                    print("비밀번호가 일치하지 않습니다.")
                    continue

                newUser["password"] = password

            elif select == "2":
                name = input("이름 입력 >>> ")

                if not UserView.isValid(oldUser.get("name"), name):
                    continue

                newUser["name"] = name

            elif select == "3":
                email = input("이메일 입력 >>> ")

                if not UserView.isValid(oldUser.get("email"), email):
                    continue

                newUser["email"] = email
            else:
                print("선택하신 번호는 등록되지 않은 메뉴입니다.")
                print()

        return None

    @staticmethod
    def isValid(oldValue, value):
        if not bool(value):
            print("공백일 수 없습니다")
            return False
        elif oldValue== value:
            print("기존의 정보와 동일합니다")
            return False
        return True
