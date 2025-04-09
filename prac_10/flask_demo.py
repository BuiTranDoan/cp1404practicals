from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")


@app.route('/results')
def results():
    search_term = session.get('search_term', '')
    page = get_page(search_term)
    return render_template("result.html", page=page)


def get_page(search_term):
    try:
        page = wikipedia.page(search_term, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            title = e.options[0]
            page = wikipedia.page(title, auto_suggest=False)
        except Exception:
            page = None
    except wikipedia.exceptions.PageError:
        page = None
    except Exception:
        page = None
    return page


if __name__ == '__main__':
    app.run(debug=True)