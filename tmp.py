from os import path
import pickle
# load in level data
level = 1
world_data = []
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
    print("Hello World")
for i in world_data:
    for j in i:
        print(j, end=' ')
    print()
