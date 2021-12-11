from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route('/')
def hello_func():
    print('Hello World!')
    return redirect('/about')

@app.route('/about')
def about_func():
    name = 'Roy'
    uni= "BGU"
    return render_template('about.html', name='name', uni='uni')

if __name__ == '__main__':
    app.run()



@app.route('/home_page')
@app.route('/home')
@app.route('/')
def home_func():
    print('You are in our homepage')
    return redirect(url_for('about_func'))
