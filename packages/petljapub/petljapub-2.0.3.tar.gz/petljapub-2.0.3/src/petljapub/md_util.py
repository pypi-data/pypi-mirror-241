import sys, os, pathlib
import re
import yaml
from .util import read_file
from . import logger

# split initial Metadata in Yaml format from the rest of the file in
# Markdown format
def parse_front_matter(fname):
    # Taken from Jekyll
    # https://github.com/jekyll/jekyll/blob/3.5-stable/lib/jekyll/document.rb#L13
    YAML_FRONT_MATTER_REGEXP = r"\A---\s*\n(.*?)\n?^((---|\.\.\.)\s*$\n?)"

    file = read_file(fname)
    if file is None:
        logger.error("reading file:", fname)
        return "", {}

    match = re.search(YAML_FRONT_MATTER_REGEXP, file, re.DOTALL|re.MULTILINE)
    if not match:
        logger.error("parsing file:", fname)
        return "", {}
    
    try:
        header = yaml.safe_load(match.group(1))
        content = match.string[match.end():]
        return content, header
    except:
        logger.error("parsing file:", fname)
        return "", {}

# surround the given source code in a given programming language with
# appropriate markdown formating (~~~)
def md_source_code(code, lang, title=None):
    lang_id = {"cpp": "cpp", "cs": "cs", "py": "python"}.get(lang, lang) # defaults to lang if not "cpp", "cs", "py"
    result_md = title + "\n" if title else ""
    result_md += "~~~" + lang_id + "\n" + code + "~~~\n"
    return result_md

link_re = r"\[([^]\n]*)\]\(([-a-zA-Z_0-9./]*)\)"
image_re = r"!" + link_re

# find all links in a Markdown document (returns list of pairs
# containing link title and link path)

def link(title, path):
    return "[{}]({})".format(title, path)

def links_in_md(md):
    result = []
    for link in re.finditer("(?<![!])" + link_re, md):
        result.append((link.group(1), link.group(2)))
    return result

# replaces link with the given new content
def replace_link(md, old_title, old_path, new_content):
    old_link = link(old_title, old_path)
    return md.replace(old_link, new_content)

def change_link(md, old_title, old_path, new_title, new_path):
    new_link = link(new_title, new_path)
    return replace_link(md, old_title, old_path, new_link)

# find all images in a Markdown document (returns list of pairs
# containing image title and image path)
def images_in_md(md):
    result = []
    for image in re.finditer(image_re, md):
        result.append((image.group(1), image.group(2)))
    return result


def max_heading_level(md):
    max_level = 0
    for line in md.split('\n'):
        m = re.match(r"^(#+)\s+(.+)$", line)
        if m:
            max_level = max(max_level, len(m.group(1)))
    return max_level

def min_heading_level(md):
    min_level = sys.maxsize
    for line in md.split('\n'):
        m = re.match(r"^(#+)\s+(.+)$", line)
        if m:
            min_level = min(min_level, len(m.group(1)))
    return 0 if min_level == sys.maxsize else min_level

# build bold text
def bold(text):
    return "**{}**".format(text)

# build italic text
def italic(text):
    return "*{}*".format(text)

# build level k heading
def heading(title, level = 1, unnumbered=False, unlisted=False, anchor=""):
    result = "#" * level + " " + title
    extra = []
    if anchor:
        extra.append("#" + anchor)
    if unnumbered:
        extra.append(".unnumbered")
    if unlisted:
        extra.append(".unlisted")
    if extra != []:
        result += " {" + " ".join(extra) + "}"
    return result

# build list item
def list_item(text):
    return "  - {}\n".format(text)

# build an enumeration
def enumerate(items, compact=False):
    sep = "\n" if compact else "\n\n"
    return sep.join(map(lambda s: "  a) " + s, items))

heading_re = r"^(#+)\s+(.+)$"
def analyze_heading(text):
    m = re.match(heading_re, text)
    if m:
        level = len(m.group(1))
        title = m.group(2)
        return (title, level)
    else:
        return (None, None)

# degrade all headings so that # becomes # * level
def degrade_headings(md, level, unnumbered=False, unlisted=False):
    result = []
    for line in md.split('\n'):
        (title, current_level) = analyze_heading(line)
        if title:
            result.append(heading(title, current_level + level - 1, unnumbered=unnumbered, unlisted=unlisted))
        else:
            result.append(line)
    return "\n".join(result)

# remove headings and replace them by ordinary text (it might be normal, italic, or bold)
def remove_headings(md, level, replacement):
    heading_re = r"^" + "#"*level + r"\s+(\S+([ ]\S+)*)[ ]*$"
    return re.sub(heading_re, replacement + r"\1" + replacement, md, flags=re.MULTILINE)

# remove blank lines after given (heading) text, so that it fits into
# same line with the text that follows it (to save space)
def keep_with_next(text, heading):
    text = re.sub(r"^{}\s*(?![-])".format(re.escape(heading)), "{}: ".format(heading), text, flags=re.MULTILINE)
    # the exception are itemized enumerations behind inner headings
    text = re.sub(r"^{}[:]?\s*-".format(re.escape(heading)), "{}:\n\n  -".format(heading), text, flags=re.MULTILINE)
    return text
    

class PandocMarkdown:
    # fix latex $ signs in accordance with Pandoc Markdown dialect
    @staticmethod
    def fix_latex_dollars(md):
        # replace $$ by $ for inline maths
        md = re.sub(r"\$\$", "$", md)
        # put $$ around displayed maths
        # single displayed line
        md = re.sub(r"\n\n\s*\$(.+)\$([ \t]*{.+})?\s*(\n\n|\n\Z|\Z)", r"\n\n$$\1$$\2\n\n", md)
        # multiple displayed lines
        md = re.sub(r"\n\n\s*\$([^$]+)\$([ \t]*{.+})?\s*(\n\n|\n\Z|\Z)", r"\n\n$$\1$$\2\n\n", md)
        return md

    # fix indentation of itemized lists in accordance with Pandoc
    # Markdown dialect
    @staticmethod
    def fix_itemize(md):
        return re.sub(r"^-(?!(\d|\n|[-]))", "  -", md)

    # fix Markdown content in accordance with Pandoc Markdown dialect
    @staticmethod
    def fix(md):
        md = PandocMarkdown.fix_latex_dollars(md)
        md = PandocMarkdown.fix_itemize(md)
        return md

if __name__ == '__main__':
    pass
