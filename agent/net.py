# init net.py
import torch.nn as nn
import torch.nn.functional as F

"""
state: 
robot_me pos_x, pos_y, angle
robot_em pos_x, pos_y, angle

action:
robot1 v_x, v_y, ro, shoot
"""

class Net(nn.Module):
    def __init__(self, n_states, n_actions):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(n_states, 50)
        self.fc1.weight.data.normal_(0, 0.1)   # initialization
        self.out = nn.Linear(50, n_actions)
        self.out.weight.data.normal_(0, 0.1)   # initialization

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        actions_value = self.out(x)
        return actions_value
        #hi 我是廖鹏山
        #我也是廖鹏山