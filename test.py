#task1 LRU Cache

from collections import OrderedDict
class LRUCache:
    def __init_ _(self, capacity: int = 128):

        self.capacity = capacity
        self.Cache = OrderedDict()
    def get(self , key):
        if key not in self.cache:
            return None

        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
         if key in self.cache:

             self.cache.move_to_end(key)
         self.cache[key] = value
         if len(self.cache) >
self.capacity:
            self.cache.popitem(last=False)


    def has (self, key):
         return key in self.cache



#task 2 SSML Parser

import xml.etree.ElementTree as ET

def parseSSML(ssml_string: str):
    try:
        root = ET.fromstring(ssml_string)
        return root

    except ET.ParseError:
         raise ValueError("Invalid SSML string")


#Task 3 convert ssml node tree

def ssmlNodeToText(node) -> str:
    text = node.text or " "

   for child in node:
        text += ssmlNodeToText(child)
        if child.tail:
            text += child.tail

   return text
git push origin main

