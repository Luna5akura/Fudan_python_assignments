from collections import deque


def load_data(file_path):
    graph = {}
    id_to_station = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            station_id, line_name, station_name, transfer_ids = data
            id_to_station[station_id] = (line_name, station_name)
            if line_name not in graph:
                graph[line_name] = {}
            graph[line_name][station_name] = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            station_id, line_name, station_name, transfer_ids = data
            for transfer_id in transfer_ids.split('/'):
                if transfer_id:
                    transfer_line, transfer_station = id_to_station[transfer_id]
                    graph[line_name][station_name].add((transfer_line, transfer_station))

    return graph


def bfs(graph, start_line, start_station, end_line, end_station):
    print(f"BFS: 起点 {start_line} {start_station}, 终点 {end_line} {end_station}")
    queue = deque([((start_line, start_station), [(start_line, start_station)])])
    visited = {(start_line, start_station)}

    while queue:
        (line, station), path = queue.popleft()
        if line == end_line and station == end_station:
            return path

        for next_station in graph[line]:
            if (line, next_station) not in visited:
                queue.append(((line, next_station), path + [(line, next_station)]))
                visited.add((line, next_station))

        for transfer_line, transfer_station in graph[line][station]:
            if (transfer_line, transfer_station) not in visited:
                queue.append(((transfer_line, transfer_station), path + ["换乘", (transfer_line, transfer_station)]))
                visited.add((transfer_line, transfer_station))

    print(f"BFS: 没有找到从 {start_line} {start_station} 到 {end_line} {end_station} 的路径")
    return None


def print_path(path):
    print(path)
    if not path:
        print("没有找到换乘路线")
        return

    current_line = ""
    for station in path:
        if station == "换乘":
            print(station)
        else:
            line_name, station_name = station
            if line_name != current_line:
                current_line = line_name
                print(f"{line_name}: ", end="")
            print(station_name, end=" ")
    print()


def main(input_str):
    start_line, start_station, end_line, end_station = input_str.replace('-', '，').split('，')
    print(f"起点: {start_line.strip()} {start_station.strip()}")
    print(f"终点: {end_line.strip()} {end_station.strip()}")
    graph = load_data('线路.csv')
    path = bfs(graph, start_line.strip(), start_station.strip(), end_line.strip(), end_station.strip())
    print_path(path)


if __name__ == '__main__':
    main("18号线，复旦大学-10号线，交通大学")
    main("18号线，上海财经大学-8号线，东方体育中心")