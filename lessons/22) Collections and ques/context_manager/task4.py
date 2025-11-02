class ConfigManager:
    def __init__(self, config_object, new_value):
        self.config_object = config_object
        self.new_value = new_value
        self.initial_value = None

    def __enter__(self):
        self.initial_value = self.config_object.config_attr
        self.config_object.config_attr = self.new_value
        print(f'конфигурация временно изменена {self.config_object.config_attr}')
        return self.config_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.config_object.config_attr = self.initial_value
        print(f'конфигурация восстановлена {self.config_object.config_attr}')
        return  False

class AppConfig:
    def __init__(self, initial_config):
        self.config_attr = initial_config
app_config = AppConfig(initial_config='production mode')
print(f'before {app_config.config_attr}')
with ConfigManager(app_config, 'development mode') as temp:
    print(f'{temp.config_attr}')
print(f'after {app_config.config_attr}')

