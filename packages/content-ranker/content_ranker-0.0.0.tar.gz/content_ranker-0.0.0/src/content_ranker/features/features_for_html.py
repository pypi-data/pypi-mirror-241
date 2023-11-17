"""
This module extracts features for an html page
"""
import json
from collections import deque

from selectolax.parser import HTMLParser

TAGS_TO_IGNORE = {'head', 'iframe', 'script', 'meta', 'link', 'style', 'input', 'checkbox',
                  'button', 'noscript'}


class FeatureForHtml:
    """
    A class for extracting features from an html page

    ...

    Attributes
    ----------
    logger: logging.Logger
        Object for logging
    tag_map_file:
        Tag map filename
    set_of_ignorance: set
        tags to ignore in the process
    Methods
    -------
    feature_calculator(self, plaintext_bytes, root_url):
    create_tag_queue(self, element):
    check_if_element_is_texty(self, element):
    get_leaves_and_features(self, tree):
    detect_arvan_cloud(tree):
    preprocess(self, plaintext_bytes, root_url):

    """

    def __init__(self, tag_map_file, logger):
        with open(tag_map_file, 'r') as f:
            self.tag_map = json.load(f)
        self.logger = logger
        self.set_of_ignorance = TAGS_TO_IGNORE

    def feature_calculator(self, plaintext_bytes, root_url):
        """
        Calculates features of html

            Parameters:
                 plaintext_bytes(bytes): bytes of the html page
                 root_url(str): url of the html page
            Returns:
                 doc_features_list(list or None): list of calculated features, None if no feature is calculated
        """
        doc_features_list = self.preprocess(plaintext_bytes, root_url)
        if doc_features_list is None or len(doc_features_list) == 0:
            return None
        return doc_features_list

    def create_tag_queue(self, element):
        """
        Calculates features of html

            Parameters:
                 element(selectolax.parser.Node): bytes of the html page

            Returns:
                 tags_queue(collections.deque): tags sequence
                 tag_current_availability(bool): True if the tag is not in the restricted list
        """
        tags_queue = deque()
        tag_current_availability = True
        pointer_to_tag = element
        while pointer_to_tag.tag != "html":
            tag_current = pointer_to_tag.tag
            if tag_current in self.set_of_ignorance:
                tag_current_availability = False
                break
            tags_queue.append(tag_current)
            pointer_to_tag = pointer_to_tag.parent
        return tags_queue, tag_current_availability

    def check_if_element_is_texty(self, element):
        """
        Checks if selectolax element is texty

            Parameters:
                 element(selectolax.parser.Node): element of the tree

            Returns:
                 status(bool): True if the element is texty
        """
        status = True
        text_of_tag = element.text(deep=False, separator=" ", strip=True).strip()
        if len(text_of_tag) == 0 or (element.tag in self.set_of_ignorance):
            status = False
        return status

    def _add_to_features_list_from_parent(self, element, result):
        """
        Calculates features of html

            Parameters:
                 element(selectolax.parser.Node): element of the tree of the html
                 result(list): list of features
            Returns:
                 status(bool): True if added to the features list, False if not
        """
        pointer_to_tag_parent_id = element.parent.attrs.get("__soroush_id")
        if pointer_to_tag_parent_id is not None:
            element.attrs["__soroush_id"] = len(result)
            parent_features = result[int(pointer_to_tag_parent_id)][:]
            parent_features[self.tag_map.get(element.tag, 0)] += 1
            result.append(parent_features)
            status = True
        else:
            status = False
        return status

    def process(self, tree):
        """
        Calculates features of html

            Parameters:
                 tree(selectolax.parser.HTMLParser): DOM tree of the html

            Returns:
                 result(list): list of features
        """

        result = []
        root = tree.root
        for e in root.traverse():
            status = self.check_if_element_is_texty(e)
            if not status:
                continue
            if e.tag != "html":
                status = self._add_to_features_list_from_parent(e, result)
                if status:
                    continue
            tags_queue, tag_current_availability = self.create_tag_queue(e)
            if not tag_current_availability:
                continue
            tags_queue.append("html")
            feature_row = self.get_leaf_representation_feature_creation(tags_queue)
            e.attrs["__soroush_id"] = len(result)
            result.append(feature_row)
        return result

    def get_leaf_representation_feature_creation(self, tag_deque):
        """
        Calculates features of html

            Parameters:
                 tag_deque(collections.deque): deque of the tag names

            Returns:
                 tags_vec(list): vector created from tag sequence
        """
        tags_vec = [0] * len(self.tag_map)
        while tag_deque:
            special_tag = tag_deque.pop()
            tags_vec[self.tag_map.get(special_tag, 0)] += 1
        return tags_vec

    @staticmethod
    def detect_arvan_cloud(tree):
        """
        Detects arvancloud pages, both Persian and English

            Parameters:
                 tree(selectolax.parser.HTMLParser): element of the tree
            Returns:
                 status(bool): True if it is actually arvancloud
        """
        error_element = tree.css_first("div.error-section__information")
        if error_element is not None:
            status = True
        else:
            status = False
        return status

    def preprocess(self, plaintext_bytes, root_url):
        """
        Parses html to create tree, then detects arvanclouds and then extracts features

            Parameters:
                 plaintext_bytes(bytes): bytes of the html page
                 root_url(str): url of the html page
            Returns:
                 result(list or None): list of calculated features, None if no feature is calculated
        """
        tree = HTMLParser(plaintext_bytes, detect_encoding=True)
        arvan_status = self.detect_arvan_cloud(tree)
        if arvan_status:
            self.logger.warning("arvancloud url detected: %s" % root_url)
        result = self.process(tree)
        return result
