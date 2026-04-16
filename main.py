import argparse
import sys

from src import messages
from src.analyzer import parse_env_file
from src.exporter import export_results
from src.formatter import group_results, render_console_output
from src.runner import run_analysis


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

try:
    env_vars = parse_env_file(args.env, required=True)
except FileNotFoundError:
    print(messages.required_env_file_not_found(args.env))
    sys.exit(1)

example_vars = parse_env_file(args.example, required=False)

results = []
if example_vars is None:
    results.append(messages.optional_reference_not_found(args.example))

results.extend(run_analysis(env_vars, example_vars, strict_mode=args.prod_check))

errors, warnings, info = group_results(results)

render_console_output(
    errors,
    warnings,
    info,
    env_path=args.env,
    example_path=args.example if example_vars is not None else None,
    strict_mode=args.prod_check
)

if args.output:
    export_results(args.output, errors, warnings, info)
    print(f"\n{messages.results_exported(args.output)}")