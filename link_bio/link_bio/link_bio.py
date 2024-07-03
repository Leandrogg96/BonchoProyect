import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.components.footer import footer
import link_bio.styles.styles as styles

from rxconfig import config


class State(rx.State):
    """The app state."""

    ... 


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        header(),
        footer(),
        
    )


app = rx.App()
app.add_page(index)
