import json
import numpy as np


def matrix(ranking):
    r = dict()
    rank_len = ranking_length(ranking)
    for i, rank in enumerate(ranking):
        if type(rank) is str:
            r[int(rank)] = i
        else:
            for r in rank:
                r[int(r)] = i

    result = []
    for i in range(rank_len):
        result.append([1 if r[i + 1] <= r[j + 1] 
                       else 0 for j in range(rank_len)])
    return np.matrix(result)


def rank_L(ranking) -> int:
    l = 0
    for i in ranking:
        if type(i) is str:
            l += 1
        else:
            l += len(i)
    return l


def launch(str_a: str, str_b: str) -> str:
    ranking_a = json.loads(str_a)
    ranking_b = json.loads(str_b)
    y_a = relationship_matrix(ranking_a)
    y_a_t = y_a.transpose()
    y_b = relationship_matrix(ranking_b)
    y_b_t = y_b.transpose()
    y_a_b = np.multiply(y_a, y_b)
    y_a_b_t = np.multiply(y_a_t, y_b_t)
    conflicts = []

    for i in range(y_a_b.shape[0]):
        for j in range(y_a_b[i].shape[1]):
            if int(y_a_b[i, j]) == 0 and int(y_a_b_t[i, j]) == 0:
                if (str(j + 1), str(i + 1)) not in conflicts:
                    conflicts.append((str(i + 1), str(j + 1)))

    return json.dumps(conflicts)
