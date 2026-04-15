import argparse

from src.analyzer import parse_env_file
from src.exporter import export_results
from rules.security import (
    check_app_debug,
    check_app_key,
    check_db_password,
    check_sensitive_variables,
)
from rules.structure import compare_env_files


parser = argparse.ArgumentParser(
    description="Env Guardian - Analyze .env files and detect insecure configurations"
)

parser.add_argument(
    "--env",
    default=".env",
    help="Path to the .env file to analyze"
)

parser.add_argument(
    "--example",
    default=".env.example",
    help="Path to the .env.example file to compare against"
)

parser.add_argument(
    "--output",
    help="Path to export the results (.txt or .json)"
)

parser.add_argument(
    "--prod-check",
    action="store_true",
    help="Enable stricter checks for production-like environments"
)

args = parser.parse_args()


env_vars = parse_env_file(args.env)
example_vars = parse_env_file(args.example)

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

if args.output:
    export_results(args.output, errors, warnings, info)
    print(f"\n[INFO] Results exported to {args.output}")