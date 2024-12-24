import argparse
from config_parser import ConfigParser
from converter import ConfigToYAML

def main():
    parser = argparse.ArgumentParser(description="Инструмент для преобразования учебного конфигурационного языка в YAML.")
    parser.add_argument("--input", required=True, help="Путь к входному файлу с конфигурацией.")
    args = parser.parse_args()

    input_file = args.input

    try:
        # Считывание и парсинг входного файла
        with open(input_file, "r") as file:
            content = file.read()
        parsed_data = ConfigParser.parse(content)

        # Преобразование в YAML
        yaml_output = ConfigToYAML.convert(parsed_data)

        # Вывод результата
        print(yaml_output)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()