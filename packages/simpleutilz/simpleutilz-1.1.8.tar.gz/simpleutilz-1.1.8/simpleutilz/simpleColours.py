import os
import colorspacious as cs


def RGB_to_colour(value):
    '''Converts RGB value to a colour string'''
    denaryValue = convert_value_to_denary(value, "rgb")
    colour = Binary_search(denaryValue, 'ListOfColours.py')
    return colour

def hex_to_colour(value):
    '''Converts hex value to a colour string'''
    denaryValue = convert_value_to_denary(value, "hex")
    colour = Binary_search(denaryValue, 'ListOfColours.py')
    return colour
    
def RGBA_to_colour(value):
    '''Converts RGBA value to a colour string'''
    denaryValue = convert_value_to_denary(value, "rgba")
    colour = Binary_search(denaryValue, 'ListOfColours.py')
    return colour

def binary_to_colour(value):
    '''Converts binary value to a colour string'''
    denaryValue = convert_value_to_denary(value, "binary")
    colour = Binary_search(denaryValue, 'ListOfColours.py')
    return colour

def hex_to_colour_not_precise(value):
    '''Converts hex value to a colour string'''
    colour = find_closest_color(value)
    return colour

# Define the predefined colors in hex format
colors_hex = {
    "Black": "#000000",
    "Blue": "#0000FF",
    "Green": "#00FF00",
    "Purple": "#800080",
    "Brown": "#A52A2A",
    "Red": "#FF0000",
    "Orange": "#FFA500",
    "Pink": "#FFC0CB",
    "Yellow": "#FFFF00",
    "White": "#FFFFFF",
}

def hex_to_lab(hex_color):
    hex_value = hex_color.lstrip('#')
    rgb = tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))
    lab_color = cs.cspace_convert(rgb, "sRGB255", "CAM02-UCS")
    return lab_color


def calculate_distance(color1, color2):
    delta = [c1 - c2 for c1, c2 in zip(color1, color2)]
    distance = sum(delta_i ** 2 for delta_i in delta) ** 0.5
    return distance

def find_closest_color(input_hex):
    input_lab = hex_to_lab(input_hex)
    closest_color = min(colors_hex.keys(), key=lambda color: calculate_distance(input_lab, hex_to_lab(colors_hex[color])))
    return closest_color
   
def convert_value_to_denary(value, whatFormat):
    '''Converts a value to denary'''
    if whatFormat == "hex":
        if "#" in value:
            hexWithoutHashTag = value.replace("#","")
        else:
            hexWithoutHashTag = value
        hexWithoutHashTag = hexWithoutHashTag.upper()
        denaryValue = int(hexWithoutHashTag, 16)
    elif whatFormat == "rgb":
        if "(" in value:
            rgbWithoutBrackets = value.replace("(","")
            rgbWithoutBrackets = rgbWithoutBrackets.replace(")","")
        else:
            rgbWithoutBrackets = value
        rgbWithoutBrackets = rgbWithoutBrackets.split(",")
        hexValue = '{:02x}{:02x}{:02x}'.format(int(rgbWithoutBrackets[0]), int(rgbWithoutBrackets[1]), int(rgbWithoutBrackets[2]))
        denaryValue = int(hexValue, 16)
    elif whatFormat == "rgba":
        if "(" in value:
            rgbWithoutBrackets = value.replace("(","")
            rgbWithoutBrackets = rgbWithoutBrackets.replace(")","")
        else:
            rgbWithoutBrackets = value
        rgbWithoutBrackets = rgbWithoutBrackets.split(",")
        hexValue = '{:02x}{:02x}{:02x}{:02x}'.format(int(rgbWithoutBrackets[0]), int(rgbWithoutBrackets[1]), int(rgbWithoutBrackets[2]), int(rgbWithoutBrackets[3]))
        denaryValue = int(hexValue, 16)
    elif whatFormat == "binary":
        if "0b" in value:
            binaryWithout0b = value.replace("0b","")
        else:
            binaryWithout0b = value
        denaryValue = int(binaryWithout0b, 2)
    else:
        return ("Not a valid format")
        
    return denaryValue    
    
def Binary_search(value, dataset):
    '''Binary search to find the colour in the dataset'''
    file_path = os.path.join(os.path.dirname(__file__), dataset)
    with open(file_path, "r") as file:
        lines = file.readlines()
    low = 0
    high = len(lines) - 1

    while low <= high:
        mid = (low + high) // 2
        line = lines[mid].split(',')[0]

        if int(line) == int(value):
            return lines[mid].split(',')[1]
        elif int(line) < int(value):
            low = mid + 1
        else:
            high = mid - 1
    
    upperValue = lines[mid + 1].split(',')[0]
    lowerValue = lines[mid - 1].split(',')[0]
    if (int(upperValue) - int(mid)) > (int(mid) - int(lowerValue)):
        return lines[mid].split(',')[1]
    else:
        return lines[mid+2].split(',')[1]    
    
    
if __name__ == "__main__":
    print(hex_to_colour_not_precise(input("Enter value innit: ")))