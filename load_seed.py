import json
from db import get_connection

#parse .json file
with open('NeetcodeSeed.json','r') as file:
    data = json.load(file)

con = get_connection()
cur = con.cursor()
con.close()