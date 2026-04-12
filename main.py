from src.analyzer import parse_env_file
from rules.security import check_app_debug

env_vars = parse_env_file(".env.example")

results = []
results.extend(check_app_debug(env_vars))

for result in results:
    print(result)