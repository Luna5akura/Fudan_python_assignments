students = {
    200001: {'name': '张三', 'gender': '男', 'age': 19, 'score': 598},
    200016: {'name': '芳芳', 'gender': '女', 'age': 19, 'score': 605},
    202201: {'name': '圆圆', 'gender': '女', 'age': 18, 'score': 586},
    202336: {'name': '李四', 'gender': '男', 'age': 18, 'score': 635},
    202318: {'name': '王五', 'gender': '男', 'age': 18, 'score': 618},
    202112: {'name': '佳佳', 'gender': '女', 'age': 18, 'score': 620}
}


def main():
    while True:
        print("=" * 30,
              "\n1. 显示ID为202201的学生信息"
              "\n2. 按ID查询学生信息"
              "\n3. 显示所有学生信息"
              "\n4. 统计男女生人数,显示年龄>18岁的学生"
              "\n5. 显示成绩最高的学生信息"
              "\n0. 退出程序\n",
              "=" * 30)

        choice = input("请输入选项: ")

        if choice == '1':
            ids = 202201
            info = students.get(ids)
            if info:
                print(
                    f"学号:{ids}, 姓名:{info['name']}, 性别:{info['gender']}, 年龄:{info['age']}, 成绩:{info['score']}")
            else:
                print("未找到该学生信息")

        elif choice == '2':
            ids = int(input("请输入要查询的学生ID: "))
            info = students.get(ids)
            if info:
                print(
                    f"学号:{ids}, 姓名:{info['name']}, 性别:{info['gender']}, 年龄:{info['age']}, 成绩:{info['score']}")
            else:
                print("未找到该学生信息")

        elif choice == '3':
            for ids, info in students.items():
                print(
                    f"学号:{ids}, 姓名:{info['name']}, 性别:{info['gender']}, 年龄:{info['age']}, 成绩:{info['score']}")

        elif choice == '4':
            male_count = female_count = 0
            print("年龄大于18岁的学生:")
            for info in students.values():
                if info['gender'] == '男':
                    male_count += 1
                else:
                    female_count += 1

                if info['age'] > 18:
                    print(info['name'])

            print(f"男生: {male_count}人, 女生: {female_count}人")

        elif choice == '5':
            max_score = 0
            top_student = None
            for ids, info in students.items():
                if info['score'] > max_score:
                    max_score = info['score']
                    top_student: dict[int:dict] = (ids, info)

            print(
                f"成绩最高的学生: 学号:{top_student[0]}, 姓名:{top_student[1]['name']}, 成绩:{top_student[1]['score']}")

        elif choice == '0':
            print("程序已退出")
            break

        else:
            print("无效的选项,请重新输入")


if __name__ == '__main__':
    main()
