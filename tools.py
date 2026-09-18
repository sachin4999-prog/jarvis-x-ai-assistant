import os
import subprocess

# Keep this True while testing online.
# Change to False when running JARVIS-X on your own Windows PC.
DRY_RUN = True


def open_folder(folder_path):
    if DRY_RUN:
        return f"[TEST] I would open the folder: {folder_path}"

    if not os.path.exists(folder_path):
        return f"Folder not found: {folder_path}"

    os.startfile(folder_path)
    return f"Opened folder: {folder_path}"


def open_file(file_path):
    if DRY_RUN:
        return f"[TEST] I would open the file: {file_path}"

    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    os.startfile(file_path)
    return f"Opened file: {file_path}"


def search_files(folder_path, keyword):
    if not os.path.exists(folder_path):
        return f"Folder not found: {folder_path}"

    matches = []

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if keyword.lower() in filename.lower():
                matches.append(os.path.join(root, filename))

    if not matches:
        return f"No files found containing: {keyword}"

    return "\n".join(matches)


def prepare_workspace(project_folder):
    if DRY_RUN:
        return (
            "[TEST] Workspace preparation plan:\n"
            f"1. Open project folder: {project_folder}\n"
            "2. Open the required project files\n"
            "3. Prepare the workspace"
        )

    return open_folder(project_folder)
