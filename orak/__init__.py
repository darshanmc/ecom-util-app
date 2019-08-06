from flask import Flask
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = '2d52a01275db6cec821099e816ab0063'

with open('orak/resource/environment.json') as file:
    env_obj = json.loads(file.read())

environment = {}
environment['Local'] = env_obj['local']
environment['PJ'] = env_obj['pj']
environment['DEV'] = env_obj['dev']
environment['QA'] = env_obj['qa']
environment['PROD'] = env_obj['prod']

with open('orak/resource/url.json') as url_file:
    urls = json.loads(url_file.read())

login_service = {}
login_service['Local'] = env_obj['local'] + urls['login']
login_service['PJ'] = env_obj['pj'] + urls['login']
login_service['DEV'] = env_obj['dev'] + urls['login']
login_service['QA'] = env_obj['qa'] + urls['login']
login_service['PROD'] = env_obj['prod'] + urls['login']

bulk_service = {}

bulk_service['User'] = urls['user_url']
bulk_service['Organization'] = urls['organization_bulk']
bulk_service['FTB Order'] = urls['ftb_order_bulk']
bulk_service['FTB Order Report'] = urls['ftb_order_report_bulk']
bulk_service['Dealer Order Report'] = urls['dealer_order_report_bulk']
bulk_service['Dealer Order'] = urls['dealer_order_bulk']
bulk_service['Dealer'] = urls['dealer_bulk']

with open('orak/resource/b2benv.json') as b2benv_file:
    b2b_env_obj = json.loads(b2benv_file.read())

b2b_environment = {}
b2b_environment['Local'] = b2b_env_obj['local']
b2b_environment['PJ'] = b2b_env_obj['pj']
b2b_environment['QA'] = b2b_env_obj['qa']
b2b_environment['PROD'] = b2b_env_obj['prod']

with open('orak/resource/b2burl.json') as b2burl_file:
    b2b_urls = json.loads(b2burl_file.read())

from orak import route