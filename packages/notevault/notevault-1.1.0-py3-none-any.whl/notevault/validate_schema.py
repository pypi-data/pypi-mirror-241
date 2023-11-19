import yaml


def validate_schema(yaml_file: str) -> str:
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)

    # Rule 1: Models must match Section definitions
    models = data["Model"]
    sections = data["DocumentStructure"]["Sections"]
    for section in sections:
        section_type = section["section"]["type"]
        if section_type not in models:
            raise ValueError(f"Model '{section_type}' not defined for section.")

    # Rule 2: Sections marked with "is_list" must specify "list_specifier"
    for section in sections:
        if section["section"].get("is_list", False):
            if "list_specifier" not in section["section"]:
                raise ValueError(
                    f"'list_specifier' not defined for list section '{section['section']['heading']}'."
                )

    # Rule 3: If "list_specifier" is "heading", "heading_field" must be defined
    for section in sections:
        if section["section"].get("list_specifier") == "heading":
            if "heading_field" not in section["section"]:
                raise ValueError(
                    f"'heading_field' not defined for section '{section['section']['heading']}' with 'list_specifier' as 'heading'."
                )
            heading_field = section["section"]["heading_field"]
            section_model = models[section["section"]["type"]]
            if heading_field not in section_model:
                raise ValueError(
                    f"'heading_field' '{heading_field}' not found in model '{section['section']['type']}'."
                )

    return "Schema validation passed."


if __name__ == "__main__":
    # Replace 'your_schema.yaml' with the path to your YAML file
    print(
        validate_schema(
            "/Users/Q187392/dev/s/private/py-notevault/tests/resources/schema.yaml"
        )
    )
