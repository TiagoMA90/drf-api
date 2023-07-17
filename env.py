import os

os.environ['DATABASE_URL'] = "postgres://xfoonmbu:8JwqKT7lL451J1EhyDMRH5BZEoYoehB5@trumpet.db.elephantsql.com/xfoonmbu"
os.environ['CLOUDINARY_URL'] = 'cloudinary://572555385744258:0COw3jIp0nWL_2Lzjn7KTeGgihM@dmbdqco85'
os.environ.setdefault("SECRET_KEY", "hadouken")
os.environ['DEV'] = '1'