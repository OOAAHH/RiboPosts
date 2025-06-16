# Bulk convert aptamer posts to plain Markdown

This repository contains aptamer posts with heavy HTML/CSS styling. `convert_to_plain_md.py` removes these styles and converts the posts to simpler Markdown.

## Usage
Run the script from the repository root:

```bash
python3 convert_to_plain_md.py
```

Each `.md` file (except `README.md`) will be processed in place. Images and Mol* viewer code remain untouched.
