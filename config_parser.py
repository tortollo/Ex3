import re

class ConfigParser:
    @staticmethod
    def parse(content):
        """Парсинг входного текста в формате учебного конфигурационного языка."""
        result = {}
        lines = content.splitlines()
        multiline_comment = False

        for line in lines:
            line = line.strip()

            # Игнорирование пустых строк
            if not line:
                continue

            # Многострочные комментарии
            if line == "=begin":
                multiline_comment = True
                continue
            if line == "=end":
                multiline_comment = False
                continue
            if multiline_comment:
                continue

            # Однострочные комментарии
            if line.startswith(";"):
                continue

            # Парсинг массивов
            if line.startswith("[") and line.endswith("]"):
                key, values = ConfigParser._parse_array(line)
                result[key] = values
                continue

            # Парсинг констант
            if "=" in line:
                key, value = ConfigParser._parse_constant(line)
                result[key] = value
                continue

            raise ValueError(f"Неизвестная строка: {line}")

        return result

    @staticmethod
    def _parse_array(line):
        """Парсинг массивов."""
        key, values = re.match(r"\[(.*)\] = \[(.*)\]", line).groups()
        values = [v.strip() for v in values.split(",")]
        return key, values

    @staticmethod
    def _parse_constant(line):
        """Парсинг констант."""
        key, value = line.split("=", 1)
        return key.strip(), value.strip()