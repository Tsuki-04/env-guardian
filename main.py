from src.analyzer import parse_env_file

env_vars = parse_env_file(".env.example")

for key, value in env_vars.items():
    print(f"{key} = {value}")