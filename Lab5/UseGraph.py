
import Graph

#ga1 = Graph.GraphAlgorithms('graph-1.txt')
#ga2 = Graph.GraphAlgorithms('graph-2.txt')
#ga3 = Graph.GraphAlgorithms('graph-3.txt')
#ga4 = Graph.GraphAlgorithms('graph-4.txt')

ga1 = Graph.GraphAlgorithms("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab5/graph-1.txt")
ga2 = Graph.GraphAlgorithms("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab5/graph-2.txt")
ga3 = Graph.GraphAlgorithms("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab5/graph-3.txt")
ga4 = Graph.GraphAlgorithms("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab5/graph-4.txt")

print("DFS recursive:")
print(ga1.DFS('recursive'))
print(ga2.DFS('recursive'))
print(ga3.DFS('recursive'))
print(ga4.DFS('recursive'))

print("DFS stack:")
print(ga1.DFS('stack'))
print(ga2.DFS('stack'))
print(ga3.DFS('stack'))
print(ga4.DFS('stack'))

print("BFS:")
print(ga1.BFS())
print(ga2.BFS())
print(ga3.BFS())
print(ga4.BFS())


print("hasCycle?")
print(ga1.hasCycle())

#print("Shortest path from a to f:")
#print(ga1.shortestpath('a','f'))

