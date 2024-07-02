import reflex as rx

def header() -> rx.Component:
    return rx.flex(
    rx.avatar(src="/logo.jpg", fallback="RU", size="9"),
    rx.text("BONCHO", weight="bold", size="4"),
    rx.text("@boncho_comidas", color_scheme="gray"),
    rx.button(
        "Edit Profile",
        color_scheme="indigo",
        variant="solid",
    ),
    direction="column",
    spacing="1",
)