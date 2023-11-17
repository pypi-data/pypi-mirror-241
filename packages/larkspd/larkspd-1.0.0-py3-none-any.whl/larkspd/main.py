import requests
from abc import ABC, abstractmethod
from util import get_ip_address
from flask import Flask, request, jsonify


class LarkControllerBase(ABC):
    def __init__(self, port, pw):
        super().__init__()
        self.user_id = None
        self.aim_url = None
        self.pw = pw
        self.mission_name = None
        local_ip_addr = get_ip_address()
        if local_ip_addr is None:
            raise Exception("请在有公网IP的机器上运行！")
        self.local_ip_addr = local_ip_addr
        self.port = port
        self.ip_address = get_ip_address()
        self.app = Flask(__name__)

        @self.app.route('/', methods=['POST'])
        def route_message():
            data = request.get_json()
            print(data)
            status = data['status']
            if status == 'ping':
                return jsonify({'message': 'ok'})
            elif status == 'start':
                message = self.start()
                return jsonify({'message': message})
            elif status == 'stop':
                message = self.stop()
                return jsonify({'message': message})
            elif status == 'check':
                message = self.check()
                return jsonify({'message': message})

    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass

    @abstractmethod
    def check(self) -> str:
        pass

    def send_message(self, text):
        report_data = {
            'script': {
                'my_status': 'report',
                'message': {
                    'user_id': self.user_id,
                    'text': text,
                }
            },
            'pw': self.pw
        }
        requests.post(self.aim_url, json=report_data)

    def run_mission(self, mission_name: str, user_id: str, aim_url='http://www.sblsh.site:17777/'):
        self.mission_name = mission_name
        self.aim_url = aim_url
        self.user_id = user_id
        create_data = {
            'script': {
                'my_status': 'create_mission',
                'message': {
                    'user_id': user_id,
                    'name': mission_name,
                    'ip_addr': self.ip_address,
                    'port': self.port
                }
            },
            'pw': self.pw
        }
        requests.post(aim_url, json=create_data)
        self.app.run(host='0.0.0.0', port=self.port, debug=False)

