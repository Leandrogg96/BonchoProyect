from enum import Enum

#Constants
MAX_WIDTH = "600px"

#Sizes
class Spacer(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"

title_style = dict(
   padding_top=Spacer.DEFAULT.value,
   margin_y= Spacer.DEFAULT
)