# A=[1,2,3]

# a,b,=A[:2]

# print(a)
# print(b)

##################

import os

cwd=os.getcwd()
print(cwd)
new_dir_name='random'
new_path=os.path.join(cwd,new_dir_name)
# os.mkdir(new_path)
os.rmdir(new_path)