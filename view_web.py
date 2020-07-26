from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{ 
           'author': 'Paulo Netto',
           'title': 'Blog post 1',
           'content': 'This is my post 1',
           'date_posted': 'June 24'

         },
        {  
           'author': 'Paulo Netto',
           'title': 'Blog post 1',
           'content': 'This is my post 1',
           'date_posted': 'June 24'
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home_page.html', posts=posts)

app.run(debug=True)
