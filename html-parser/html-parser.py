from typing import List, Optional, Dict
from dataclasses import dataclass, field

from json import dumps
from pprint import pprint

from html.parser import HTMLParser


@dataclass
class Node:
    tagName: Optional[str] = ""
    text: Optional[str] = ""
    children: List["Node"] = field(default_factory=lambda: [])
    attributeMap: Dict[str, str] = field(default_factory=lambda: {})
    parent: Optional["Node"] = None


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node()
        self.cursor = self.root

    def handle_starttag(self, tag, attrs):
        if not self.cursor.tagName:
            self.cursor.tagName = tag
            self.cursor.attributeMap = {key: value for key, value in attrs}
            return
        child = Node(tagName=tag, attributeMap={key: value for key, value in attrs})
        child.parent = self.cursor
        self.cursor.children.append(child)
        if tag == "meta":
            return
        self.cursor = child

    def handle_data(self, data):
        if data:
            self.cursor.text = data.strip()

    def handle_endtag(self, tag):
        parent = self.cursor.parent
        self.cursor = parent

    def display(self):
        pprint(self.root)


# Watch it working
with open("./sample.html", "r") as file:
    html = "".join(file.readlines())
    parser = MyHTMLParser()
    parser.feed(html)
    parser.display()
