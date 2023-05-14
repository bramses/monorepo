import os
import dotenv

dotenv.load_dotenv()

GH_USERNAME = os.getenv("GH_USERNAME")
ROOT_DIR = os.getenv("ROOT_DIR")
SKIP_DIRS = os.getenv("SKIP_DIRS")


def find_readme_files(root_dir):
    readme_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'README.md' and dirpath not in SKIP_DIRS:
                readme_files.append(os.path.join(dirpath, filename))
    return readme_files

def generate_md_content(readme_files):
    md_content = []
    for readme_file in readme_files:
        dir_name = os.path.dirname(readme_file)
        title = os.path.basename(dir_name)
        path_in_monorepo = dir_name.replace(root_directory, "")
        summary = generate_summary(readme_file)  # Replace this with your own function or chat conversation
        relative_path = os.path.relpath(dir_name, root_directory)
        github_link = generate_github_link(relative_path)  # Replace this with your own function or chat conversation
        md_content.append(f"## {title}\n\nPath in Monorepo:\n```\n{path_in_monorepo}\n```\n\n{summary}\n\n{github_link}")
    return md_content

def generate_summary(readme_file):
    # surround contents of README.md with <details> and return
    summary = "<summary>Click to expand</summary>\n\n"
    with open(readme_file, "r") as f:
        content = f.read()
    return f"<details>{summary}\n\n{content}\n\n</details>"


def generate_github_link(dir_name):
    # Replace this with your own function or chat conversation to generate the GitHub link
    return f"[link](https://github.com/{GH_USERNAME}/{dir_name})"

# Main script
root_directory = ROOT_DIR
readme_files = find_readme_files(root_directory)
md_content = generate_md_content(readme_files)

# Write the content to an MD file
with open("readme_summary.md", "w") as md_file:
    md_file.write("\n\n".join(md_content))