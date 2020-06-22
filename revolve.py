from flask import request, jsonify, render_template
from config import revolve_bot, app


@app.route('/chat', methods=['GET'])
def chat():
    message = request.args['msg']
    resp = revolve_bot.get_response(message)
    return jsonify({'reply': resp.text, 'time': resp.created_at}), 200


@app.route('/revolvebot', methods=['GET'])
def get_bot_playground():
    return render_template('playground.html')


if __name__ == '__main__':
    app.run(debug=True, port=3310)

