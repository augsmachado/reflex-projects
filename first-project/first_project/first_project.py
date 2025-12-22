"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Contador com Reflex", size="9"),
            rx.text("Contagem atual: ", State.count, size="6"),
            rx.hstack(
                rx.button("Diminuir", on_click=State.decrement, color_scheme="red"),
                rx.button("Aumentar", on_click=State.increment, color_scheme="green"),
                spacing="4",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

app = rx.App()
app.add_page(index)
