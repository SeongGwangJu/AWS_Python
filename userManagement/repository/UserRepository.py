from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
import pandas as pd
class UserRepository:

    @staticmethod
    def saveUser(user=None):
        try:
            connection = DataBaseConfig.getConnection()
            #커서 생성, 커서
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            #f포맷팅을 하는것보다, 커서가 대신 . %s = String
            sql = """
            insert into user_tb
            values(0, %s, %s, %s, %s) 
            """

            #execute는 int, 성공횟수를 return함
            insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
            connection.commit() #insert 마무리
            return insertCount
        except Exception as e : #catch 대신 except.
            print(e)
            return 0

    @staticmethod
    def getUsersAll():
        try:
            connection = DataBaseConfig.getConnection()

            # cursor = connection.cursor()
            # 출력 : Tuple Type : ((1, 'Gwang', '1234', '주성광', 'jusg0721@naver.com'),)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            #출력 : Dict Type : [{'userId': 1, 'username': 'Gwang', 'password': '1234', 'name': '주성광', 'email': 'jusg0721@naver.com'}]

            sql = """
            select
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            """

            cursor.execute(sql)
            rs = cursor.fetchall() ## 모든 사용자를 딕셔너리 목록으로 가져옴
            # rs = cursor.fetchone() ## 단일 사용자 정보를 딕셔너리로 가져옴
            return rs
        except Exception as e :
            print(e)
            return None

if __name__ == "__main__":
    userList = UserRepository.getUsersAll()
    print(userList)

    # 출력해보면 pandas가 깔끔하게 표 형식으로 정리해줌. *pandas as pd로 정의됨
    # dataFrame은 list나 tuple만 가능.
    df = pd.DataFrame(userList)
    print(df)
    # print(df.get("username"))
