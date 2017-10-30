# Deque importes from collection module
from collections import deque

def solve(maze):
    start = maze.start #starting coordinated of the maze
    end = maze.end #End coordinates of the maze

    width = maze.width

    queue = deque([start])
    shape = (maze.height, maze.width)
    prev = [None] * (maze.width * maze.height) #To store the parent of the node for generating path 
    visited = [False] * (maze.width * maze.height) #To store the nodes visited

    count = 0

    completed = False # Flag to know end point reached or not

    visited[start.Position[0] * width + start.Position[1]] = True # mark source as visited

    while queue:
        count += 1
        current = queue.pop() 

        if current == end: #if current is the destination node then stop here only.
            completed = True
            break

        for n in current.Neighbours:
            if n != None:
                npos = n.Position[0] * width + n.Position[1]
                if visited[npos] == False: #if node n is not visited yet then put it into the queue
                    queue.appendleft(n)
                    visited[npos] = True # mark it as visited
                    prev[npos] = current # store its parent as current

    path = deque()
    current = end
    while (current != None): #tracing the path from destination to start
        path.appendleft(current)
        current = prev[current.Position[0] * width + current.Position[1]]

    return [path, [count, len(path), completed]]
