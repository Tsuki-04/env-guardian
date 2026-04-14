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

errors = []
warnings = []
info = []

for result in results:
    if result.startswith("[ERROR]"):
        errors.append(result)
    elif result.startswith("[WARNING]"):
        warnings.append(result)
    elif result.startswith("[INFO]"):
        info.append(result)

if errors:
    print("\n=== ERRORS ===")
    for e in errors:
        print(e)

if warnings:
    print("\n=== WARNINGS ===")
    for w in warnings:
        print(w)

if info:
    print("\n=== INFO ===")
    for i in info:
        print(i)

print("\n=== SUMMARY ===")
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")
print(f"Info: {len(info)}")