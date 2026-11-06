import json
from db import get_connection

#parse .json file
with open('NeetcodeSeed.json','r') as file:
    data = json.load(file)

con = get_connection()
cur = con.cursor()

#populate tables
#outer loop iterates on categories and problems in each category
for category_name, problems in data.items():
    cur.execute("INSERT OR IGNORE INTO categories (category) VALUES (?)", (category_name,))
    cur.execute("SELECT id FROM categories WHERE category = ?", (category_name,))

    row = cur.fetchone()
    c_id= row[0]

    #inner loop iterates on each problem and its columns
    for title, fields in problems.items():
        cur.execute("INSERT OR IGNORE INTO problems (id, title, difficulty, category_id, nurl, url) VALUES(?,?,?,?,?,?)", 
        (fields["id"], title, fields["difficulty"], c_id, fields["nurl"], fields["url"]))

con.commit()
con.close()