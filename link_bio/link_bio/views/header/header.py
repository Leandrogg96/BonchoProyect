import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.title import title


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="LogoB.jpg", 
                     width="23%", 
                     height="auto",
                     border_radius="50%"),
            title("Bienvenidos a Boncho!"),
        ),
   
    rx.box( 
            rx.text("En Boncho, nos especializamos en ofrecerte lo mejor de la comida casera y pizzas al estilo italiano. ¡Ven y disfruta de nuestros deliciosos platos!"),
            rx.text("Horarios:", weight="bold"),
            rx.text("Lunes a sábados de 12:00 a 14:30 || Martes a domingos de 21:00 a 00:00."),
            rx.text("Además de nuestras sabrosas pizzas 🍕 tambien tenemos deliciosos lomitos🥪 que te encantarán."),
            rx.text("Direccion: 📍Independencia 572", weight="bold")
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
            padding=styles.Spacer.DEFAULT.value
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