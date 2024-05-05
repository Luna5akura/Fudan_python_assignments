def BMI1(name, height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"{name}的BMI是{bmi:.2f}，属于偏瘦。"
    elif bmi < 24:
        return f"{name}的BMI是{bmi:.2f}，属于正常体重。"
    elif bmi < 27:
        return f"{name}的BMI是{bmi:.2f}，属于偏胖。"
    else:
        return f"{name}的BMI是{bmi:.2f}，属于肥胖。"


def BMI2(*person):
    for lst in person:
        for p in lst:
            print(BMI1(*p))


if __name__ == "__main__":
    person1 = ("张三", 1.75, 60)
    person2 = ("李四", 1.65, 55)
    person3 = ("王五", 1.85, 80)

    print(BMI1(*person1))
    print(BMI1(*person2))
    print(BMI1(*person3))

    list1 = [("张三", 1.75, 60), ("李四", 1.65, 55), ("王五", 1.85, 80)]
    list2 = [person2, person3]
    BMI2(list1, list2)
