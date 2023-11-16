import unittest
from src.petljapub.md_util import *

class TestMDUtil(unittest.TestCase):

    def test_parse_front_matter(self):
        content, header = parse_front_matter('tests/data/01 Formule/01 geometrija/01 trening/trening-st.md')
        self.assertEqual(content[0:9], "Спортиста")
        self.assertEqual(header['title'], "Тренинг")
        
    def test_md_source_code(self):
        self.assertEqual(md_source_code("#include <iostream>", "cpp"), "~~~cpp\n#include <iostream>~~~\n")
        self.assertEqual(md_source_code("using System;", "cs"), "~~~cs\nusing System;~~~\n")
        self.assertEqual(md_source_code("import math", "py"), "~~~python\nimport math~~~\n")
        self.assertEqual(md_source_code("#include <stdio.h>", "c"), "~~~c\n#include <stdio.h>~~~\n")

    def test_link(self):
        self.assertEqual(link("Наслов", "putanja"), "[Наслов](putanja)")

    def links_md(self):
        return """# Наслов
Ovde je [линк](link) на средини реда.
[Линк](link) на почетку реда.
На крају реда је [линк](link)
Линк [који има више речи](putanja).
Линк [садржи "наводнике"](putanja).
Линк [садржи (заграде)](putanja).
Линк [наслов](/slozena/putanja).
Покушај [линка у
више редова](putanja).
Ово је ![слика](slika).
Ево је још једна ![слика са (мало) дужим описом](/slozena/putanja/slika.jpg).
"""

    def test_links_in_md(self):
        links = links_in_md(self.links_md())
        self.assertEqual(len(links), 7)
        self.assertEqual(links[0], ("линк", "link"))
        self.assertEqual(links[1], ("Линк", "link"))
        self.assertEqual(links[2], ("линк", "link"))
        self.assertEqual(links[3], ("који има више речи", "putanja"))
        self.assertEqual(links[4], ("садржи \"наводнике\"", "putanja"))
        self.assertEqual(links[5], ("садржи (заграде)", "putanja"))
        self.assertEqual(links[6], ("наслов", "/slozena/putanja"))

    def test_images_in_md(self):
        images = images_in_md(self.links_md())
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0], ("слика", "slika"))
        self.assertEqual(images[1], ("слика са (мало) дужим описом", "/slozena/putanja/slika.jpg"))

    def test_change_link(self):
        md = "Ovde je [линк](link) на средини реда."
        self.assertEqual(change_link(md, "линк", "link", "веза", "veza"), "Ovde je [веза](veza) на средини реда.")

    def test_replace_link(self):
        md = "Ovde je [линк](link) на средини реда."
        self.assertEqual(replace_link(md, "линк", "link", "*веза*"), "Ovde je *веза* на средини реда.")

    def test_format(self):
        self.assertEqual(bold("abc"), "**abc**")
        self.assertEqual(italic("abc"), "*abc*")
        
    def test_heading(self):
        self.assertEqual(heading("Наслов", 2), "## Наслов")
        self.assertEqual(heading("Наслов", 2, unnumbered=True, unlisted=True), "## Наслов {.unnumbered .unlisted}")
        self.assertEqual(heading("Наслов", 2, anchor="here"), "## Наслов {#here}")
        self.assertEqual(heading("Наслов", 2, unnumbered=True, anchor="here"), "## Наслов {#here .unnumbered}")

    def test_analyze_heading(self):
        (title, level) = analyze_heading("## Наслов")
        self.assertEqual(title, "Наслов")
        self.assertEqual(level, 2)
        (title, level) = analyze_heading("Наслов")
        self.assertIsNone(title)
        self.assertIsNone(level)

    def test_heading_levels(self):
        md = """# Ово је главни наслов
## ово је поднаслов
# Ово је опет главни наслов
## ово је поднаслов
### ово је подподнаслов
## ово је поднаслов
# Још један главни наслов"""
        self.assertEqual(min_heading_level(md), 1)
        self.assertEqual(max_heading_level(md), 3)

        mdd = """### Ово је главни наслов
#### ово је поднаслов
### Ово је опет главни наслов
#### ово је поднаслов
##### ово је подподнаслов
#### ово је поднаслов
### Још један главни наслов"""        

        self.assertEqual(degrade_headings(md, 3), mdd)

    def test_remove_headings(self):
        self.assertEqual(remove_headings("## Ово је наслов", 2, "*"), "*Ово је наслов*")
        self.assertEqual(remove_headings("## Ово је наслов\nЗдраво\n# Главни наслов\n## Joш један наслов\nЗдраво", 2, "**"),
                         "**Ово је наслов**\nЗдраво\n# Главни наслов\n**Joш један наслов**\nЗдраво")

    def test_keep_with_next(self):
        md = """*Задатак*

Ово је текст."""

        self.assertEqual(keep_with_next(md, "*Задатак*"), "*Задатак*: Ово је текст.")

        md = """*Задатак*

  - Ово је текст."""

        self.assertEqual(keep_with_next(md, "*Задатак*"), "*Задатак*:\n\n  - Ово је текст.")
        

    def test_pandoc_dollars(self):
        md = """Dvostruki dolari $$x^2$$.
Jednostruki dolari $x^2$.

$$x^2$$

i

$x^2 + 
3x - 2$

i

$x^2 + 3y$ {#eq:xy}

i

$
x_3 + 4
$   {#eq:x34}

$x_5$
"""
        md_fixed = """Dvostruki dolari $x^2$.
Jednostruki dolari $x^2$.

$$x^2$$

i

$$x^2 + 
3x - 2$$

i

$$x^2 + 3y$$ {#eq:xy}

i

$$
x_3 + 4
$$   {#eq:x34}

$$x_5$$

"""
        self.assertEqual(PandocMarkdown.fix_latex_dollars(md), md_fixed)
        
