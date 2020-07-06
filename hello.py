#to activate virtual environment
#venv\Scripts\activate
#to import images
#https://stackabuse.com/serving-static-files-with-flask/
#https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
#deactivate  - to stop virtual environment


from flask import Flask, render_template
from covidStats import totdata,statedata
from newsbot import Scraper

app = Flask(__name__)

#for testing
posts = [
{
    'author':'hari',
    'title':'hari',
    'dateposted':'1212121'
},
{
    'author':'sid',
    'title':'siddd',
    'dateposted':'126222'
}

]

#importing state data by scraping
state = totdata()

#importing news data by scraping
s = Scraper([
    'Coronavirus',
    'pandemic',
    'COVID-19',
    'infection',
    'Wuhan'
    ])

s.parse()

#for testing
@app.route("/test")
def test():
    return render_template("test.html",posts = posts)


@app.route("/")
@app.route("/index.html")
@app.route("/home")
def home():
    return render_template("index.html",news  =  s.saved_linksTexts)

#app.add_url_rule("index.html")

@app.route("/aboutus")
@app.route("/aboutus.html")
def salvador():
    return render_template("aboutus.html")

@app.route("/news")
@app.route("/news.html")
def news():
    return render_template("news.html")

@app.route("/table.html")
@app.route("/table")
def table():
    return render_template("table.html",states  =  state)



#app.add_url_rule('/hello', 'hello', hello_world)


if __name__ == "__main__":
    app.run(debug=True)
