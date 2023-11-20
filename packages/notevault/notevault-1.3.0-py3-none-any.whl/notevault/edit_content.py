import os
import subprocess
import tempfile
from typing import Dict

from notevault.create_schemas import Content


def edit_contents(
    contents: Dict[str, Content], interactive: bool
) -> Dict[str, Content]:
    edited_contents = {}

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_paths = {}

        # Create temporary files with the correct names in the temporary directory
        for key, content in contents.items():
            tmp_file_path = os.path.join(tmp_dir, f"{key}.md")
            with open(tmp_file_path, "w") as tmp_file:
                tmp_file.write(content)  # Write the content's text to the file
            tmp_paths[key] = tmp_file_path

        if interactive and tmp_paths:
            editor = os.environ.get("EDITOR", "vim")
            # Prepare command to open vim with vertical splits
            vim_command = [editor] + ["-O"] + list(tmp_paths.values())
            subprocess.call(vim_command)

        # Read the edited content back into the Content objects
        for key, path in tmp_paths.items():
            with open(path, "r") as file:
                edited_text = file.read()
            edited_contents[key] = Content(
                edited_text
            )  # Create a new Content object with the edited text

    return edited_contents


if __name__ == "__main__":
    # Example dictionary of contents
    sample_contents = {
        "content1": Content("Hello, this is content 1."),
        "content2": Content("This is another piece, content 2."),
    }

    # Call the edit_contents function
    interactive_mode = True  # Set this to False if you don't want to open the editor
    edited_contents = edit_contents(sample_contents, interactive_mode)

    # Print the edited contents (or handle them as needed)
    for key, content in edited_contents.items():
        print(f"Edited content for {key}: {content}")
