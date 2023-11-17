"""GPT-Terminal menu file."""

from gpterminal.config import MAX_TOKENS, OPENAI_KEY, GPT_MODEL


def get_menu():
    while True:
        welcome_to_menu_text = f"""

        Добро пожаловать в меню GPT-Terminal. 
        Вы можете настроить определенные параметры, написав число в консоль.
        (1): Настройка токена OpenAI API
        (2): Настройка модели GPT
        (3): Настройка MAX кол-ва токенов для запроса

        Текущие настройки:
        Ключ OpenAI API: {OPENAI_KEY}
        Модель GPT: {GPT_MODEL}
        MAX кол-во токенов на один запрос: {MAX_TOKENS}

        Чтобы выйти назад, напишите: chat
        Чтобы выйти из программы, напишите: exit
        """

        print(welcome_to_menu_text)

        user_input = input("Введите число или команду: ")

        if user_input.lower() == '1':
            print(f"Текущий Ключ OpenAI API: {OPENAI_KEY}")
            input_api = input("Введите новый Ключ OpenAI API: ")
            break
        if user_input.lower() == '2':
            print(f"Текущая Модель GPT: {GPT_MODEL}")
            input_model = input("Ввыберите другую модель: ")
            break
        if user_input.lower() == '3':
            print(f"Текущее MAX кол-во токенов на один запрос: {MAX_TOKENS}")
            input_max_tokens = int(input("Введите новое MAX кол-во токенов на один запрос: "))
            break

        
        if user_input.lower() == 'help':
            print(welcome_to_menu_text)
        if user_input.lower() == 'chat':
            print("В разработке...")
        if user_input.lower() == 'exit':
            break

        else:
            print('Такой команды или цифры нет. Попробуй сначала. Напиши help.')


def change_api():
    ...

def change_max_tokens():
    ...

def change_model():
    ...