import toml
import random

random_number = f"{random.randint(0,100)}{random.randint(0,100)}"
print(f"RandomNumber--->>{random_number}")

# Load the existing TOML file
with open('zappa_settings.toml', 'r') as f:
    settings = toml.load(f)

# Modify the values
settings['development']['s3_bucket'] = f'tc{random_number}'
settings['development']['aws_region'] = 'us-west-2'
settings['development']['project_name'] = f'tc-test{random_number}'
settings['development']['runtime'] = f'python3.10'

settings['development']['aws_environment_variables']['TC_DRIVER_PATH'] = 's3://ghrc-cog/tc.sqlite'

# Write the modified data back to the file
with open('zappa_settings.toml', 'w') as f:
    toml.dump(settings, f)


