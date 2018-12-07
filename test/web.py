import time
import logging, os
from flask import Flask

app = Flask(__name__)
c = 0
begin = time.time()
log = logging.getLogger(__file__)
log.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))
file_handler = logging.FileHandler('web.log')
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')

file_handler.setFormatter(formatter)
log.addHandler(file_handler)


@app.route('/')
def hello_world():
    global c, begin
    per = 3000
    if c % per == 0:
        end = time.time()

        log.debug('no:{};\tpid:{};\ttimes:{}s/{}req'.format(c, os.getpid(), end - begin, per))
        begin = end
    c += 1
    return 'Hello World!'
