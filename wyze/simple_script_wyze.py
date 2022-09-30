import os
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

def main():
    client = Client(email=os.environ['WYZE_EMAIL'], password=os.environ['WYZE_PASSWORD'])

    try:
        response = client.bulbs.list()
        light_bulbs = {}
        for device in response:
            light_bulbs[device.nickname] = client.bulbs.info(device_mac=device.mac)
    except WyzeApiError as e:
        # You will get a WyzeApiError if the request failed
        print(f"Got an error: {e}")

    change_lighting(client, light_bulbs, get_lighting("bi-color-1")["colors"], get_lighting("bi-color-1")["brightness"])


def change_lighting(client, bulbs, colors, brightness):
    color_iteration = 0
    bright_iteration = 0
    for bulb_name in bulbs.keys():
        bulb = bulbs[bulb_name]
        if not( bulb.is_on):
            client.bulbs.turn_on(device_mac=bulb.mac, device_model=bulb.product.model) 
        client.bulbs.set_brightness(device_mac=bulb.mac, device_model=bulb.product.model, brightness=brightness[bright_iteration])
        client.bulbs.set_color(device_mac=bulb.mac, device_model=bulb.product.model, color=colors[color_iteration])
        
        color_iteration = 1 + color_iteration if color_iteration < len(colors) - 1 else 0
        bright_iteration = 1 + bright_iteration if bright_iteration < len(brightness) - 1 else 0

def get_lighting(name_1):
    match name_1:
        case "bi-color-1":
            return { "colors": ['0000FF', 'FF00FF', 'AA336A'] , "brightness": [60]}
        case "les-color-1":
            return { "colors": ['cc5500', 'ffa500', 'AA336A'] , "brightness": [60]}

main()