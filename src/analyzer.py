import os


def parse_env_file(file_path, required=True):
    if not os.path.exists(file_path):
        if required:
            raise FileNotFoundError(f"Required file not found: {file_path}")
        return None

    env_vars = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            env_vars[key.strip()] = value.strip()

    return env_vars