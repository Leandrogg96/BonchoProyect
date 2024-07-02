import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.components.footer import footer
import link_bio.components.styles.styles as styles

from rxconfig import config


class State(rx.State):
    """The app state."""

    ... 


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Spacer.BIG
            ),
        ),
        footer(),
    )


app = rx.App()
app.add_page(index)
