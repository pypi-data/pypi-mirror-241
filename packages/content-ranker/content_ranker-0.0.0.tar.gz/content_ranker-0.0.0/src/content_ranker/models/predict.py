import argparse
import json
import os
import sys


import torch

import numpy as np
from bs4 import BeautifulSoup, NavigableString
from collections import defaultdict
import re
from lxml import etree

from content_ranker.models.classifiers import LeafClassifier

TAGS_TO_IGNORE = {'head', 'iframe', 'script', 'meta', 'link', 'style', 'input', 'checkbox',
                  'button', 'noscript'}


class MainContentClassificationPredict():
    def __init__(self, model_address, tag_map_file, kwargs, device):
        self.device = device
        self.model = LeafClassifier(**kwargs)
        self.model.load_state_dict(torch.load(model_address, map_location=torch.device(self.device)))
        self.model = self.model.to(self.device)
        self.model.eval()
        self.tag_map_file = tag_map_file
        self.preprocess_html_files = PreprocessHtmlFiles(self.tag_map_file)
        self.tags_to_stay = ["a", "abbr", "acronym", "address", "applet", "area", "article", "aside", "audio", "b",
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

    def color_html(self, soup):
        labeled_tags_list = []
        for tag_name in self.tags_to_stay:
            labeled_tags_list.extend(soup.findAll(tag_name))
        for tag in labeled_tags_list:
            if tag.has_attr("__clf_label"):
                clf_label = int(tag['__clf_label'])
                if clf_label == 1:
                    style = "background-color: rgb(170, 204, 255); color: black;"
                elif clf_label == 2:
                    style = "background-color: rgb(153, 255, 153); color: black;"
                elif clf_label == 3:
                    style = "background-color: rgb(255, 255, 153); color: black;"
                elif clf_label == 4:
                    style = "background-color: rgb(255, 204, 153); color: black;"
                elif clf_label == 5:
                    style = "background-color: rgb(255, 153, 255); color: black;"
                else:
                    style = ""
                for child in tag.children:
                    if isinstance(child, NavigableString):
                        span = soup.new_tag('span')
                        child.wrap(span)
                        span["style"] = style
        return soup

    def predict(self, html_file):
        doc_features, doc_leafs, doc = self.preprocess_html_files.preprocess(html_file)
        features_tensor = torch.vstack([torch.from_numpy(array).float() for array in doc_features])
        features_tensor = torch.unsqueeze(features_tensor, 1)

        features_tensor = features_tensor.to(self.device)

        _, output = self.model(features_tensor)
        output = output[0]
        return output, doc_leafs, doc

    def make_labeled_html(self, html_file):
        output, doc_leafs, doc = self.predict(html_file)
        for i, leaf in enumerate(doc_leafs):
            leaf.set('__clf_label', str(output[i]))
        output_file_path = os.path.join(html_file)
        doc_str = etree.tostring(doc.getroot(), encoding="unicode", pretty_print=True, method='html')
        with open(output_file_path, 'w') as file:
            file.write(doc_str)

    def make_colored_html(self, html_file):
        self.make_labeled_html(html_file)
        with open(html_file, 'r') as fp:
            soup = BeautifulSoup(fp, "html.parser")
        soup = self.color_html(soup)
        with open(html_file, 'w', encoding='utf-8') as hfile:
            hfile.write(soup.prettify())


class PreprocessHtmlFiles():
    def __init__(self, tag_map_file):
        with open(tag_map_file, 'r') as f:
            self.tag_map = json.load(f)
        self.leafs = []
        self.parser = etree.HTMLParser(encoding="utf-8")

    def get_leaves(self, tree):
        list_of_texties = []
        for e in tree.iter():
            flag = 0
            if isinstance(e.tag, str):
                all_texts_set = set(e.itertext())
                set_child = set()
                for child in e.iterchildren():
                    try:
                        set_child = set_child.union(set(child.itertext()))
                    except ValueError:
                        continue
                text_of_tag = all_texts_set - set_child
                if len(text_of_tag) == 0:
                    continue
                else:
                    for text_part in text_of_tag:
                        if len(text_part.strip()) != 0:
                            flag = 1
                            break

            if flag == 1:
                u = tree.getpath(e)
                string1 = re.sub("[\[].*?[\]]", "", u)
                list_of_feature = (string1.split("/"))[1:]
                if len(TAGS_TO_IGNORE & set(list_of_feature)) == 0:
                    list_of_texties.append((e, list_of_feature))

        return list_of_texties

    def get_leaf_representation(self, tag_list):
        """Return dicts of words and HTML tags that representat a leaf."""
        tags_dict = defaultdict(int)
        for tag in tag_list:
            tags_dict[tag] += 1

        return dict(tags_dict)

    def process(self, doc):
        """
        Process "doc", updating the tag and word counts.
        Return the document representation, the HTML tags and the words.
        """
        leafs = []
        result = []
        for leaf, tag_list in self.get_leaves(doc):
            leaf_representation = self.get_leaf_representation(tag_list)
            result.append(leaf_representation)
            leafs.append(leaf)
        return leafs, result

    def parse(self, html_file):
        """
        Read and parse all HTML files.
        Return the parsed documents and a set of all words and HTML tags.
        """
        with open(html_file, "r") as file:
            doc = etree.parse(file, self.parser)
        doc_leafs, doc_result = self.process(doc)
        return doc_result, doc_leafs, doc

    def get_feature_vector(self, tags_dict):
        """Return a feature vector for an item."""
        tags_vec = np.zeros(len(self.tag_map), dtype='int32')
        for tag, num in tags_dict.items():
            # if the tag is not in the map, use 0 (OOV tag)
            tags_vec[self.tag_map.get(tag, 0)] = num

        return tags_vec

    def get_doc_inputs(self, doc_result):
        """Transform "docs" into the input format accepted by the classifier."""
        doc_features = []
        for tags_dict in doc_result:
            feature_vector = self.get_feature_vector(tags_dict)
            doc_features.append(feature_vector)
        return doc_features

    def preprocess(self, html_file):
        doc_result, doc_leafs, doc = self.parse(html_file)
        doc_features = self.get_doc_inputs(doc_result)
        return doc_features, doc_leafs, doc
