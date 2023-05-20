import requests
from subprocess import Popen
import os
import dotenv
import json

dotenv.load_dotenv()

ROOT_DIR = os.getenv("ROOT_DIR")

# read ROOT_DIR/relations.json

def read_relations():
    # read relations.json   
    with open(ROOT_DIR + "/relations.json", "r") as f:
        relations = json.load(f)
    return relations

def write_relations(relations):
    # write relations.json
    with open(ROOT_DIR + "/relations.json", "w") as f:
        json.dump(relations, f, indent=4)

    return relations


github_link = "https://github.com/bramses/gpt-to-chatgpt-ts"


def add_submodule(github_link):
    # check if github link is valid

    if not github_link:
        raise ValueError("No github link provided")

    # if repo does not exist, throw error

    if requests.get(github_link).status_code != 200:
        raise ValueError("Github link does not exist")

    # check if github link has a readme

    if not requests.get(github_link + "/blob/main/README.md").status_code == 200:
        raise ValueError("Github link does not have a readme")

    # add submodule to monorepo

    submodule_name = github_link.split("/")[-1]

    # read root directory for submodule and if it exists, throw error
    if os.path.isdir(ROOT_DIR + "/" + submodule_name):
        raise ValueError("Submodule already exists")

    # add submodule to monorepo -- run from root directory
    os.chdir(ROOT_DIR)

    p = Popen(["git", "submodule", "add", github_link])

    p.wait()


    # return name of github repo
    return github_link.split("/")[-1]



# create a new key in the relations dict
# add the new key to the relations dict

def add_key(relations, key):
    relations[key] = []

    return relations

# recreate the readme

def recreate_readme():
    Popen(["python", "../readme_summarizer/summarize_readmes.py"])

def main():
    github_link = input("Enter github link: ")
    submodule_name = add_submodule(github_link)
    relations = read_relations()
    relations = add_key(relations, submodule_name)
    write_relations(relations)
    recreate_readme()

if __name__ == "__main__":
    main()
