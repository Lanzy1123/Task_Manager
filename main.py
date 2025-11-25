from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    completed=db.Column(db.Integer,default=0)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        user_task=request.form['content']
        new_task=Todo(content=user_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
             return 'There was an error while adding ur task'
    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_Td=Todo.query.get_or_404(id)
    try:
        db.session.delete(task_Td)
        db.session.commit()
        return redirect('/')
    except:
         return 'There was an error while deleting task'

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task=Todo.query.get_or_404(id)
    if request.method=='POST':
        task.content=request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
             return 'There was am error updating task'
    else:
        return render_template('update.html',task=task)
        
if __name__ == '__main__':
    app.run(debug=True)
    
    
 #zhumdal chemistry chapter 1