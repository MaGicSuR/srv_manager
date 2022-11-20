import json, os

example_config = {
    'test_server': {
        'IP': '1.1.1.1',
        'port': '22',
        'username': 'root',
        'password': 'password',
    },
    'test_server2': {
        'IP': '1.1.1.2',
        'port': '22',
        'username': 'root',
        'password': 'password',
    },
}

class Config():
    def __init__(self) -> None:
        print('Config initialization started.')
        self.config_file = 'servers.json'
        self.config_path = os.getcwd() + '\\' + self.config_file
        
        if os.path.exists(self.config_path) == False:
            self.create_example()
            print(f'Could not find {self.config_file}! New config has been created.')
        
    def create_example(self) -> bool:
        # Serializing json
        json_object = json.dumps(example_config, indent=4)
        with open(self.config_file, 'w') as file:
            file.write(json_object)
            return True

    def load_config(self) -> None:
        with open(self.config_file, 'r') as file:
            file.flush()
            json_buffer = json.load(file)
            file.close()
            return json_buffer

    def get_servers(self) -> list:
        file = self.load_config()
        servers = []
        servers.clear()
        servers.append(None)
        for i in file:
            servers.append(i)
        return servers

    def get_value(self, server: str, value: str):
        try:
            file = self.load_config()
            for i in file:
                if i == server:
                    return file[i][value]
        except Exception:
            pass