mode = "local"
train_low = True
train_high = True
train_low_with_penalty = True

n_parallel = 16 # 16
maze_id = 8 # 13

fence = False
n_itr = 1000 # number of iterations
death_reward = -10.0
sensor_range = 30.0
low_step_num = 5e4  # 6e5 for large maze, 5e4 for small maze
max_low_step = 1000 # num of low steps in one episode, 3000 for large maze

train_high_every = 1
discount_high = 0.99 # changeable
success_reward = 1000.
exp_prefix_set = 'tmp'

animate = False # False
time_step_agg_anneal = False
anneal_base_number = 1.023293 # 100 * 1.023293 ** -100 = 10

direct_goal = False # whether to include goal as (x,y) or as 20 rays
random_start = True
velocity_field = False # whether to use manually-set velocity field as
train_low_with_v_split = True # use HAAR
train_low_with_v_gradient = False # useless
baseline_name = 'linear'
low_level_entropy_penalty = 0.

train_low_with_external = False # train with external rewards only, no auxiliary reward
itr_delay = 0

transfer = False

pkl_path = "/h/andrewli/Documents/HAAR-A-Hierarchical-RL-Algorithm/data/local/Ant-snn/Ant-snn_10MI_5grid_6latCat_bil_0010/params.pkl"
