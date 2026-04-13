from src.analyzer import parse_env_file
from rules.security import (
    check_app_debug,
    check_app_key,
    check_db_password,
    check_sensitive_variables,
)
from rules.structure import compare_env_files

env_vars = parse_env_file(".env")
example_vars = parse_env_file(".env.example")

results = []
results.extend(check_app_debug(env_vars))
results.extend(check_app_key(env_vars))
results.extend(check_db_password(env_vars))
results.extend(check_sensitive_variables(env_vars))
results.extend(compare_env_files(env_vars, example_vars))

for result in results:
    print(result)