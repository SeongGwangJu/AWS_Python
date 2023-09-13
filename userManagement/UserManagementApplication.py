

def main():
    from userManagement.view.MenuView import MenuView
    #staticMethod인 index를 호출. False를 반환할 때 종료됨.
    while(MenuView.index()):
        pass
if __name__ == "__main__":
    main()
    print("프로그램이 종료되었습니다.")