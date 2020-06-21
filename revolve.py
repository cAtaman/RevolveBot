import sys
from chatbot import revolve_bot


if __name__ == '__main__':
    try:
        chat = sys.argv[1:]
    except:
        print('Ask a question like so:  "python revolve Hi"')
        sys.exit()
        
    chat = ' '.join(chat)
    resp = revolve_bot.get_response(chat)
    print(resp)
    