import numpy as np


HOLE_DIST = 0.2

def box_with_hole():
    return _edges_to_points([
        [0, 10, 0, 0],  # define edges like so: [x_a, y_a, x_b, y_b]
        [0, 0, 10, 0],  # (x_a, y_a) is the starting point of the edge
        [10, 0, 10, 10],  # (x_b, y_b) is the end point
        [0, 10, 4, 10],
        [6, 10, 10, 10]
    ])

def corridor():
    return _edges_to_points([
        [0, 0, 0, 10],
        [4, 0, 4, 10]
    ])

def _edges_to_points(edges):

    def dotted_edge(pt_a, pt_b):
        pt_a = pt_a.reshape(1, 2)
        pt_b = pt_b.reshape(1, 2)
        dist = np.linalg.norm(pt_b - pt_a)
        edge_range = (np.arange(0, dist, HOLE_DIST) / dist).reshape(-1, 1)
        dotted_edge_except_last_point = pt_a + edge_range * (pt_b - pt_a)
        return np.vstack([dotted_edge_except_last_point, pt_b])

    pts = np.array([0, 0]).reshape(1, 2)
    for i in range(len(edges)):
        pt_a = np.array([edges[i][0], edges[i][1]]).reshape(1, 2)
        pt_b = np.array([edges[i][2], edges[i][3]]).reshape(1, 2)
        new_pts = dotted_edge(pt_a, pt_b)
        pts = np.vstack([pts, new_pts])
    return pts[1:, :]
