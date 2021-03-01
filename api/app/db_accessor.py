import psycopg2
import os 

# db = os.getenv('DATABASE_URL')
db = "postgres://brygidiarisqgd:f04cbbb1d36166983d9bd8bbf1385626beb3459e25ab44f963f145d856580af4@ec2-35-174-118-71.compute-1.amazonaws.com:5432/d3sg2vuht28bkc"

def do_query(query, params):
  conn = psycopg2.connect(db, sslmode="require")
  cur = conn.cursor()

  if (params != None):
    cur.execute(query, params)
  else:
    cur.execute(query)

  return cur.fetchall()
  # conn.commit()
  # cur.close()
  # con
def do_insert(query, params):
  conn = psycopg2.connect(db, sslmode="require")
  cur = conn.cursor()

  cur.execute(query, params)

  conn.commit()