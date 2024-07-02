import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header


from rxconfig import config


class State(rx.State):
    """The app state."""

    ... 


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        navbar(),
        header(),
        rx.vstack(
            rx.heading("Welcome to Boncho!", 
                       align="center", 
                       direction="column", 
                       spacing="3", 
                       width="100%", 
                       size="9", 
                       weight="bold", 
                       color_scheme="crimson",
                       high_contrast=True),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
