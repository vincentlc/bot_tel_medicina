from pyngrok import conf, ngrok
import requests
from config import TOKEN
import time
#if we need debug log, we can uncomment this part
def log_event_callback(log):
    print(str(log))

conf.get_default().log_event_callback = log_event_callback


class Server:

    def __init__(self, *args, **kwargs):
        url = ngrok.connect(addr=8080, proto='http')
        self.ngrok_process = ngrok.get_ngrok_process()
        self.url = url.public_url.replace("http", "https")

        print('init')

    def start_server(self):
        try:
            self.ngrok_process.proc.wait()
        except KeyboardInterrupt:
            print(" Shutting down server.")

            ngrok.kill()

    def activate_webhook(self, token):
        url = "https://api.telegram.org/bot" + token + "/setWebHook?url=" + self.url + '/'
        print(url)
        x = requests.get(url)
        return x.status_code

    def loop_activate(self):
        for i in range(10):
            reply = self.activate_webhook(TOKEN)
            if reply != 200:
                print("retry")
                time.sleep(5)
            else:
                print("success")
                break


if __name__ == '__main__':
    while True:
        ngrok.kill()
        server = Server()
        server.loop_activate()
        server.start_server()
