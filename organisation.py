import sys
from flask import Flask, Blueprint

sys.path.insert(0,'/var/www/html/ORGANISATION/py')


from getOrgDetails import getOrgDetails_api
from getUserOrg import getUserOrg_api

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SESSION_COOKIE_SECURE'] = True

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RzT'

app.register_blueprint(getOrgDetails_api)
app.register_blueprint(getUserOrg_api)


if __name__ == "__main__":
    app.run()
