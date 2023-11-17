from gpterminal.config import MODELS_LIST


def check_api(OPENAI_KEY):
    while not OPENAI_KEY or not (40 <= len(OPENAI_KEY) <= 64):
        OPENAI_KEY = input("Пожалуйста, введите ваш OpenAI API ключ (длина ключа должна быть от 40 до 64 символов): ")

    with open('gpterminal/config.py', 'r') as file:
        data = file.readlines()
    with open('gpterminal/config.py', 'w') as file:
        for line in data:
            if line.startswith('OPENAI_KEY'):
                file.write(f"OPENAI_KEY = '{OPENAI_KEY}'\n")
            else:
                file.write(line)
    return OPENAI_KEY


def check_max_tokens(MAX_TOKENS):
    while not MAX_TOKENS or not (100 <= MAX_TOKENS <= 4096):
        try:
            MAX_TOKENS = int(input("Пожалуйста, введите максимальное количество токенов (от 100 до 4096): "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

    with open('gpterminal/config.py', 'r') as file:
        data = file.readlines()
    with open('gpterminal/config.py', 'w') as file:
        for line in data:
            if line.startswith('MAX_TOKENS'):
                file.write(f"MAX_TOKENS = {MAX_TOKENS}\n")
            else:
                file.write(line)
    return MAX_TOKENS




def check_model(GPT_MODEL):
    while True:
        if not GPT_MODEL or GPT_MODEL not in MODELS_LIST:
            print("Указанная модель недопустима. Доступные модели:")
            print(", ".join(MODELS_LIST))
            GPT_MODEL = input("Пожалуйста, укажите модель: ")
        else:
            break

    # Записываем полученное значение в файл config.py
    with open('gpterminal/config.py', 'r') as file:
        data = file.readlines()
    with open('gpterminal/config.py', 'w') as file:
        for line in data:
            if line.startswith('GPT_MODEL'):
                file.write(f"GPT_MODEL = '{GPT_MODEL}'\n")
            else:
                file.write(line)
    return GPT_MODEL
