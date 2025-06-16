import re
import os

# Directory containing markdown files
MD_DIR = os.path.dirname(__file__)

# HTML tags to remove completely
REMOVE_TAGS = ['html', 'head', 'div', 'span', 'font']

# Regex patterns
STYLE_RE = re.compile(r'<style.*?</style>', re.S)
SCRIPT_RE = re.compile(r'<script.*?</script>', re.S)
BR_RE = re.compile(r'<br\s*/?>', re.I)
HEADER_RE = re.compile(r'<p class="header_box"[^>]*>(.*?)</p>', re.S)
SUBHEADER_RE = re.compile(r'<p class="blowheader_box"[^>]*>(.*?)</p>', re.S)
P_RE = re.compile(r'<p[^>]*>(.*?)</p>', re.S)
TAG_RE = re.compile(r'</?({})[^>]*>'.format('|'.join(REMOVE_TAGS)), re.S)
A_RE = re.compile(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)

# Keep img tags as is
IMG_RE = re.compile(r'<img[^>]*>')


def clean_html(content: str) -> str:
    # remove style and script sections
    content = STYLE_RE.sub('', content)
    content = SCRIPT_RE.sub('', content)
    # replace br with newline
    content = BR_RE.sub('\n', content)
    # convert headers
    content = HEADER_RE.sub(lambda m: '\n## ' + m.group(1).strip() + '\n', content)
    content = SUBHEADER_RE.sub(lambda m: '\n### ' + m.group(1).strip() + '\n', content)
    # convert links
    content = A_RE.sub(lambda m: f'[{m.group(2).strip()}]({m.group(1)})', content)
    # remove unwanted tags
    content = TAG_RE.sub('', content)
    # convert paragraphs to plain text
    content = P_RE.sub(lambda m: m.group(1).strip() + '\n', content)
    return content


def process_file(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    new_text = clean_html(text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)


def main():
    for name in os.listdir(MD_DIR):
        if name.endswith('.md') and name != 'README.md':
            process_file(os.path.join(MD_DIR, name))


if __name__ == '__main__':
    main()
