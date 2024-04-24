def create_greeting_template(template):
    def inner_function(last_name, first_name):
        # Заменяем плейсхолдеры `%F%` на фамилию и `%N%` на имя
        formatted_template = template.replace('%F%', last_name).replace('%N%', first_name)
        # Возвращаем отформатированную строку
        return formatted_template
    # Возвращаем внутреннюю функцию
    return inner_function
