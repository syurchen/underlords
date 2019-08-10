class Config(object):
    BACKGROUND_COLORS = ('#25222d', '#312c40')
    STAR_COLORS = ('#bbb2a9', '#b4c4e6', '#f3ef00')
    STAR_COLORS_RGB = ((167, 168, 162), (180, 196, 230), (243, 250, 45))
    #_starColorsRgb = ((37, 36, 41), (180, 196, 230), (52, 44, 59))
    
    STATIC_FOLDER = 'static/'
    UPLOAD_FOLDER = STATIC_FOLDER + 'uploads/'
    TMP_FOLDER = 'temp/'
    HERO_ICON_FOLDER = 'img/hero-icons/'
    LEVEL_ICON_FOLDER = 'img/scoreboard-icons/levels/'

    ENABLE_CACHE = False
    CACHE_FILE = TMP_FOLDER + 'cache'

    JSON_HEROES_FILE = STATIC_FOLDER + 'js/units.json'

    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'underlords'

    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
