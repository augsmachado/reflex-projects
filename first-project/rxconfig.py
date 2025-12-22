import reflex as rx

config = rx.Config(
    app_name="first_project",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)