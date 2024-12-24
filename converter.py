import yaml

class ConfigToYAML:
    @staticmethod
    def convert(data):
        """Преобразование данных в YAML."""
        return yaml.dump(data, sort_keys=False, allow_unicode=True)