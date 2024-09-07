

import math
        #################### RACING LINE ######################

        # Optimal racing line for the reinvent_base
        # Each row: [x,y,speed,timeFromPreviousPoint]

racing_track = [[3.06848, 0.70271, 3.42259, 0.04239],
[3.21467, 0.69489, 3.83516, 0.03817],
[3.36204, 0.6896, 4.0, 0.03687],
[3.51032, 0.6863, 4.0, 0.03708],
[3.65926, 0.68449, 4.0, 0.03724],
[3.80865, 0.68372, 4.0, 0.03735],
[3.95832, 0.68357, 4.0, 0.03742],
[4.10807, 0.68364, 4.0, 0.03744],
[4.25759, 0.68422, 4.0, 0.03738],
[4.40677, 0.68558, 3.67333, 0.04061],
[4.55544, 0.688, 3.38677, 0.0439],
[4.70346, 0.69176, 3.12483, 0.04738],
[4.85065, 0.69716, 2.87543, 0.05122],
[4.99682, 0.70451, 2.65833, 0.05506],
[5.14179, 0.7141, 2.45557, 0.05916],
[5.28528, 0.72629, 2.26777, 0.06351],
[5.42704, 0.74147, 2.09436, 0.06807],
[5.56674, 0.76003, 1.93344, 0.07289],
[5.704, 0.78243, 1.78318, 0.07799],
[5.83839, 0.80911, 1.64161, 0.08346],
[5.96942, 0.84054, 1.50723, 0.0894],
[6.09651, 0.8772, 1.366, 0.09683],
[6.21901, 0.9196, 1.25195, 0.10354],
[6.33615, 0.96819, 1.15336, 0.10996],
[6.44705, 1.02346, 1.15336, 0.10743],
[6.55066, 1.08583, 1.08627, 0.11132],
[6.64569, 1.15569, 1.0, 0.11795],
[6.73033, 1.2335, 1.0, 0.11498],
[6.80265, 1.31928, 1.0, 0.11219],
[6.86038, 1.41254, 1.0, 0.10968],
[6.90409, 1.51128, 1.0, 0.10798],
[6.93124, 1.61454, 1.0, 0.10677],
[6.93872, 1.72028, 1.06227, 0.09979],
[6.92879, 1.82563, 1.10899, 0.09542],
[6.90352, 1.92883, 1.10899, 0.09581],
[6.86433, 2.0287, 1.10899, 0.09674],
[6.80932, 2.123, 1.17602, 0.09284],
[6.74022, 2.21057, 1.28175, 0.08702],
[6.6592, 2.29111, 1.40169, 0.0815],
[6.56806, 2.3647, 1.53508, 0.07631],
[6.46829, 2.43165, 1.69599, 0.07084],
[6.36128, 2.4925, 1.88834, 0.06519],
[6.24826, 2.54791, 2.14966, 0.05855],
[6.13048, 2.59877, 2.49815, 0.05136],
[6.00908, 2.64606, 3.09149, 0.04214],
[5.88526, 2.69089, 3.77629, 0.03487],
[5.76018, 2.73441, 3.5493, 0.03731],
[5.6294, 2.78066, 3.45367, 0.04017],
[5.4989, 2.82799, 3.44442, 0.0403],
[5.36884, 2.87677, 3.44442, 0.04033],
[5.23938, 2.92739, 3.44442, 0.04036],
[5.1107, 2.98024, 3.44442, 0.04039],
[4.98298, 3.03562, 3.44442, 0.04041],
[4.85634, 3.09363, 3.44442, 0.04044],
[4.73081, 3.15429, 3.5107, 0.03971],
[4.6064, 3.21748, 3.66234, 0.0381],
[4.48305, 3.28298, 3.93736, 0.03547],
[4.36061, 3.3505, 4.0, 0.03495],
[4.23894, 3.41969, 4.0, 0.03499],
[4.11792, 3.49025, 3.61742, 0.03873],
[3.99742, 3.56192, 3.12065, 0.04493],
[3.87735, 3.63453, 2.7819, 0.05044],
[3.76025, 3.70627, 2.47894, 0.0554],
[3.64285, 3.77709, 2.23292, 0.0614],
[3.52491, 3.84625, 1.99616, 0.06849],
[3.40621, 3.91297, 1.99616, 0.06822],
[3.28654, 3.97645, 1.99616, 0.06786],
[3.16571, 4.03588, 1.99616, 0.06745],
[3.04358, 4.09025, 1.99616, 0.06697],
[2.92004, 4.13847, 1.99616, 0.06644],
[2.79508, 4.17906, 1.95051, 0.06736],
[2.6692, 4.21295, 1.86861, 0.06977],
[2.54265, 4.24011, 1.77324, 0.07299],
[2.41572, 4.26047, 1.67246, 0.07687],
[2.28871, 4.27389, 1.56777, 0.08146],
[2.16198, 4.28022, 1.4605, 0.08688],
[2.03593, 4.27918, 1.36113, 0.09261],
[1.91107, 4.27026, 1.2377, 0.10114],
[1.78807, 4.25282, 1.1361, 0.10935],
[1.66779, 4.22615, 1.1361, 0.10845],
[1.55136, 4.1894, 1.1361, 0.10746],
[1.44024, 4.14171, 1.1361, 0.10643],
[1.33625, 4.08226, 1.1361, 0.10544],
[1.24205, 4.00979, 1.1361, 0.10461],
[1.16098, 3.92344, 1.18179, 0.10023],
[1.09328, 3.8255, 1.35734, 0.08771],
[1.03652, 3.71934, 1.4561, 0.08267],
[0.98994, 3.60626, 1.54274, 0.07927],
[0.95311, 3.48712, 1.63959, 0.07605],
[0.9256, 3.36271, 1.73457, 0.07346],
[0.90707, 3.23368, 1.84315, 0.07073],
[0.89712, 3.10068, 1.96833, 0.06776],
[0.89525, 2.96444, 2.09197, 0.06514],
[0.90099, 2.82565, 2.20339, 0.06304],
[0.91393, 2.68511, 2.18243, 0.06467],
[0.93374, 2.54373, 2.10752, 0.06774],
[0.96012, 2.40254, 2.03704, 0.07051],
[0.99285, 2.26269, 1.96514, 0.07309],
[1.03184, 2.12537, 1.89174, 0.07546],
[1.07701, 1.99168, 1.82429, 0.07736],
[1.12824, 1.86241, 1.70707, 0.08146],
[1.18548, 1.73816, 1.59245, 0.0859],
[1.24868, 1.61937, 1.47507, 0.09122],
[1.31787, 1.50639, 1.47507, 0.08981],
[1.39312, 1.39961, 1.47507, 0.08856],
[1.47453, 1.2994, 1.47507, 0.08753],
[1.56262, 1.20663, 1.47507, 0.08673],
[1.65804, 1.12241, 1.47507, 0.08628],
[1.76166, 1.04833, 1.58215, 0.08051],
[1.87225, 0.98336, 1.69345, 0.07574],
[1.98886, 0.92668, 1.80844, 0.07169],
[2.11077, 0.87763, 1.9275, 0.06818],
[2.2374, 0.83566, 2.0561, 0.06488],
[2.36821, 0.80024, 2.19585, 0.06172],
[2.50273, 0.7709, 2.36068, 0.05832],
[2.64049, 0.74709, 2.56548, 0.05449],
[2.78099, 0.72819, 2.79651, 0.05069],
[2.92379, 0.7136, 3.08356, 0.04655]]

        #################### END RACING LINE ######################

racing_track_points_count = len(racing_track)
reward_min = 1e-3  ## due to problem in learnin engine
reward_max = 1e0
speed_max = 4
max_steering_angle_speeds=[
  [-30,2.00],
  [-20,2.50],
  [-10,3.70],
  [-5,  4.0],
  [5,  3.70],
  [10, 2.50],
  [20, 2.00],
  [30, 0]
  ]
def max_steering_angle_speed(angle):
    for i in range(len(max_steering_angle_speeds)):
      if angle <  max_steering_angle_speeds[i][0]:
        return max_steering_angle_speeds[i][1]
    return 0

class Reward:
    def __init__(self, verbose=False):
        self.first_racingpoint_index = None
        self.verbose = verbose
        self.race_line_angles=None

        self.last_reward=0
        self.last_x=racing_track[0][0]
        self.last_y=racing_track[0][1]
        self.last_distance_race_line=0
        self.last_heading=0
        self.last_heading_optimal=0
        self.last_speed=0
        self.last_speed_optimal=speed_max


    def reward_function(self, params):

        def distance_between_points(p1,p2):
            return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

        def triangle_area(a,b,c):
            s= (a+b+c)/2  # half perimeter
            return math.sqrt(s*(s-a)*(s-b)*(s-c))

        def triangle_height(base,a,b):
            return 2*triangle_area(base,a,b)/base

        def distance_to_racing_line(closest_coords, second_closest_coords, car_coords):
            raceline_distance = distance_between_points(closest_coords,second_closest_coords)
            if raceline_distance == 0:
                return 0
            b = distance_between_points(car_coords,closest_coords)
            c = distance_between_points(car_coords,second_closest_coords)
            try:
                return triangle_height(raceline_distance,b,c)
            except:
                return b

        def get_distances_2_raceline_points(coords):
            distances = []
            for i in range(racing_track_points_count):
                distances.append(distance_between_points(racing_track[i],coords))
            return distances

        def closest_2_racing_points_index(car_coords):
            distances = get_distances_2_raceline_points(car_coords)

            closest_index = distances.index(min(distances))
            if closest_index is None:
                raise Exception("closest_index is none")
            last_index = closest_index -1
            if last_index == -1:
                last_index=racing_track_points_count-1
            next_index = closest_index + 1
            if next_index == racing_track_points_count:
                next_index = 0
            second_closest_index=next_index
            if distances[next_index] > distances[last_index] :
                next_index=closest_index
                second_closest_index=last_index
            return [closest_index, second_closest_index,next_index,last_index]

        def slope (p1,p2):
            if p2[1] == p1[1] or p2[0]==p1[0]: 
                return 0
            return (p2[1]-p1[1])/(p2[0]-p1[0])
        def line_angle(p1,p2):
            return math.degrees(math.atan(slope(p1,p2)))
        def lines_angle_difference(line1point1,line1point2,line2point1,line2point2):
            return line_angle(line1point1,line1point2)-line_angle(line2point1,line2point2)

        def get_raceline_angles():
            angles=[]
            for i in range(racing_track_points_count-1):
                angles.append(line_angle(racing_track[i],racing_track[i+1]))
            angles.append(line_angle(racing_track[racing_track_points_count-1],racing_track[0]))
            return angles
     
        def get_last_raceline_similar_direction(pointIndex):
            baseAngle=self.race_line_angles[pointIndex]
            for i in range(pointIndex+1,racing_track_points_count):
                if abs(baseAngle - self.race_line_angles[i]) > 5:
                    return i-1
            for i in range(0,pointIndex):
                if abs(baseAngle - self.race_line_angles[i]) > 5:
                    return i-1
            raise Exception("all can't be the same for a lap")

        def get_optimal_angle(position,target_index):
            target_point=get_last_raceline_similar_direction(target_index)
            return line_angle(position,racing_track[target_point])

        ################## INPUT PARAMETERS ###################

        all_wheels_on_track = params['all_wheels_on_track']
        x = params['x']
        y = params['y']
        distance_from_center = params['distance_from_center']
        is_left_of_center = params['is_left_of_center']
        heading = params['heading']
        progress = params['progress']
        steps = params['steps']  ## step = constant duration in time
        speed = params['speed']
        steering_angle = params['steering_angle']
        track_width = params['track_width']
        waypoints = params['waypoints']
        closest_waypoints = params['closest_waypoints']
        is_offtrack = params['is_offtrack']

        ################## CALCULATION ###################

        closest_index, second_closest_index, next_point, last_point  = closest_2_racing_points_index([x, y])
        race_line_closest = racing_track[closest_index]                     # Get optimal [x, y, speed, time]
        race_line_second_closest = racing_track[second_closest_index]
        
        if steps == 1 or self.first_racingpoint_index is None:
            self.race_line_angles=get_raceline_angles()
            self.first_racingpoint_index = closest_index
        
        distance_race_line = distance_to_racing_line(race_line_closest[0:2], race_line_second_closest[0:2], [x, y])
        distance_race_line_change=distance_race_line - self.last_distance_race_line
        distance_reward = 1/(1 + distance_race_line)

        speed_optimal=race_line_closest[2]
        speed_diff = speed_optimal - speed
        speed_change=speed - self.last_speed
        speed_reward = 1/(1+abs(speed_diff))

        heading_optimal=get_optimal_angle([x, y],next_point)
        heading_diff=heading-heading_optimal
        heading_change=heading_optimal-self.last_heading_optimal
        heading_reward=1/(1+abs(heading_diff))
        
        reward_calculated = distance_reward * 0.25 + speed_reward *0.25 + heading_reward*0.5

        if speed == 0 or max_steering_angle_speed(steering_angle) < speed or all_wheels_on_track == False:  # totally wrong direction or too slow
            reward = reward_min
        else:
            reward = reward_calculated
        if self.verbose == True :
            print(f"SIMPRIB: {steps:d},{closest_index:d},{next_point:d},{last_point:d},{race_line_closest[0]:f},{race_line_closest[1]:f},{distance_race_line:f},{self.last_distance_race_line:f},{distance_race_line_change:f},{distance_reward:f},{speed_optimal:f},{speed_diff:f},{self.last_speed:f},{self.last_speed_optimal:f},{speed_change:f},{speed_reward:f},{heading},{heading_optimal},{steering_angle},{heading_diff},{self.last_heading:f},{self.last_heading_optimal:f},{heading_change:f},{heading_reward:f},{reward_calculated:f}")

            print(f"Steps: {steps:d}, Points closest: {closest_index:d} next: {next_point:d} last: {last_point:d}")
            print(f"  Location x: {x:f}, y: {y:f} optimal x: {race_line_closest[0]:f} y: {race_line_closest[1]:f}")
            print(f"  Distance to racing line: {distance_race_line:f} last: {self.last_distance_race_line:f} variance {distance_race_line_change:f}")
            print(f"      reward ==> {distance_reward:f}")
            print(f"  Speed actual: {speed:f} optimal: {speed_optimal:f} diff: {speed_diff:f} last: {self.last_speed:f} optimal: {self.last_speed_optimal:f} variance: {speed_change:f} ")
            print(f"      reward ==> {speed_reward:f}")        
            print(f"   Headinging actual: {heading} optimal: {heading_optimal} optimal: {steering_angle} diff: {heading_diff} last: {self.last_heading:f}  optimal: {self.last_heading_optimal:f} variance {heading_change:f} ")
            print(f"      reward ==> {heading_reward:f}")
            print(f"")
            print(f" reward ==> {reward:f} calculated: {reward_calculated:f} last: {self.last_reward:f}")
            print("-----------------------------------------------")
            
        self.last_reward=reward
        self.last_x=x
        self.last_y=y
        self.last_distance_race_line=distance_race_line
        self.last_heading=heading
        self.last_heading_optimal=heading_optimal
        self.last_speed=speed
        self.last_speed_optimal=speed_optimal
        return float(reward)

reward_object = Reward(True) # add parameter verbose=True to get more output

def reward_function(params):
    return reward_object.reward_function(params)
