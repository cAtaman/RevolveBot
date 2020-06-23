import sys
import requests


def main(name='user', screen_width=100):
    form_header = '\n{:=^' + str(screen_width) + '}\n'
    name = input(form_header.format('  Sign up  ') + 'Please input your name...  ')
    form = '{:>' + str(screen_width) + '}\n{:>' + str(screen_width) + '}'
    
    print(form_header.format('  Chat  '))
    message = input(name + '\n')
    while message:
        req = requests.request("POST", "http://127.0.0.1:3310/chat", data={'msg': message})
        print(form.format('RevolveBot', req.json()['reply'], req.json()['time']))
        message = input(name + '\n')


if __name__ == '__main__':
    args = sys.argv[1:3]
    if not args:
        print('Hint: you can specify the chat area width... Use: "python terminal_client.py <size: int>"')
    main()
    sys.exit()