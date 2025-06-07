#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    tree  = ET.parse(filename)
    root = tree.getroot()

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
        
    ET.ElementTree(root).write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for element in root:
        data[element.tag] = element.text
    return data