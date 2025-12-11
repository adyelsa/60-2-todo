# from datetime import date
# from flet import Text, TextField 

import flet  as ft 
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    # greeting_text.value = 'Привет мир'
    # greeting_text.color = ft.Colors.GREEN

    def on_button_click(_):
        print(name_input.value)
        name = name_input.value.strip()

        if name:
            ts = datetime.now(). strftime("%Y:%m:%d - %H:%M:%S")

            greeting_text.value = F"{ts} - Hello {name}" 
            greeting_text.color = None
            
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
        page.update()




    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    elevated_button = ft.ElevatedButton(text="Send", on_click=on_button_click, icon=ft.Icons.SEND, color=ft.Colors.GREEN, icon_color=ft.Colors.RED)

    text_button = ft.TextButton(text='Send', on_click=on_button_click, icon=ft.Icons.SEND)

    icon_button = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)




    page.add(greeting_text, name_input, text_button, elevated_button, icon_button)

ft.app(target=main)
# Сайт - view=ft.WEB_BROWSER
