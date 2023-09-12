class Student:
    name = None
    age = None
    #생성자
    #self : this와 같다.  (자기 자신의 주소 =생성된 객체의 주소
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #toString()
    def __str__(self):
        return f"Student[name : {self.name}, age: {self.age}]"

    def setName(self, name):
        self.name = name

def main():
    s1 = Student("김준일", 30)
    print(s1)

if __name__ == "__main__":
    main()

#여기서 실행시키면 __main__이 출력되지만
print("학생모듈", __name__)
