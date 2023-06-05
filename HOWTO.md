## add a git subrepo

```bash
git submodule add gh-url
```

## update the README.md

```bash
cd scripts/readme_summarizer/ 
poetry shell
python summarize_readmes.py
```

copy readme_summary.md to README.md

## move something to archive

```bash
git mv <dir> _archive/
```