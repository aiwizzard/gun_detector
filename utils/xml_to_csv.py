import os
import glob
import pandas as pd
import argparse
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for item in root.findall('object'):
            value = (root.find('filename').text,
                    int(root.find('size')[0].text),
                    int(root.find('size')[1].text),
                    item[0].text,
                    int(item[4][0].text),
                    int(item[4][1].text),
                    int(item[4][2].text),
                    int(item[4][3].text)            
                    )
            xml_list.append(value)
    columns = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=columns)
    return xml_df

    def main():
        current_directory =os.getcwd()
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        for directory in ['train', 'test']:
            image_path = os.path.join(parent_directory, f'images/{directory}')
            xml_df = xml_to_csv(image_path)
            xml_df.to_csv(f'annotations/{directory}_labels.csv', index=None)
            print("Successfully converted xml to csv")

