from color_settings import *

def display_current_settings(current_light):
    for bulb in current_light.keys():
        print("--------------------------")
        print("Bulb Name: %s\n" % current_light[bulb]["name"])
        print("Bulb Color: %s\n" % color_from_hex(current_light[bulb]["name"]))
        print("Bulb Color Hex: %s\n" % current_light[bulb]["color"])
        print("Bulb Brightness: %s\n" % current_light[bulb]["brightness"])
        print("--------------------------")


def get_bulbs(client):
    try:
        response = client.bulbs.list()
        light_bulbs = {}
        for device in response:
            light_bulbs[device.mac] = client.bulbs.info(device_mac=device.mac)
    except WyzeApiError as e:
        # You will get a WyzeApiError if the request failed
        print(f"Got an error: {e}")
    
    return light_bulbs

def turn_off_all_lights(client, bulbs):
    for bulb in bulbs.keys():
        client.bulbs.turn_off(device_mac=bulbs[bulb].mac, device_model=bulbs[bulb].product.model)