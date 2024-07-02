import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
            rx.text(
                    rx.text.em("Lema Boncho"),
                    align="center", 
                    size="6"
                )
            )