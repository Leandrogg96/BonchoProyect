import reflex as rx
from link_bio.styles.styles import Spacer

def navbar_link(text: str, url: str, value: bool) -> rx.Component:
    return rx.link(
        rx.text(text, 
                size="4", 
                weight="bold",
                color_scheme="brown"),
                is_external=value, 
                href=url
        )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/LogoB.jpg",
                        width=Spacer.BIG,
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Boncho", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#", False),
                    navbar_link("Quienes somos?", "/#", False),
                    navbar_link("Productos", "/#", False),
                    navbar_link("Instagram", "https://www.instagram.com/boncho_comidas/", True),
                    navbar_link("Contacto", "/#", False),
                    navbar_link("Hace tu pedido!", "https://menu.fu.do/boncho", True),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width=Spacer.BIG,
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Boncho", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("brown", 3),
        padding_y=Spacer.SMALL,
        padding_x=Spacer.SMALL,
        #position="fixed",
        top="0px",
        # z_index="5",
        width="100%",
    )