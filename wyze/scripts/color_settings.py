import colour

def get_lighting(name_1):
    match name_1:
        case "bi-color-1":
            return { "colors": 
                        [colour.Color("blue").get_hex_l(), 
                        'FF00FF', 
                        'AA336A',
                        'cc5500', 
                        'ffa500'] , 
                     "brightness": [60]}
        case "les-color-1":
            return { "colors": 
                        ['cc5500', 
                        'ffa500'] , 
                     "brightness": [60]}
        case "fav-color-1":
            return { "colors": 
                        ['FFA500', 
                        'FFC0CB', 
                        'A020F0'] , 
                     "brightness": [40]}
        case "rainbow":
            return { 
                    "colors": [
                        get_colors("red"), 
                        get_colors("orange"), 
                        get_colors("yellow"), 
                        get_colors("green"), 
                        get_colors("blue"), 
                        get_colors("violet")
                     ],
                     "brightness": [40]
                    }

def get_colors(color_name):
    color_name_corrected = color_name.lower()
    match color_name_corrected:
        case "red":
            return 'FF0000'
        case "orange":
            return 'FFA500'
        case "yellow":
            return 'FFFF00'
        case "green":
            return '00FF00'
        case "blue":
            return '00FFFF'
        case "violet":
            return '7f00ff'
        case other:
            # Default
            return 'FFFFFF'

def color_from_hex(hex_color):
    match hex_color:
        case "FF0000":
            return 'red'
        case "FFA500":
            return 'orange'
        case "FFFF00":
            return 'yellow'
        case "00FF00":
            return 'green'
        case "00FFFF":
            return 'blue'
        case "7f00ff":
            return 'violet'
        case other:
            return 'color not stored.'