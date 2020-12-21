import psycopg2
from img_pars import ImgPars


con = psycopg2.connect('dbname=diploma_project user=postgres host=localhost')

cur = con.cursor()



cur.execute('SELECT * FROM country')
result = cur.fetchall();
country_id = {item[0]: item[1] for item in result}
cities = []
for key, value in country_id.items():
    parser = ImgPars(f'{value}')
    for link in parser.get_cities():
        cities.append(link.split('/')[-2].capitalize())
        cur.execute(f"""
        INSERT INTO city(name, slug, country_id)
        VALUES ('{''.join(cities)}', '{''.join(cities)}', '{key}');        
        """)
        con.commit()
        cities.clear()
cur.execute('SELECT * FROM city')
result = cur.fetchall();
for item in result:
    country = country_id.get(int(f'{item[-1]}'))
    parser = ImgPars(f'{country}')
    photo_links = parser.prep_img_to_db(f'{item[1]}')
    cur.execute(f"""
    INSERT INTO gallary(name, photo, photo_2, photo_3, photo_4, photo_5, photo_6, photo_7, photo_8, photo_9, photo_10, city_id, country_id)
    VALUES ('{item[1]}', '{photo_links[0]}', '{photo_links[1]}', '{photo_links[2]}', '{photo_links[3]}', '{photo_links[4]}', '{photo_links[5]}', '{photo_links[6]}', '{photo_links[7]}', '{photo_links[8]}', '{photo_links[9]}', '{item[0]}', '{item[-1]}')
    """)
    con.commit()

cur.close()
con.close()



