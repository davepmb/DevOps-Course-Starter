from flask import Flask, render_template, request, redirect, url_for
import session_items as session
import os
import requests
from todo_item import ToDoItem


app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    board_id = os.getenv('BOARD_ID')
    api_key = os.getenv('TRELLO_API_KEY')
    api_secret = os.getenv('TRELLO_API_TOKEN')
    response = requests.get(f'https://api.trello.com/1/boards/{board_id}/cards', params={'key': api_key, 'token': api_secret})
    
    trello_card_list = response.json()

    our_card_list = []
    for card in trello_card_list:
        status = "Not Started" if card["idList"] == os.environ["THINGS_TO_DO"] else "Completed"
        ouritem = ToDoItem(card["id"], status , card["name"])
        our_card_list.append (ouritem)


       
        
    return render_template('index.html', items = our_card_list)


@app.route('/additem', methods=['POST'])
def add_item():
    itemname = request.form.get('newitem')
    response = requests.post(
        "https://api.trello.com/1/cards",
        params={"key": os.environ["TRELLO_API_KEY"], "token": os.environ["TRELLO_API_TOKEN"], "name": itemname, "idList": os.environ["THINGS_TO_DO"]}
    )
    return redirect("/")

@app.route('/completeitem', methods=['POST'])
def completeitem():
    itemid = request.form.get('itemid')
    response = requests.put(
        f"https://api.trello.com/1/cards/{itemid}",
        params={"key": os.environ["TRELLO_API_KEY"], "token": os.environ["TRELLO_API_TOKEN"], "idList": os.environ["DONE"]}
    )
    return redirect("/")



if __name__ == '__main__':
    app.run()
