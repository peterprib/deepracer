import math

maxSteerAngleSpeed=[
  [-45,2.00],
  [-30,2.00],
  [-20,2.50],
  [-10,3.70],
  [0,  4.0],
  [10, 3.70],
  [20, 2.50],
  [30, 2.00]
  ]

def get_angle_target_speed(angle):
    is_inside = [dist(p, car) < r for p in maxSteerAngleSpeed]
    return 1


def get_target_speed():
    return 1

def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def rect(r, theta):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x, y

def polar(x, y):
    r = (x ** 2 + y ** 2) ** .5
    theta = math.degrees(math.atan2(y,x))
    return r, theta

def angle_mod_360(angle):
    """
    Maps an angle to the interval -180, +180.

    Examples:
    angle_mod_360(362) == 2
    angle_mod_360(270) == -90

    :param angle: angle in degree
    :return: angle in degree. Between -180 and +180
    """
    n = math.floor(angle/360.0)
    angle_between_0_and_360 = angle - n*360.0

    if angle_between_0_and_360 <= 180.0:
        return angle_between_0_and_360
    else:
        return angle_between_0_and_360 - 360

def get_waypoints_ordered_in_driving_direction(params):
    # waypoints are always provided in counter clock wise order
    if params['is_reversed']: # driving clock wise.
        return list(reversed(params['waypoints']))
    else: # driving counter clock wise.
        return params['waypoints']

def up_sample(waypoints, factor):
    """
    Adds extra waypoints in between provided waypoints

    :param waypoints:
    :param factor: integer. E.g. 3 means that the resulting list has 3 times as many points.
    :return:
    """
    p = waypoints
    n = len(p)

    return [[i / factor * p[(j+1) % n][0] + (1 - i / factor) * p[j][0],
             i / factor * p[(j+1) % n][1] + (1 - i / factor) * p[j][1]] for j in range(n) for i in range(factor)]


def get_target_point(params):
    waypoints = up_sample(get_waypoints_ordered_in_driving_direction(params), 20)

    car = [params['x'], params['y']]

    distances = [dist(p, car) for p in waypoints]
    min_dist = min(distances)
    i_closest = distances.index(min_dist)

    n = len(waypoints)

    waypoints_starting_with_closest = [waypoints[(i+i_closest) % n] for i in range(n)]

    r = params['track_width'] * 0.9

    is_inside = [dist(p, car) < r for p in waypoints_starting_with_closest]
    i_first_outside = is_inside.index(False)

    if i_first_outside < 0:  # this can only happen if we choose r as big as the entire track
        return waypoints[i_closest]

    return waypoints_starting_with_closest[i_first_outside]


def get_target_steering_degree(params):
    tx, ty = get_target_point(params)
    car_x = params['x']
    car_y = params['y']
    dx = tx-car_x
    dy = ty-car_y
    heading = params['heading']
    _, target_angle = polar(dx, dy)
    steering_angle = target_angle - heading
    return angle_mod_360(steering_angle)

def score_steer_to_point_ahead(params):
    best_stearing_angle = get_target_steering_degree(params)
    steering_angle = params['steering_angle']

    error = (steering_angle - best_stearing_angle) / 60.0  # 60 degree is already really bad
    score = 1.0 - abs(error)

    return max(score, 0.01)  # optimizer is rumored to struggle with negative numbers and numbers too close to zero

def reward_function(params):
    return float(score_steer_to_point_ahead(params))

def get_test_params():
    return {
        'x': 0.7,
        'y': 1.05,
        'heading': 160.0,
        'track_width': 0.45,
        'is_reversed': False,
        'steering_angle': 0.0,
        'waypoints': [
            [0.75, -0.7],
            [1.0, 0.0],
            [0.7, 0.52],
            [0.58, 0.7],
            [0.48, 0.8],
            [0.15, 0.95],
            [-0.1, 1.0],
            [-0.7, 0.75],
            [-0.9, 0.25],
            [-0.9, -0.55],
        ]
    }

def test_reward():
    params = get_test_params()
    reward = reward_function(params)
    print("test_reward: {}".format(reward))
    assert reward > 0.0

def test_get_target_point():
    result = get_target_point(get_test_params())
    expected = [0.33, 0.86]
    eps = 0.1
    print("get_target_point: x={}, y={}".format(result[0], result[1]))
    assert dist(result, expected) < eps

def test_get_target_steering():
    result = get_target_steering_degree(get_test_params())
    expected = 46
    eps = 1.0
    print("get_target_steering={}".format(result))
    assert abs(result - expected) < eps

def test_angle_mod_360():
    eps = 0.001
    assert abs(-90 - angle_mod_360(270.0)) < eps
    assert abs(-179 - angle_mod_360(181)) < eps
    assert abs(0.01 - angle_mod_360(360.01)) < eps
    assert abs(5 - angle_mod_360(365.0)) < eps
    assert abs(-2 - angle_mod_360(-722)) < eps

def test_upsample():
    params = get_test_params()
    print(repr(up_sample(params['waypoints'], 2)))

def test_score_steer_to_point_ahead():
    params_l_45 = {**get_test_params(), 'steering_angle': +45}
    params_l_15 = {**get_test_params(), 'steering_angle': +15}
    params_0 = {**get_test_params(), 'steering_angle': 0.0}
    params_r_15 = {**get_test_params(), 'steering_angle': -15}
    params_r_45 = {**get_test_params(), 'steering_angle': -45}

    sc = score_steer_to_point_ahead

    # 0.828, 0.328, 0.078, 0.01, 0.01
    print("Scores: {}, {}, {}, {}, {}".format(sc(params_l_45), sc(params_l_15), sc(params_0), sc(params_r_15), sc(params_r_45)))

def run_tests():
    test_angle_mod_360()
    test_reward()
    test_upsample()
    test_get_target_point()
    test_get_target_steering()
    test_score_steer_to_point_ahead()
    print("All tests successful")


# run_tests()
run_tests()

def reset_Values(p):
    p.heading = None
    p.speed = None
    p.steering_angle = None 
    p.steps = None
    p.direction_diff = None
    p.normalized_distance_from_route = None
    p.distance_from_center = None
    p.reward = None

class Previous:
    heading = None
    speed = None
    steering_angle = None 
    steps = None
    direction_diff = None
    normalized_distance_from_route = None
    distance_from_center = None
    reward = None

def reward_function(params):
    heading = params['heading']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    steering_angle = params['steering_angle']
    speed = params['speed']

    if previous.steps is None or steps < previous.steps:
        reset_Values(Previous)

    has_speed_dropped = False
    if previous._speed is not None or  previous.speed > speed:
    has_speed_dropped = previous.speed is not None or  previous.speed > speed
    #Penalize slowing down without good reason on straight portions
    if has_speed_dropped and not is_turn_upcoming: 
        speed_maintain_bonus = min( speed / previous.speed, 1 )
    #Penalize making the heading direction worse
    heading_decrease_bonus = 0
    if previous.direction_diff is not None:
        if is_heading_in_right_direction:
            if abs( previous.direction_diff / direction_diff ) > 1:
                heading_decrease_bonus = min(10, abs( previous.direction_diff / direction_diff ))
    #has the steering angle changed
    has_steering_angle_changed = False
    if previous.steering_angle is not None:
        if not(math.isclose(previous.steering_angle,steering_angle)):
            has_steering_angle_changed = True
    steering_angle_maintain_bonus = 1 
    #Not changing the steering angle is a good thing if heading in the right direction
    if is_heading_in_right_direction and not has_steering_angle_changed:
        if abs(direction_diff) < 10:
            steering_angle_maintain_bonus *= 2
        if abs(direction_diff) < 5:
            steering_angle_maintain_bonus *= 2
        if previous.direction_diff is not None and abs(previous.direction_diff) > abs(direction_diff):
            steering_angle_maintain_bonus *= 2
    #Reward reducing distance to the race line
    distance_reduction_bonus = 1
    if previous.normalized_distance_from_route is not None and previous.normalized_distance_from_route > normalized_distance_from_route:
        if abs(normalized_distance_from_route) > 0:
            distance_reduction_bonus = min( abs( previous.normalized_distance_from_route / normalized_distance_from_route ), 2)
    # Before returning reward, update the variables


    previous.speed = speed
    previous.steering_angle = steering_angle
    previous.direction_diff = direction_diff
    previous.steps = steps
    previous.normalized_distance_from_route = normalized_distance_from_route