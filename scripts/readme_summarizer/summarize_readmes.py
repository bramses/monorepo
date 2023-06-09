import os
import dotenv
import json

dotenv.load_dotenv()

GH_USERNAME = os.getenv("GH_USERNAME")
ROOT_DIR = os.getenv("ROOT_DIR")
SKIP_DIRS_STR = os.getenv("SKIP_DIRS")
SKIP_DIRS = json.loads(SKIP_DIRS_STR)

INTRO_SECTION = """
# Monorepo README Summary

This is a summary of all the README.md files in the monorepo. It is generated by the script `scripts/readme_summarizer/summarize_readmes.py` and should be updated whenever a README.md file is added or updated.

## Table of Contents
"""

RELATIONSHIP_GRAPH = """
## Relationship Graph

This is a graph of the relationships between the README.md files in the monorepo. It is generated by the script `scripts/readme_summarizer/summarize_readmes.py` and should be updated whenever a README.md file is added or updated.
"""




def generate_relationship_graph(relations):
    '''
    given a dict of relations, generate a graph that can be displayed in the readme
    '''    
    graph = "```mermaid\ngraph LR\n"
    for key, values in relations.items():
        for value in values:
            graph += f"    {key} --> {value}\n"
        if len(values) == 0:
            graph += f"    {key}\n"
    graph += "```"
    return graph

def generate_toc(md_content):
    toc = []
    
    for block in md_content:
        line = block.split("\n")[0]

        if line.startswith("## "):
            toc.append(f"- [{line[3:]}](#{line[3:].lower().replace(' ', '-')})")
    
    return toc


def find_readme_files(root_dir):
    readme_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            
            contains = False
            for skip_dir in SKIP_DIRS:
                if skip_dir in dirpath:
                    print(f"Skipping {dirpath}")
                    contains = True
                    break

            if filename == 'README.md' and not contains and dirpath is not root_dir:
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
    # remove _archive from dir_name
    dir_name = dir_name.replace("_archive/", "")

    # if gh dir_name has /, then it is a subdirectory and we need to add a tree like the below url:
    if dir_name.count("/") >= 1:
        # add tree/main before only the first /
        dir_name = dir_name.replace("/", "/tree/main/", 1)


    # Replace this with your own function or chat conversation to generate the GitHub link
    return f"[link](https://github.com/{GH_USERNAME}/{dir_name})"

# Main script
root_directory = ROOT_DIR
readme_files = find_readme_files(root_directory)
md_content = generate_md_content(readme_files)

# Write the content to an MD file
with open("readme_summary.md", "w") as md_file:
    md_file.write(INTRO_SECTION)
    md_file.write("\n\n")
    md_file.write("\n\n".join(generate_toc(md_content)))
    md_file.write("\n\n")
    md_file.write(RELATIONSHIP_GRAPH)
    md_file.write("\n\n")
    

    # read in the relations.json from the root directory

    with open(os.path.join(root_directory, "relations.json"), "r") as f:
        relations = json.load(f)

    md_file.write(generate_relationship_graph(relations=relations))
    md_file.write("\n\n")
    md_file.write("\n\n".join(md_content))
