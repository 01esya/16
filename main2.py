import sys
import python_f

if __name__ == '__main__':
    python_f.help1.help1()
    # Список работников.
    aircrafts = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        match command:
            case 'exit':
                break

            case 'add':
                # Добавить словарь в список.
                i = python_f.add1.add1()
                aircrafts.append(i)
                # Отсортировать список в случае необходимости.
                if len(aircrafts) > 1:
                    aircrafts.sort(key=lambda item: item.get('name', ''))

            case 'list':
                python_f.list.list(aircrafts)

            case 'select':
                i = input('Введите тип:')
                python_f.select.select(i, aircrafts)

            case 'help':
                python_f.help1.help1()

            case _:
                python_f.error1.error1(command)