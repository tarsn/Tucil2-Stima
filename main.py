from closest_point_nd import get_closest_point_n_dimension 
from visualizer_3d import visualize_points

points, pair = get_closest_point_n_dimension()
if (len(points[0]) == 3):
  visualize_points(points, pair)