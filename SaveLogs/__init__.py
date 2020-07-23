from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
import json
from os import path

class SaveLogsHandler(IPythonHandler):
    def get(self):
        self.finish('Still running')

    def post(self):
        event = json.loads(self.request.body)

        filename = event['value']['filename'] + '_log.txt'
        
        # data = []
        # if (not path.exists(filename)):
        #     data = [event]
        # else:
        #     with open(filename, 'r') as fs:
        #         data = json.load(fs)
        #         data.append(event)
        #         fs.close()

        with open(filename, 'a+') as fs:
            fs.write(str(event))
            fs.close()

        self.finish('data recieved')


def load_jupyter_server_extension(nb_server_app): 
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/savelogs')
    web_app.add_handlers(host_pattern, [(route_pattern, SaveLogsHandler)])