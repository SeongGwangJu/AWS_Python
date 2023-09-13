class UserView:

    @staticmethod #싱글톤 대신
    def register():
        from userManagement.entity.User import User
        from userManagement.controller.UserController import UserController
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

