import reflex as rx
import link_bio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.center(
                rx.heading(  
                    text,
                size="8",
                width="100%",
                style=styles.title_style
                )
            )