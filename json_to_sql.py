import sqlite3
import pandas as pd

business_df = pd.read_json('initial_business.json')
reviews_df = pd.read_json('initial_reviews.json')

conn = sqlite3.connect('yelp2.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS businesses (
    business_id TEXT PRIMARY KEY,
    name TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    latitude REAL,
    longitude REAL,
    stars REAL,
    review_count INTEGER,
    is_open INTEGER
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS categories (
    business_id TEXT,
    category TEXT
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    review_id TEXT PRIMARY KEY,
    user_id TEXT,
    business_id TEXT,
    stars REAL,
    useful INT,
    funny INT,
    cool INT,
    date DATETIME,
    FOREIGN KEY(business_id) REFERENCES businesses(business_id)
);
''')

category_data = business_df[['business_id','categories']]
exploded_df = category_data.explode('categories', ignore_index=True)

for index, business in business_df.iterrows():
    c.execute('''
    INSERT INTO businesses (business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (business['business_id'], business['name'], business['address'], business['city'], business['state'],
          business['postal_code'], business['latitude'], business['longitude'], business['stars'],
          business['review_count'], business['is_open']))
    
   
for index, category in exploded_df.iterrows():
    c.execute('''
        INSERT INTO categories (business_id, category)
        VALUES (?, ?)
        ''', (category['business_id'], category['categories']))

for index, review in reviews_df.iterrows():
    review_date = review['date'].strftime('%Y-%m-%d %H:%M:%S')
    
    c.execute('''
        INSERT INTO reviews (review_id, user_id, business_id, stars, useful, funny, cool, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (review['review_id'], review['user_id'], review['business_id'], review['stars'], review['useful'],
          review['funny'], review['cool'], review_date))
conn.commit()
conn.close()
