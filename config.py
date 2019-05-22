import os

DEBUG = True
SECRET_KEY = os.urandom(24)

MONGODB_SETTINGS = {
  'db': 'Price_System',
  'host': '127.0.0.1',
  'port': 27017
}
