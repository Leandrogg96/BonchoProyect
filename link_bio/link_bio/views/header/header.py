import reflex as rx
import link_bio.components.styles.styles as styles



def header() -> rx.Component:
    return rx.flex(
    rx.avatar(src="LogoB.jpg", fallback="BC", size="9"),
    rx.text("BONCHO", weight="bold", size="4"),
    rx.box( 
            rx.text("Comidas caseras y pizzas Lunes a Sabados de 12 a 14:30"),
            rx.text("🍝Comidas caseras Martes a Domingos de 21 a 00hs"),
            rx.text("🍕Pizzas estilo italianas y lomitos🥪"),
            rx.text("Direccion: 📍Independencia 572"),
            rx.text("@boncho_comidas", color_scheme="brown")
    ),
    rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="instagram"
                )
            ),
            "Ver perfil",
            color_scheme="brown",
            variant="solid",
            width="100%",
            padding=styles.Spacer.MEDIUM.value
            ),
            href="https://www.instagram.com/boncho_comidas/",
            is_external=True,
            width="100%"
        ),
    align="center",
    direction="column",
    justify="end",
    spacing="1",
)