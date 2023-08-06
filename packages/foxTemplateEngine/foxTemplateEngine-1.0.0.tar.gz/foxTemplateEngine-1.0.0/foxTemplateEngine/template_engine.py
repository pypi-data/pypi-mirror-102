from sys import argv
import re
import os


tags: list = [
    'a', 'abbr', 'adress', 'area',
    'article', 'aside', 'audio', 'b',
    'base', 'bdi', 'bdo', 'blockquote',
    'body', 'br', 'button', 'canvas',
    'caption', 'cite', 'code', 'col',
    'colgroup', 'data', 'datalist', 'dd',
    'del', 'details', 'dfn', 'dialog',
    'div', 'dl', 'dt', 'em', 'embed',
    'fieldset', 'figcaption', 'figure',
    'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'head', 'header', 'hr', 'html', 'i',
    'iframe', 'img', 'input', 'title', 'html'
]

context: dict = {}


def html_render(line: str) -> str:
    tag: str = re.search(r'\w+', line)
    if tag:
        tag = tag.group(0)
        if tag in tags:
            if ('.' + tag) in line:
                line = line.replace('.' + tag, '</' + tag)
                if '\n' in line:
                    line = line.replace('\n', '>\n')
                else:
                    line += '>'
            else:
                line = line.replace(tag, '<' + tag).replace('\n', '>\n')
    
    while '{{' in line and '}}' in line:
        left = line.find('{{')
        right = line.find('}}')
        code = line[left + 3 : right]
        line = line.replace(line[left:right + 2], str(eval(code)))
    return line



def if_repeat(file, for_repeat: list, q: int):
    arr = []
    for line in file:
        if '% repeat ' in line:
            quantity = int(line[line.rfind(' %') - 1])
            if_repeat(file, arr, quantity)
            continue
        if '% end %' in line: 
            break
        arr.append(line)
    for i in range(q):
        for i in arr:
            for_repeat.append(i)
        

def transform(file_name: str, cntx: dict):

    global context
    context = cntx
    with open(file_name, 'r') as file, open(file_name + '_fox', 'w') as result_file:
        file_gen = (line for line in file)
        current_line = 0
        for line in file_gen:
            if '% repeat ' in line:
                quantity = int(line[line.rfind(' %') - 1])
                for_repeat = []
                if_repeat(file_gen, for_repeat, quantity)
                for i in for_repeat:
                    result_file.write(html_render(i))
                continue
            result_file.write(html_render(line)) 
