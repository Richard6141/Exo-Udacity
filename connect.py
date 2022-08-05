import psycopg2

conn = psycopg2.connect(
    host= "localhost",
    port= 5432,
    database =  "exemple",
    user = "postgres",
    password =  "postgres")
    

cursor = conn.cursor()

# Ouvrir un curseur pour effectuer des opérations sur la base de données
cur = conn.cursor()

# supprimer toute table todos existante
cur.execute("DROP TABLE IF EXISTS todos;")

#(re)créer la table todos
# (remarque : les guillemets triples permettent d’obtenir un texte multiligne en python)
cur.execute("""
CREATE TABLE todos (
id serial PRIMARY KEY,
description VARCHAR NOT NULL
);
""")

# commit, donc il effectue les opérations sur la base de données et persiste dans la base de données.
conn.commit()

cur.close()
conn.close()