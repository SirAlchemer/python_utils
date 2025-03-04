from .util_classes import ANSI_Codes   
    
def ANSI(string: str, **kwargs) -> str:
    if kwargs.get("red", False) == True:
        string = ANSI_Codes.RED + string
    if kwargs.get("cyan", False) == True:
        string = ANSI_Codes.CYAN + string
    if kwargs.get("add_end_ansi", True) == False: 
        return string
    if kwargs.get("bold", False) == True:
        string = ANSI_Codes.BOLD + string
    if kwargs.get("dark_gray", False) == True:
        string = ANSI_Codes.DARK_GRAY + string
    if kwargs.get("italics", False) == True:
        string = ANSI_Codes.ITALICS + string
    if kwargs.get("underline", False) == True:
        string = ANSI_Codes.UNDERLINE + string
    if kwargs.get("white_background", False) == True:
        string = ANSI_Codes.WHITE_BACKGROUND + string
    if kwargs.get("black", False) == True:
        string = ANSI_Codes.BLACK + string
    if kwargs.get("strike_through", False) == True:
        string = ANSI_Codes.STRIKE_THROUGH + string
    if kwargs.get("double_underline", False) == True:
        string = ANSI_Codes.DOUBLE_UNDERLINE + string
    if kwargs.get("red_background", False) == True:
        string = ANSI_Codes.RED_BACKGROUND + string
    if kwargs.get("mint_background", False) == True:
        string = ANSI_Codes.MINT_BACKGROUND + string
    if kwargs.get("yellow_background", False) == True:
        string = ANSI_Codes.YELLOW_BACKGROUND + string
    if kwargs.get("blue_background", False) == True:
        string = ANSI_Codes.BlUE_BACKGROUND + string
    if kwargs.get("magenta_background", False) == True:
        string = ANSI_Codes.MAGENTA_BACKGROUND + string
    if kwargs.get("cyan_background", False) == True:
        string = ANSI_Codes.CYAN_BACKGROUND + string
    if kwargs.get("white_background", False) == True:
        string = ANSI_Codes.WHITE_BACKGROUND + string
    if kwargs.get("overline", False) == True:
        string = ANSI_Codes.OVER_LINE + string
    if kwargs.get("light_red", False) == True:
        string = ANSI_Codes.LIGHT_RED + string
    if kwargs.get("gray_background", False) == True:
        string = ANSI_Codes.GRAY_BACKGROUND + string
    if kwargs.get("light_red_background", False) == True:
        string = ANSI_Codes.LIGHT_RED_BACKGROUND + string
    if kwargs.get("gray", False) == True:
        string = ANSI_Codes.GRAY + string
    if kwargs.get("mint", False) == True:
        string = ANSI_Codes.MINT + string
    if kwargs.get("yellow", False) == True:
        string = ANSI_Codes.YELLOW + string
    if kwargs.get("magenta", False) == True:
        string = ANSI_Codes.MAGENTA + string
    if kwargs.get("white", False) == True:
        string = ANSI_Codes.WHITE + string
    if kwargs.get("light_red", False) == True:
        string = ANSI_Codes.LIGHT_RED + string
    if kwargs.get("light_red_background", False) == True:
        string = ANSI_Codes.LIGHT_RED_BACKGROUND + string
    if kwargs.get("gray_background", False) == True:
        string = ANSI_Codes.GRAY_BACKGROUND + string
    if kwargs.get("light_blue", False) == True:
        string = ANSI_Codes.CYAN + string
    return string + ANSI_Codes.END_ANSI
