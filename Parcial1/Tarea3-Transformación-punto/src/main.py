import numpy as np
m1 = np.array(
    [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 1]
    ]
)

m2 = np.array(
    [
        [1, 0, 0, 4],
        [0, 1, 0, -3],
        [0, 0, 1, 7],
        [0, 0, 0, 1]
    ]
)

m3 = np.array(
    [
        [0, -1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
)

point = np.array(
    [
        7,
        3,
        1,
        1
    ]
)

move = np.dot(m1, m2, m3)
print(move)
print(np.dot(move, point))
