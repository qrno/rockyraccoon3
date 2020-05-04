import re

# Equivalence between rr-tag and html-tags
eq = { '#': 'h1',
       '##': 'h2',
       '###': 'h3',
       '####': 'h4',
       '#####': 'h5',
       '######': 'h6'
       }

regexes = { 'tag':      '^([^\s]+)',
            'tag+' :    '^([^\s]+[\s]?)'}

class Element():
    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    def simple_html(self):
        if self.tag == 'empty':
            return ""
        return "<{}>{}</{}>".format(self.tag, self.content, self.tag)

class Parser():
    def __init__(self, text):
        self.text = text

    def get_tag(self, line):
        fw = self.get_first_word(line)
        if fw is None:
            return 'empty'
        if fw in eq:
            return eq[fw]
        return "p"      # All lines that don't have tags are p's

    def get_content(self, line):
        line = line.rstrip()
        if self.get_tag(line) == 'p':
            return line
        else:
            without_tag = re.sub(regexes['tag+'], '', line)
            return without_tag

    def get_element(self, line):
        return Element(self.get_tag(line), self.get_content(line))

    def get_html(self):
        result=""
        for line in self.text:
            e = self.get_element(line)
            result += e.simple_html()
            if e.tag != 'empty':
                result += '\n'
        return result

    def get_first_word(self, line):
        m = re.match(regexes['tag'], line)
        if m is None:
            return None
        return m.group(1)
