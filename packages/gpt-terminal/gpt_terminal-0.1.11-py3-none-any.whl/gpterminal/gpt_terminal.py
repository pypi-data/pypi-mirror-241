"""GPT-Terminal main file."""
from gpterminal.gpt_settings import get_chatgpt_response
from gpterminal.menu import get_menu

def main():


    print("""
          Привет! Для выхода из программы введите 'exit'
          
          Напиши: 'menu', если хочешь зайти в настройки.
          """)
    while True:
        try:
            user_input = input("Вы: ")

            if user_input.lower() == 'exit':
                print("\nСпасибо за использование, возвращайтесь еще!")
                break

            if user_input.lower() == 'menu':
                get_menu()
                break

            response = get_chatgpt_response(user_input)
            print(f"ChatGPT: {response}")
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("\nСкрипт прерван пользователем.")
            break


if __name__ == "__main__":
    main()
