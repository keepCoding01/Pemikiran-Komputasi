import random


def prim(graph, n):
    visited = [False] * n
    key = [10**9] * n
    parent = [-1] * n

    start = random.randint(0, n - 1)
    key[start] = 0

    total_cost = 0
    for _ in range(n):
        min_key = 10**9
        min_city = -1
        for j in range(n):
            if not visited[j] and key[j] < min_key:
                min_key = key[j]
                min_city = j

        if min_city == -1:
            break

        visited[min_city] = True
        total_cost += key[min_city]

        for neighbor in graph[min_city]:
            if not visited[neighbor] and graph[min_city][neighbor] < key[neighbor]:
                key[neighbor] = graph[min_city][neighbor]
                parent[neighbor] = min_city

    return total_cost


def main():
    # Input: number of cities/districts and cost of the chosen generator
    n, m = map(int, input().strip().split())
    graph = {}
    city_index = {}
    index_city = {}
    index = 0

    total_tunnel_length = 0

    for i in range(n):
        city = input().strip()
        if city not in city_index:
            city_index[city] = index
            index_city[index] = city
            graph[city_index[city]] = {}
            index += 1

        neighbors = input().strip().split()
        for j in range(0, len(neighbors), 2):
            neighbor = neighbors[j]
            distance = int(neighbors[j + 1])
            if neighbor not in city_index:
                city_index[neighbor] = index
                index_city[index] = neighbor
                graph[city_index[neighbor]] = {}
                index += 1

            graph[city_index[city]][city_index[neighbor]] = distance
            graph[city_index[neighbor]][city_index[city]] = distance
            total_tunnel_length += distance

    # The total length of tunnels is counted twice (once for each direction), so we divide by 2
    total_tunnel_length //= 2

    total_cost = prim(graph, n)

    # The total cost includes the cost of the generator and the cost of the MST
    total_cost_with_generator = total_cost * 2 + m

    print(f"{total_cost_with_generator} juta")


if __name__ == "__main__":
    main()
