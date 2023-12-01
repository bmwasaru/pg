import os

if os.environ.get('DATABASE_URL'):
    db_url = os.environ['DATABASE_URL']
else:
    db_url = "postgres://lugha_xyz:lugh2kr30jfdkfe3@localhost:5432/lugha_xyz"
