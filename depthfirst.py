# imported deque from collections module
from collections import deque

def solve(maze):
    start = maze.start
    end = maze.end
    width = maze.width
    stack = deque([start]) # stack is used for DFS
    shape = (maze.height, maze.width)
    prev = [None] * (maze.width * maze.height) # initialize prev as None
    visited = [False] * (maze.width * maze.height) # mark visited as false for all the nodes initially
    count = 0

    completed = False 
    
    while stack:
        count += 1
        current = stack.pop()

        if current == end: # if current is the destination node then stop here only.
            completed = True
            break

        visited[current.Position[0] * width + current.Position[1]] = True 

        for n in current.Neighbours:
            if n != None:
                npos = n.Position[0] * width + n.Position[1]
                if visited[npos] == False:
                    stack.append(n)
                    prev[npos] = current

    path = deque()
    current = end
    while (current != None): #retracing the path from destination to start point
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
