import re


def html2markdown(html):
    '''Take in html text as input and return markdown'''
    html = html.replace("<em>", "*")
    html = html.replace("</em>", "*")
    html = html.split()

    html = " ".join(html)
    html = html.replace("<p>", "")
    html = html.replace("</p>", "\n\n")
    return html.strip()

html = (
    'This is the <a href="https://pypi.org/project/html2markdown/">link</a> to the html2markdown package and '
    'here is <a href="https://github.com/dlon/html2markdown">another link</a> to the project homepage'
)
expected = (
    'This is the [link](https://pypi.org/project/html2markdown/) to the html2markdown package and '
    'here is [another link](https://github.com/dlon/html2markdown) to the project homepage'
)

print(html2markdown(html))
print(expected)
