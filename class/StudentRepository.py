class StudentRepository:

    def __init__(self):
        self.studentList = []
        # self.studentList = List() #와 같음

    def add(self, student):
        self.studentList.append(student)
        print("학생을 추가하였습니다.")

    def findStudentByName(self, name):
        for student in self.studentList:
            if student.name == name:
                return student
        return None

# def student():
    # pass
    #함수를 비우고 싶을때. 중괄호를 써놓고 리턴이 없으면 오류가난다.!
def main():
    from Student import Student
    #from: 모듈파일  import: 모듈 내부의 클래스,함수, 변수
    sr = StudentRepository()
    sr.add(Student("주성광, 30"))
    sr.add(Student("주성광2, 30"))
    sr.add(Student("주성광3, 30"))
    sr.add(Student("주성광4, 30"))
    print(sr.studentList)
    print(sr.findStudentByName("주성광"))
    print("학생저장소모듈", __name__)
main()
