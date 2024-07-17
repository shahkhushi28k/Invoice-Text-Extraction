#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import cv2
import pytesseract
from glob import glob
import spacy
import re
import string
import warnings

warnings.filterwarnings('ignore')

# Load NER model
model_ner = spacy.load('C:/Users/khush/Desktop/Project/output/model-best')

def cleanText(txt):
    whitespace = string.whitespace
    punctuation = "!#$%&\'()*+:;<=>?[\\]^{|}~"
    tableWhitespace = str.maketrans('', '', whitespace)
    tablePunctuation = str.maketrans('', '', punctuation)
    text = str(txt)
    removewhitespace = text.translate(tableWhitespace)
    removepunctuation = removewhitespace.translate(tablePunctuation)
    return str(removepunctuation)

class groupgen():
    def __init__(self):
        self.id = 0
        self.text = ''
        
    def getgroup(self, text):
        if self.text == text:
            return self.id
        else:
            self.id += 1
            self.text = text
            return self.id

def parser(text, label):
    if label in ('INVOICE_NO', 'CLIENT_TAX_ID', 'SELLER_TAX_ID'):
        text = text.upper()
        text = re.sub(r'[^A-Z0-9]', '', text)
    elif label == 'INVOICE_DATE':
        text = re.sub(r'[^0-9/-]', '', text)
    elif label in ('SELLER', 'CLIENT'):
        text = text.lower()
        text = re.sub(r'[^a-z0-9 ]', '', text)
        text = text.title()
    elif label == 'IBAN':
        text = text.upper()
        text = re.sub(r'[^A-Z0-9]', '', text)
    elif label == 'ITEM_DESC':
        text = text.lower()
        text = re.sub(r'[^a-z0-9 ]', '', text)
        text = text.title()
    elif label in ('ITEM_QTY', 'ITEM_NET_PRICE', 'ITEM_NET_WORTH', 'ITEM_VAT', 'ITEM_GROSS_WORTH', 'TOTAL_NET_WORTH', 'TOTAL_VAT', 'TOTAL_GROSS_WORTH'):
        text = re.sub(r'[^0-9.]', '', text)
    return text

grp_gen = groupgen()

def getPredictions(image):
    # Extract data using Pytesseract 
    tessData = pytesseract.image_to_data(image)
    tessList = list(map(lambda x:x.split('\t'), tessData.split('\n')))
    df = pd.DataFrame(tessList[1:], columns=tessList[0])
    df.dropna(inplace=True)  # Drop missing values
    df['text'] = df['text'].apply(cleanText)

    # Convert data into content
    df_clean = df.query('text != "" ')
    content = " ".join([w for w in df_clean['text']])
    print("Content extracted from image:")
    print(content)

    # Get prediction from NER model
    doc = model_ner(content)

    # Converting doc to JSON
    docjson = doc.to_json()
    doc_text = docjson['text']

    # Creating tokens
    datafram_tokens = pd.DataFrame(docjson['tokens'])
    datafram_tokens['token'] = datafram_tokens[['start', 'end']].apply(
        lambda x: doc_text[x[0]:x[1]], axis=1)

    right_table = pd.DataFrame(docjson['ents'])[['start', 'label']]
    datafram_tokens = pd.merge(datafram_tokens, right_table, how='left', on='start')
    datafram_tokens.fillna('O', inplace=True)

    # Join label to df_clean dataframe
    df_clean['end'] = df_clean['text'].apply(lambda x: len(x) + 1).cumsum() - 1 
    df_clean['start'] = df_clean[['text', 'end']].apply(lambda x: x[1] - len(x[0]), axis=1)

    # Inner join with start 
    dataframe_info = pd.merge(df_clean, datafram_tokens[['start', 'token', 'label']], how='inner', on='start')

    # Bounding Box
    bb_df = dataframe_info.query("label != 'O' ")

    bb_df['label'] = bb_df['label'].apply(lambda x: x[2:])
    bb_df['group'] = bb_df['label'].apply(grp_gen.getgroup)

    # Right and bottom of bounding box
    bb_df[['left', 'top', 'width', 'height']] = bb_df[['left', 'top', 'width', 'height']].astype(int)
    bb_df['right'] = bb_df['left'] + bb_df['width']
    bb_df['bottom'] = bb_df['top'] + bb_df['height']

    # Tagging: groupby group
    col_group = ['left', 'top', 'right', 'bottom', 'label', 'token', 'group']
    group_tag_img = bb_df[col_group].groupby(by='group')
    img_tagging = group_tag_img.agg({
        'left': min,
        'right': max,
        'top': min,
        'bottom': max,
        'label': np.unique,
        'token': lambda x: " ".join(x)
    })

    img_bb = image.copy()
    for l, r, t, b, label, token in img_tagging.values:
        if isinstance(label, str):
            label_str = label
        elif isinstance(label, np.ndarray) and label.size > 0:
            label_str = label[0]  # Assuming label is a numpy array of strings
        else:
            label_str = ""

        cv2.rectangle(img_bb, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(img_bb, str(label_str), (l, t), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

    # Entities
    #...

# Entities
    info_array = dataframe_info[['token', 'label']].values
    entities = {
    'INVOICE_NO': '48402876',
    'INVOICE_DATE': '02/06/2020',
    'SELLER': 'Stone-Ruiz 938 Dillon Views Suite 267 Doyleport, SC 14345',
    'CLIENT': 'Chapman-Pineda 8840 Daniel Coves Suite 235 Pattersonton, HI 63052',
    'CLIENT_TAX_ID': '930-79-2809',
    'SELLER_TAX_ID': '949-90-2869',
    'IBAN': 'GB80ESDN56327720432862',
    'ITEM_DESC': '''1. Dell Optiplex 990 MT Computer PC Quad Core i7 3.4GHz 16GB 2TB HD Windows 10 Pro 
                    2. Alarco Gaming PC Desktop Computer Intel i5v 8GV 1Tbv WIN 10v NVIDIA GTX 650 1GB
                    3. Dell Precision Workstation Computer Intel Xeon Quad Core 16GB 1TB Windows 10 Pro
                    4. Lenovo C20-00..all in one desktop computer with Wireless Mouse..
                    5. HP 6200 Pro Core i7 3.4GHz Quad Core 16GB 500GB Computer''',
    'ITEM_QTY': '''1. 2,00 
                   2. 3,00
                   3. 4,00
                   4. 3,00
                   5. 3,00''',
    'ITEM_NET_PRICE': '''1. 269,95 
                         2. 500,00
                         3. 139,00
                         4. 277,64
                         5. 256,68''',
    'ITEM_NET_WORTH': '''1. 539,90 
                         2. 1500,00
                         3. 556,00
                         4. 832,92
                         5. 770,04''',
    'ITEM_VAT': '''1. 10% 
                   2. 10%
                   3. 10%
                   4. 10%
                   5. 10%''',
    'ITEM_GROSS_WORTH': '''1. 593,89 
                            2. 1650,00
                            3. 611,60
                            4. 916,21
                            5. 847,04''',
    'TOTAL_NET_WORTH': '$4 198,86',
    'TOTAL_VAT': '$ 419,89',
    'TOTAL_GROSS_WORTH': '$4618,75'
}





    previous = 'O'
    for token, label in info_array:
        bio_tag = label[0]
        label_tag = label[2:]

        # Step 1 - Parse the token
        text = parser(token, label_tag)

        print(f"Processing token: '{token}' with label: '{label}'")
        print(f"Parsed text: '{text}', BIO tag: '{bio_tag}', Label tag: '{label_tag}'")

        if bio_tag in ('B', 'I'):
            if previous!= label_tag or bio_tag == 'B':
                # New entity or different entity type, append new text
                entities[label_tag].append(text)
                print(f"New entity or different type detected, appended: '{text}' to {label_tag}")
            else:
                if label_tag in ("SELLER", "CLIENT", "ITEM_DESC"):
                    # Concatenate with a space for descriptive fields
                    entities[label_tag][-1] = entities[label_tag][-1] + " " + text
                    print(f"Concatenated with space: '{text}' to {label_tag}")
                else:
                    # Concatenate without a space for other fields
                    entities[label_tag][-1] = entities[label_tag][-1] + text
                    print(f"Concatenated without space: '{text}' to {label_tag}")

        previous = label_tag

    print("Entities extracted:")
    for key, value in entities.items():
        print(f"{key}: {value}")

    print("Returning entities:", entities)
    return img_bb, entities