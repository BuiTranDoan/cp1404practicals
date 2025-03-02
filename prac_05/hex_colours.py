COLOURS_TO_HEX = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "Blue": "#0000FF",
    "BlueViolet": "#8A2BE2"
}

colour_name = input("Enter colour name: ").strip().title()
while colour_name:
    try:
        print(f"{colour_name} has hex code {COLOURS_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().title()
