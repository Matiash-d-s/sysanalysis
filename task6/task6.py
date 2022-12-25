import json
import numpy as np

def comp_m(column):
    c = len(column)
    res = np.zeros((c, c))
    for i in range(c):
        for j in range(c):
            val = 0
            if column[i] > column[j]:
                val = 1
            elif column[i] == column[j]:
                val = 0.5
            res[i][j] = val
    return res

def task(input_json: str):
    start_matrix = np.array(json.loads(input_json)).T
    comparision_matrix = []
    for col in range(start_matrix.shape[1]):
        comparision_matrix.append(comp_m(start_matrix[:, col]).T)
    avg_values = np.mean(comparision_matrix, axis=0)
    k0 = [1/start_matrix.shape[0] for i in range(start_matrix.shape[1])]
    y = np.dot(avg_values, k0)
    l = np.dot(np.ones(len(y)), y)
    k1 = np.dot(1/l, y)
    while max(abs(k1-k0)) >= 0.001:
        k0 = k1
        y = np.dot(avg_values, k0)
        l = np.dot(np.ones(len(y)), y)
        k1 = np.dot(1/l, y)
    return json.dumps([round(el, 3) for el in k1])
