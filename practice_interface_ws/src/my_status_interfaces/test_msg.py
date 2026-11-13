from my_status_interfaces.msg import Student

def main():
    stu = Student()
    stu.name =   '张三'
    stu.age = 20
    stu.score = 95.5

    print(f"姓名:{stu.name}")
    print(f"年龄:{stu.age}")
    print(f"分数：{stu.score}")

if __name__ == '__main__':
  main()