import json


def export_to_txt(file_path, errors, warnings, info):
    with open(file_path, "w", encoding="utf-8") as file:
        if errors:
            file.write("=== ERRORS ===\n")
            for error in errors:
                file.write(f"{error}\n")
            file.write("\n")

        if warnings:
            file.write("=== WARNINGS ===\n")
            for warning in warnings:
                file.write(f"{warning}\n")
            file.write("\n")

        if info:
            file.write("=== INFO ===\n")
            for item in info:
                file.write(f"{item}\n")
            file.write("\n")

        file.write("=== SUMMARY ===\n")
        file.write(f"Errors: {len(errors)}\n")
        file.write(f"Warnings: {len(warnings)}\n")
        file.write(f"Info: {len(info)}\n")


def export_to_json(file_path, errors, warnings, info):
    data = {
        "errors": errors,
        "warnings": warnings,
        "info": info,
        "summary": {
            "errors": len(errors),
            "warnings": len(warnings),
            "info": len(info)
        }
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def export_results(file_path, errors, warnings, info):
    if file_path.endswith(".txt"):
        export_to_txt(file_path, errors, warnings, info)
    elif file_path.endswith(".json"):
        export_to_json(file_path, errors, warnings, info)
    else:
        raise ValueError("Unsupported output format. Use .txt or .json")