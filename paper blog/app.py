from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/paper'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(80), unique=True, nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    msg = db.Column(db.String(80), unique=True, nullable=False)


@app.route('/')
def home():
    post = Post.query.filter_by().all()
    return render_template('index.html',post = post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<string:Post_id>')
def post(Post_id):
    post = Post.query.filter_by(id=Post_id).one()
    return render_template('post.html',post=post)


@app.route('/contact',methods=['POST','GET'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('message')
        message = Message(name=name,email=email,msg=msg)
        db.session.add(message)
        db.session.commit()
    return render_template('contact.html')

@app.route('/add',methods=['GET','POST'])
def add():
    if(request.method=='POST'):
        title = request.form.get('title')
        slug = request.form.get('slug')
        content = request.form.get('content')
        post = Post(title=title,slug=slug,content=content)
        db.session.add(post)
        db.session.commit()
    return render_template('add.html')

app.run(debug=True)