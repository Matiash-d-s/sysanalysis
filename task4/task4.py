from io import StringIO
import math
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    direct_management = []
    direct_subordination=[]
    indirect_management=[]
    indirect_subordination=[]
    subordination=[]
    result = []
    vertexes = []
    s = 0

    for row in reader:
        graph.append(row)
    for x in graph:
        for y in x:
            y = int(y)
    for x in graph:
        direct_management.append(x[0])
    for x in graph:
        direct_subordination.append(x[1])
    f = graph
    g = graph
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] == g[j][0]:
                indirect_management.append(f[i][0])
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][1]:
                indirect_subordination.append(f[i][1])
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][0]:
                subordination.append(f[i][1])
    for x in graph:
        for y in x:
            if y not in vertexes:
                vertexes.append(y)
    vertexes.sort()

    for v in vertexes:
        result.append([])
    for v in vertexes:
        a = int(v) - 1
        result[a].append(direct_management.count(v))
        result[a].append(direct_subordination.count(v))
        result[a].append(indirect_management.count(v))
        result[a].append(indirect_subordination.count(v))
        result[a].append(subordination.count(v))
    for j in range(len(vertexes)):
        for i in range(5):
            if result[j][i] != 0:
                s += (result[j][i] / (len(vertexes) - 1)) * math.log(result[j][i] / (len(vertexes) - 1), 2)

    return -s
