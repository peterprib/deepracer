import reward_function
import numpy as np
TRACK_NAME = 'reinvent_base'
waypoints = np.load("./tracks/%s.npy" % TRACK_NAME)
##print (waypoints)
import pandas as pd

def get_test_params():
    return {
    "all_wheels_on_track": True, ##Boolean,         # flag to indicate if the agent is on the track
    "x": 0.7, ## float,                             # agent's x-coordinate in meters
    "y": 1.05, ## float,                            # agent's y-coordinate in meters
    "closest_objects":[] , ## [int, int],           # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints":[] , ## [int, int],         # indices of the two nearest waypoints.
    "distance_from_center": 0 , ## float,           # distance in meters from the track center 
    "is_crashed": False, ## Boolean,                # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": False, ## Boolean,         # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": False, ## Boolean,               # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": False, ## Boolean,               # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": 160, ## float,                       # agent's yaw in degrees
    "objects_distance": [], ## [float, ],           # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [], ## [float, ],            # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": True, ## [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [], ## [(float, float),],   # list of object locations [(x,y), ...].
    "objects_speed": 1, ## [float, ],               # list of the objects' speeds in meters per second.
    "progress": 0, ## float,                        # percentage of track completed
    "speed": 2, ## float,                           # agent's speed in meters per second (m/s)
    "steering_angle": 0, ## float,                  # agent's steering angle in degrees
    "steps": 2, ## int,                             # number steps completed
    "track_length": 0, ## float,                    # track length in meters.
    "track_width": 0.45, ## float,                  # width of the track
    "waypoints": waypoints
    }

def test_reward_old():
    ##import old.cw_utils as cw
    ##mport old.log_analysis as la
    ##stream_name = 'sim-sample' 
    ##fname = 'logs/deepracer-%s.log' %stream_name  # The log will be downloaded into the specified path

    ##data = la.load_data("logs/evaluation-20220612082853-IBZwYd0MRMqgwKlAe7bb0A-robomaker.log")
    ##print(">> data printed")
    ##df = la.convert_to_pandas(data, waypoints)
    ##df = df.sort_values(['episode', 'steps'])
    ##print(df)

    fname="/Users\peter/Downloads/reinventBaseTrack05-training_job_x3ix_xSRTwOTYWRih3GdOw_logs/59407f57-40fc-449f-9a73-1ad4981aa981/sim-trace/training/training-simtrace/4-iteration.csv"

    df = pd.read_csv(fname)
    ##df_to_array = np.array(df)

    params = get_test_params()
    for index, row in df.iterrows():
        for column in df.columns:
            params[column]=row[column]
        params["x"]=row["X"]
        params["y"]=row["Y"]
        ##print(params)
        reward = reward_function.reward_function(params)
        ##print("test_reward: {}".format(reward))
        assert reward > 0.0
        ##assert reward <= 1.0
        print("=====================================")

def test_reward():
    params = get_test_params()

    fname="/Users\peter/Downloads/reinventBaseTrack05-training_job_x3ix_xSRTwOTYWRih3GdOw_logs/59407f57-40fc-449f-9a73-1ad4981aa981/sim-trace/training/training-simtrace/4-iteration.csv"
    import csv
    with open(fname, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = next(reader)
        for row in reader:
            for column in headers:
                params[column]=row[column]
                print(f"params set {column} = {row[column]}")
            params["x"]=row["X"]
            params["y"]=row["Y"]
            ##print(params)
            reward = reward_function.reward_function(params)
            print("test_reward: {}".format(reward))
            assert reward > 0.0



def run_tests():
    test_reward_old()
    print("All tests successful")

run_tests()

