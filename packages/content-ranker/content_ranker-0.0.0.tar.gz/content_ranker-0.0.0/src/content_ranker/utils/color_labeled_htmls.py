"""
‫این ماژول یک مجموعه ی فایل html لیبل خورده توسط دسته بند آموزش داده شده را رنگ می زند.

"""
from __future__ import annotations
import os
import argparse
from glob import glob
from typing import Union, Dict, TextIO, Optional
from bs4 import BeautifulSoup, NavigableString


class ColorHtml():
    tags_to_stay = ["a", "abbr", "acronym", "address", "applet", "area", "article", "aside", "audio", "b",
                     "base",
                     "bdo", "big", "blockquote", "br",
                     "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "data",
                     "datalist", "dir", "dd", "del", "details", "dfn",
                     "dialog", "div", "dl", "DOCTYPE",
                     "dt", "em", "embed", "fieldset", "figure", "figcation", "font", "form", "footer", "frame",
                     "frameset", "h1", "h2", "h3", "h4", "h5",
                     "h6", "head", "header", "hgroup", "html", "hr", "i", "iframe", "img",
                     "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark",
                     "marquee",
                     "menu",
                     "menuitem", "meta", "meter", "nav", "object", "ol",
                     "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp",
                     "ruby", "rt", "s",
                     "samp", 'section', "select", "small",
                     "source", "span", "strike", "strong",
                     "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot",
                     "th", "thead",
                     "title", "time", "tr", "track",
                     "tt", "u", "ul", "use", "var", "video", "wbr"]

    color_list = [
        (255, 255, 255), # white
        (170, 204, 255), # light blue
        (153, 255, 153), # green
        (255, 255, 153), # yellow
        (255, 204, 153), # orange
        (255, 153, 255), # pink
    ]

    def parse(self, html_file: TextIO | str) -> "BeautifulSoup":
        soup = BeautifulSoup(html_file, "html.parser")
        return self.__call__(soup)

    def __call__(self, soup: "BeautifulSoup"):
        self.soup = soup
        labeled_tags_list = []
        for tag_name in self.tags_to_stay:
            labeled_tags_list.extend(self.soup.findAll(tag_name))
        for tag in labeled_tags_list:
            if tag.has_attr("__clf_label"):
                clf_label = int(tag['__clf_label'])
                style = f"background-color: rgb{self.color_list[clf_label]}; color: black;"  if clf_label > 0 else ""
                for child in tag.children:
                    if isinstance(child, NavigableString):
                        span = self.soup.new_tag('span')
                        child.wrap(span)
                        span["style"] = style
        return self.soup

    def clear(self):
        del self.soup

    def save(self, output_path: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.soup.prettify())

