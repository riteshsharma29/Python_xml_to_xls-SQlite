#!/usr/bin/python
# coding: utf-8 -*-

import xml.etree.ElementTree as ET
import mpu
from xls2db import xls2db

myobj = mpu.XmlFile()

tree = ET.parse('mpu.xml')
root = tree.getroot()


'''count = 0
for child in root.iter('table'):
    count += 1
    if count == 1:  
        #print child.attrib.values()[0]
        #iterating through child nodes
        for row in child.findall('row'):
            for x in xrange(0,len(row)):
                print row[x].text,row[x].attrib.values()[0]'''


myobj.table_0([1,2],["Employee 1","Employee 2"])

for child in root.iter('table'):
#created empty list for each table column
    L0 = []
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    L7 = []
    L8 = []
    L9 = []
    L10 = []
    L11 = []
    L12 = []
    L13 = []
    L14 = []
    L15 = []
    L16 = []
    L17 = []
    L18 = []
    L19 = []
    if child.attrib.values()[0] == 'aggregateTable':
#Loop through each table data and append each column data into empty lists
        for row in child.findall('row'):
            L0.append(row[0].text)
            L1.append(row[1].text)
            L2.append(row[2].text)
        myobj.table_1(L0,L1,L2)             
    elif child.attrib.values()[0] == 'audioDescriptionTable':
        for row in child.findall('row'):
            L0.append(row[0].text)
            L1.append(row[1].text)
            L2.append(row[2].text)
            L3.append(row[3].text)
            L4.append(row[4].text)
            L5.append(row[5].text)
            L6.append(row[6].text)
            L7.append(row[7].text)
            L8.append(row[8].text)
            L9.append(row[9].text)
            L10.append(row[10].text)
        myobj.table_2(L0,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10)
    elif child.attrib.values()[0] == 'categoryConfigTable':
        for row in child.findall('row'):
            L0.append(row[0].text)
            L1.append(row[1].text)
            L2.append(row[2].text)
            L3.append(row[3].text)
            L4.append(row[4].text)
            L5.append(row[5].text)
            L6.append(row[6].text)
        myobj.table_3(L0,L1,L2,L3,L4,L5,L6)
    elif child.attrib.values()[0] == 'categoryInfoTable':
        for row in child.findall('row'):
            L0.append(row[0].text)
            L1.append(row[1].text)
            L2.append(row[2].text)
            L3.append(row[3].text)
            L4.append(row[4].text)
            L5.append(row[5].text)
            L6.append(row[6].text)
        myobj.table_4(L0,L1,L2,L3,L4,L5,L6)
    elif child.attrib.values()[0] == 'ccSubtitlesTable':
        for row in child.findall('row'):
            L0.append(row[0].text)
            L1.append(row[1].text)
            L2.append(row[2].text)
            L3.append(row[3].text)
            L4.append(row[4].text)
        myobj.table_5(L0,L1,L2,L3,L4)
    elif child.attrib.values()[0] == 'videoDescriptionTable':
        for row in child.findall('row'):
            L0.append(row[0].text)
            L1.append(row[1].text)
            L2.append(row[2].text)
            L3.append(row[3].text)
            L4.append(row[4].text)
            L5.append(row[5].text)
            L6.append(row[6].text)
            L7.append(row[7].text)
            L8.append(row[8].text)
        myobj.table_6(L0,L1,L2,L3,L4,L5,L6,L7,L8)



#Convert xml converted file into database

xls2db('tables.xlsx','outfile.db')









