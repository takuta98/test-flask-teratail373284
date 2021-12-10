from flask import Flask, render_template
import scraping

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scraping', methods=["GET"])
def do_scraping():
    result = scraping.scraping()
    return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
