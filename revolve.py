from datetime import datetime
from flask import request, jsonify, render_template
from config import revolve_bot, app
from termcolor import colored
import platform


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    message = request.form['msg']
    message = message if message else 'Hi'
    resp = revolve_bot.get_response(message)
    print('user_x: ', message)
    print(colored('RevolveBot: ' + resp.text, 'green'))
    return jsonify({'reply': resp.text, 'time': datetime.timestamp(resp.created_at)}), 200


@app.route('/revolvebot', methods=['GET'])
def get_bot_playground():
    return render_template('playground.html')


if __name__ == '__main__':
    if platform.uname().system == 'Windows':
        from colorama import init
        init()
    app.run(debug=True, port=3310)

