"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    expression: str = ""
    result: str = ""

    def add(self, value: str):
        self.expression += value

    def clear(self):
        self.expression = ""
        self.result = ""

    def calculate(self):
        try:
            self.result = str(eval(self.expression))
        except Exception:
            self.result = "Erro"


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Calculadora Reflex", size="9"),
            rx.text("Expressão: ", State.expression, size="6"),
            rx.text("Resultado: ", State.result, size="6"),
            rx.hstack(
                rx.button("7", on_click=lambda: State.add("7"), width="25%"),
                rx.button("8", on_click=lambda: State.add("8"), width="25%"),
                rx.button("9", on_click=lambda: State.add("9"), width="25%"),
                rx.button("/", on_click=lambda: State.add("/"), width="25%"),
            ),
            rx.hstack(
                rx.button("4", on_click=lambda: State.add("4"), width="25%"),
                rx.button("5", on_click=lambda: State.add("5"), width="25%"),
                rx.button("6", on_click=lambda: State.add("6"), width="25%"),
                rx.button("*", on_click=lambda: State.add("*"), width="25%"),
            ),
            rx.hstack(
                rx.button("1", on_click=lambda: State.add("1"), width="25%"),
                rx.button("2", on_click=lambda: State.add("2"), width="25%"),
                rx.button("3", on_click=lambda: State.add("3"), width="25%"),
                rx.button("-", on_click=lambda: State.add("-"), width="25%"),
            ),
            rx.hstack(
                rx.button("0", on_click=lambda: State.add("0"), width="25%"),
                rx.button(".", on_click=lambda: State.add("."), width="25%"),
                rx.button("C", on_click=State.clear, color_scheme="red", width="25%"),
                rx.button("+", on_click=lambda: State.add("+"), width="25%"),
            ),
            rx.button("=", on_click=State.calculate, color_scheme="green", width="100%"),
            spacing="3",
            justify="center",
            align="center",
            min_height="85vh",
            width="320px",
        ),
        justify="center",
        align="center",
        width="100vw",
        height="100vh",
    )


app = rx.App()
app.add_page(index)
