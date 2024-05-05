def flight(n, bookings: list[list[int]]):
    answer = [0 for _ in range(n)]
    for booking in bookings:
        answer[booking[0] - 1:booking[1]] = [x + booking[2] for x in answer[booking[0] - 1:booking[1]]]
    print(answer)


if __name__ == "__main__":
    flight(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]])
