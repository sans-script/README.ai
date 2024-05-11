import flet as ft
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def main(page):
    # Prompt Input
    prompt_field = ft.TextField(
        hint_text="Escreva um README sobre...",
        expand=True,
        multiline=True,
        max_lines=2
    )

    # Result Display Area
    result_field = ft.Column(
        height=500,
        width=700,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Markdown(
                "# Resultado aqui ✨",
                selectable=True,
                extension_set="gitHubWeb",
                code_theme="atom-one-dark",
                data="", # Initialize with empty content
            )
        ]
    )
    result_field_mk = result_field.controls[0] # Get the Markdown control

    # Editable Text Area
    response_field = ft.TextField(
        height=500,
        width=700,
        label="Você pode editar aqui ✨",
        multiline=True,
        min_lines=1,
        max_lines=30,
        value="",
        on_change=lambda e: editor_mk(e, result_field_mk) # Pass Markdown control to editor_mk
    )

    # --- Functions ---
    def add_text(event):
        prompt = prompt_field.value
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(prompt)

        result_field_mk.value = response.text
        response_field.value = response.text
        prompt_field.value = ""
        page.update()

    def editor_mk(event, result_mk):
        result_mk.value = event.control.value 
        page.update()
    
    # --- Layout ---
    view = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    prompt_field,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_text, tooltip="Adicionar prompt")
                ],
            ),
        ],
    )

    content_window = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    response_field,
                    result_field,
                ],
            ),
        ],
    )

    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text("README.ai", size=60))
    page.add(ft.Text("Seu Editor de README com Inteligência Artificial ✨", theme_style=ft.TextThemeStyle.HEADLINE_SMALL))
    page.add(ft.Text(""))
    page.add(content_window)
    page.add(view)


# ft.app(main, view=ft.WEB_BROWSER) 
ft.app(main)