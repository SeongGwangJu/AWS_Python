from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
import pandas as pd
class UserRepository:

    @staticmethod
    def saveUser(user=None):
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


    @staticmethod
    def getUsersAll():
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
        rs = cursor.fetchall() #
        return rs

if __name__ == "__main__":
    userList = UserRepository.getUsersAll()
    print(userList)


    data = {
        "userId": [1, 2, 3],
        "username": ["aaa", "bbb", "ccc"],
        "password": ["1234", "1111", "2222"],
        "name": ["aaa", "bbb", "ccc"],
        "email": ["aaa@gmail.com", "bbb@naver.com", "ccc@hanmail.net"]
    }
    # 출력해보면 pandas가 깔끔하게 표 형식으로 정리해줌. *pandas as pd
    df = pd.DataFrame(userList)
    print(df)
    # print(df.get("username"))
