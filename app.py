from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template('index.html')
    get_items()
    add_item(title)
    

if __name__ == '__main__':
    app.run()
