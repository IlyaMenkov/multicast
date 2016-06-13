from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, oid, lm, connector
import forms
from models import User, ROLE_USER, ROLE_ADMIN, Post, Content
import config


@app.route('/')
@app.route('/index')
def index():
    posts = []
    multicast_list = Content.query.all()
    for i in multicast_list:
        posts.append({'page': '/cust/{}'.format(i.id),
                      'name': i.name,
                      'dt': i.dt})
    return render_template('base.html',
                           create=True,
                           title='Home',
                           posts=posts)



@app.route('/cust/<id>')
def translation(id):
    content = Content.query.get(id)
    if content:
#    content = Content.query.order_by('-id').first()
        return render_template('translation.html',
                               ip_address=content.ip_addr,
                               dt=content.dt)
    return redirect(url_for('index'))


@app.route('/create_translation', methods=['GET', 'POST'])
@login_required
def create():
    form = forms.CreateTranslation()
    if form.is_submitted():
        name = form.name._value()
        path = form.path._value()
        dt = form.dt._value()
        VoD = form.VoD._value()

        ip_address, count = connector.settings_telnet(path_to_file=form.path._value(),
                                                      dt=dt)
        post = Content(name=name,
                       path=path,
                       ip_addr=ip_address,
                       dt=dt)

        db.session.add(post)
        db.session.commit()
#        content = Content.query.order_by('-id').first()
        return redirect(url_for('index'))
    return render_template('create.html',
                            form=form)


@app.route('/delete_translation', methods=['GET', 'POST'])
@login_required
def delete():

    form = forms.DeleteTranslation()

    form.names.choices = [(g.id, g.name) for g in Content.query.order_by('name')]
    print(form.names.choices)

    if form.is_submitted():
        name = form.data
        print name
        post = Content.query.get(int(name['names']))
        print post
        Content.query.filter_by(id=int(name['names'])).delete()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html',
                            form=form)


@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated:
      return redirect(url_for('index'))
  form = forms.LoginForm()
  if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
  return render_template('login.html',
      title='Sign In',
      form=form,
      providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))