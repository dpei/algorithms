# Apr. 25 2016
# http://gregorulm.com/finding-an-eulerian-path/
# find eularian path in undirected graph

def find_eulerian_tour(graph):
             
    # frequency of each vertices in left
    # Later in the function, vertices on the right will be re stated
    def freqencies():
        my_list = [x for (x, y) in graph]
        result = [0 for i in range(max(my_list) + 1)]
        for i in my_list:
            result[i] += 1
        return result

    # Confirm if there are other vertices left
    # in the graph, if yes, return the vertice themselves
    # If no , return -1
    def find_node(tour):
        for i in tour:
            if freq[i] != 0:
                return i
        return -1

    # helper() is used to check if first path exhausted all edges,
    # If not, helper() will initiate another find_path() and combine
    # into the original one.
    def helper(tour, next):
        find_path(tour, next)
        u = find_node(tour)
        while sum(freq) != 0:     
            sub = find_path([], u)
            tour = tour[:tour.index(u)] + sub + tour[tour.index(u) + 1:]  
            u = find_node(tour)
        return tour
                  
    def find_path(tour, next):
        for (x, y) in graph:
            if x == next:
                # pop out edge that allows tour travel to next
                current = graph.pop(graph.index((x,y)))
                # pop out reverse edge cause they are the same
                graph.pop(graph.index((current[1], current[0])))
                tour.append(current[0])
                # update freq
                freq[current[0]] -= 1
                freq[current[1]] -= 1
                return find_path(tour, current[1])
        # append last vertice
        tour.append(next)
        return tour
              
    graph += [(y, x) for (x, y) in graph]
    freq = freqencies()   
    return helper([], graph[0][0])


graph1 = [(0, 1), (1, 2), (2, 0)]
# returns [0, 1, 2, 0]

graph2 = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2)]
# returns [0, 1, 2, 3, 4, 2, 0]

graph3 = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2), (4, 5), (5, 6), (6, 4)]
# returns [0, 1, 2, 3, 4, 5, 6, 4, 2, 0]


find_eulerian_tour(graph)

graph = [(0, 1), (1, 2), (2, 0)]