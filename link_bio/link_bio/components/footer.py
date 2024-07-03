import reflex as rx

def footer() -> rx.Component:
    return rx.center(
                rx.text(
                    rx.text.em("La excelencia en cada producto. Más que comida, una experiencia")
                    #align="center", 
                    #size="3"
                ),
            )