# Config Transpiler

## Описание
Инструмент командной строки для преобразования текста на учебном конфигурационном языке в формат YAML. Также выполняет проверку синтаксиса и сообщает об ошибках.

## Возможности
- Обработка однострочных (`;`) и многострочных (`=begin` ... `=end`) комментариев.
- Поддержка массивов.
- Объявление и вычисление констант.
- Конвертация в формат YAML.

## Формат входных данных
Пример входного файла:
```plaintext
; Это комментарий
=begin
Многострочный комментарий
=end
array = [1, 2, 3]
name = John Doe
value = 42
```

## Вывод
После выполнения программа преобразует данные в YAML:
```yaml
array:
- 1
- 2
- 3
name: John Doe
value: "42"
```

## Использование
1. Создайте входной файл в формате конфигурационного языка.
2. Запустите программу:
   ```bash
   python main.py --input input.config
   ```

## Требования
- Python 3.8+
- Установленный модуль `PyYAML`:
  ```bash
  pip install pyyaml
  ```

## Тестирование
Запустите тесты:
```bash
python -m unittest discover tests
```
