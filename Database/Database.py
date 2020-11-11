import pandas as pd
import numpy as np
import csv
import HelperFunctions

DataBase = pd.read_csv("Database/DataBase.csv")

SubjectsID = {
    1:["Maths_1","TC","ICIT","Physics","C"],
    2:["Maths_2","POM","DE","DS","DBMS"],
    3:["Maths_3","CA","FEDT","POA","C++"],
    4:["Maths_4","WT","Java","SE","CN"],
    51:["CG","Ecom","OS","BE"],
    52:["CG","Ecom","OS","ST"],
    53:["CG","Ecom","OS","PHP"],
    61:["DWH & DM","MC","Linux","BI"],
    62:["DWH & DM","MC","Linux","NS"],
    63:["DWH & DM","MC","Linux","NP"],
    64:["DWH & DM","MC","Linux","AI"],
    65:["DWH & DM","MC","Linux","Multimedia"]
}

ImageData = {}
ImageData[int(DataBase["DictId"][DataBase["Name"].str.contains("Hrithik")])] = HelperFunctions.img_to_encoding("Images/hrithik.jpeg",FRmodel)
ImageData[int(DataBase["DictId"][DataBase["Name"].str.contains("Arjun")])] = HelperFunctions.img_to_encoding("Images/arjun.jpg",FRmodel)