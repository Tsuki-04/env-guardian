def parse_env_file(file_path):
    env_vars = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Ignorar líneas vacías y comentarios
            if not line or line.startswith("#"):
                continue

            # Ignorar líneas que no tengan formato CLAVE=VALOR
            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            env_vars[key.strip()] = value.strip()

    return env_vars