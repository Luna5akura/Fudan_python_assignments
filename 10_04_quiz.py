students = {
    '赵': ['Python', 'C'],
    '钱': ['Python', 'VB', 'C'],
    '孙': ['VB'],
    '李': ['Python'],
    '周': ['Python', 'C'],
    '吴': ['VB'],
    '郑': ['VB'],
    '王': ['C'],
    '冯': ['Python'],
    '陈': ['C'],
    '褚': ['Python', 'VB'],
    '卫': ['VB', 'C']
}


def main():
    all_students = set(students.keys())
    print("所有参与调查的学生:", all_students)

    two_lang_students = {name for name, langs in students.items() if len(langs) == 2}
    print("学过两门语言的学生:", two_lang_students)

    python_only = {name for name, langs in students.items() if langs == ['Python']}
    print("仅学过Python的学生:", python_only)

    vb_only = {name for name, langs in students.items() if langs == ['VB']}
    print("仅学过VB的学生:", vb_only)

    c_only = {name for name, langs in students.items() if langs == ['C']}
    print("仅学过C语言的学生:", c_only)

    one_lang = {name for name, langs in students.items() if len(langs) == 1}
    print("仅学过一门语言的学生:", one_lang)


if __name__ == '__main__':
    main()
