import colorama
from dataclasses import dataclass

colors = colorama.Fore

@dataclass(frozen=True)
class settings:
    reset : str = colors.RESET

    string : str = colors.LIGHTGREEN_EX
    boolean : str = colors.LIGHTMAGENTA_EX

    integer : str = colors.LIGHTYELLOW_EX
    decimal : str = colors.LIGHTYELLOW_EX
    
    array : str = colors.LIGHTBLUE_EX
    dictionary : str = colors.LIGHTRED_EX
