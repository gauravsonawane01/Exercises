"""
What is environment variable?
Set Environment variable
Print value stored in Environment variable

"""

import os

# printing environment variables
print(os.environ)
print("\n")

# setting environment variable
env_var = input('Please enter environment variable name:\n')

env_var_value = input('Please enter environment variable value:\n')

os.environ[env_var] = env_var_value

print(f'{env_var}={os.environ[env_var]} environment variable has been set.')