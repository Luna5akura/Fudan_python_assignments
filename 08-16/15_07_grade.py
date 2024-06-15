import pandas as pd


def main():
    df = pd.read_csv("grades.csv")
    df["平均成绩"] = df.iloc[:, 2:].mean(axis=1)
    df_sorted = df.sort_values(by='平均成绩', ascending=False)

    num_students = len(df_sorted)
    num_A = round(num_students * 0.25)
    num_B = round(num_students * 0.50) - num_A
    num_C = round(num_students * 0.75) - num_A - num_B
    num_D = num_students - num_A - num_B - num_C

    grades = ['A'] * num_A + ['B'] * num_B + ['C'] * num_C + ['D'] * num_D
    df_sorted['等级'] = grades

    df_sorted = df_sorted.sort_index()

    result_df = df_sorted[['学号', '姓名', '等级']]
    result_df.to_csv('graded.csv', index=False)


if __name__ == '__main__':
    main()
