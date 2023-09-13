class MenuView:

    @staticmethod
    def index():
        from userManagement.view.UserView import UserView
        print("[사용자 관리 프로그램]")
        print("1. 사용자 전체 조회")
        print("2. username으로 사용자 정보 검색")
        print("3. 사용자 등록")
        print("4. 사용자 수정")
        print("5. 사용자 삭제")
        select = input("메뉴 선택 >>>")

        if select =="q":
            return False
        elif select == "1":
            UserView.showAllUsers()
        elif select == "2":
            UserView.findUser()
        elif select == "3":
            UserView.register()
        elif select == "4":
            UserView.updateUser()
        elif select == "5":
            pass
        else:
            print("선택하신 번호는 등록되지 않은 메뉴입니다.")


        return True
