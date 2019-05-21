from orak import app
from flask import render_template, flash, redirect, url_for, make_response, request, jsonify
from orak.forms import LoginForm, BulkUploadForm
from orak.login import login_call
from orak.bulkload import bulk_load
from orak.services import get_cached_values, load_cache


@app.route('/', methods=["POST", "GET"])
@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        access_token, env, success = login_call(username=form.username.data, password=form.password.data, env = form.environment.data)
        if success:
            flash('Logged in successfully', 'success')
            resp =  redirect(url_for('home'))
            resp.set_cookie('access-token',access_token) 
            resp.set_cookie('env', env)
            return resp
        else:
            flash(access_token, 'danger')
            render_template('login.html', form=form, title='Login')

    return render_template('login.html', form=form, title='Login')

@app.route('/home', methods=["POST", "GET"])
def home():
    access_token = request.cookies.get('access-token')
    env = request.cookies.get('env')
    if access_token and env:
        form = BulkUploadForm()
        if form.validate_on_submit():
            message, message_type = bulk_load(schema=form.schema.data, env=env, body=form.body.data, access_token=access_token) 
            if message and message_type:
                flash(message, message_type)
            else:
                flash('Unable to call endpoint!', 'danger')    
    
        return render_template('home.html', form=form, access_token = access_token, env=env)
    else:
        flash('Please login', 'danger')
        return redirect(url_for('login'))    


@app.route('/logout')
def logout():
    access_token = request.cookies.get('access-token')
    if (access_token):
        resp = redirect(url_for('login'))
        resp.set_cookie('access-token','',max_age=0)
        resp.set_cookie('env','',max_age=0)
        return resp

@app.route('/cache')
def cache():
    env = request.cookies.get('env')
    access_token = request.cookies.get('access-token')
    if access_token and env:
        return jsonify(result = get_cached_values(access_token = access_token, env = env))
    else:
        flash('Please login', 'danger')
        return redirect(url_for('login'))        

@app.route('/loadcache')
def loadcache():
    env = request.cookies.get('env')
    access_token = request.cookies.get('access-token')
    if access_token and env:
        return jsonify(result = load_cache(access_token = access_token, env = env))        
    else:
        flash('Please login', 'danger')
        return redirect(url_for('login'))    
