
def change_lighting_pattern(client, bulbs, colors, brightness):
    current_settings = {}
    color_iteration = 0
    bright_iteration = 0
    for bulb_name in bulbs.keys():
        bulb = bulbs[bulb_name]
        client.bulbs.turn_on(device_mac=bulb.mac, device_model=bulb.product.model)
        client.bulbs.set_brightness(device_mac=bulb.mac, device_model=bulb.product.model, brightness=brightness[bright_iteration])
        client.bulbs.set_color(device_mac=bulb.mac, device_model=bulb.product.model, color=colors[color_iteration])
        
        color_iteration = 1 + color_iteration if color_iteration < len(colors) - 1 else 0
        bright_iteration = 1 + bright_iteration if bright_iteration < len(brightness) - 1 else 0

        current_settings[bulb.mac] = {
            "color": colors[color_iteration],
            "brightness": brightness[bright_iteration],
            "name": bulb_name
        }

    return current_settings

def change_lighting_environment(client, env_pattern):
    for bulb_mac in env_pattern.keys():
        bulb = env_pattern[bulb_mac]
        client.bulbs.turn_on(device_mac=bulb_mac, device_model=bulb["model"])
        client.bulbs.set_brightness(device_mac=bulb_mac, device_model=bulb["model"], brightness=bulb["brightness"])
        client.bulbs.set_color(device_mac=bulb_mac, device_model=bulb["model"], color=bulb["color"])
        # client.bulbs.set_color_temp(device_mac=bulb_mac, device_model=bulb["model"], color_temp=bulb["color_temperature"])

def get_current_configuration(client):
    all_bulbs = client.devices_list()
    current_settings = {}
    for bulb in all_bulbs:
        if bulb.type == 'MeshLight':
            bulb_info = client.bulbs.info(device_mac=bulb.mac)
            current_settings[bulb.mac] = {
                "model": bulb_info.product.model, 
                "brightness": bulb_info.brightness,
                "color": bulb_info.color,
                "color_temperature": bulb_info.color_temp,
                "is_on": bulb_info.is_on,
                "is_online": bulb_info.is_online,
                "name": bulb_info.nickname
            }

# Helper functions

def gaming_setting():
    return {
        '7C78B27B9361': 
            {'model': 'WLPA19C', 'brightness': 52, 'color': 'FF7F48', 'color_temperature': 3672, 'is_on': True, 'is_online': True, 'name': 'Ghost Lamp 3 (droopy boi)'}, 
        '7C78B28D3F1A': 
            {'model': 'WLPA19C', 'brightness': 52, 'color': 'EB41AF', 'color_temperature': 3672, 'is_on': True, 'is_online': True, 'name': 'Ghost Lamp 2'}, 
        '7C78B27DF043': 
            {'model': 'WLPA19C', 'brightness': 52, 'color': '911FFF', 'color_temperature': 3672, 'is_on': True, 'is_online': True, 'name': 'Ghost Lamp 1'}, 
        '7C78B28D2492': 
            {'model': 'WLPA19C', 'brightness': 52, 'color': '911FFF', 'color_temperature': 5935, 'is_on': True, 'is_online': True, 'name': 'Desk Lamp'}, 
        '7C78B28E35FE': 
            {'model': 'WLPA19C', 'brightness': 20, 'color': 'FF7F48', 'color_temperature': 3672, 'is_on': True, 'is_online': True, 'name': 'Target Standing Lamp'}, 
        '7C78B28E04E1': 
            {'model': 'WLPA19C', 'brightness': 3, 'color': 'FFCB47', 'color_temperature': 3500, 'is_on': True, 'is_online': False, 'name': 'Bedroom side light'}, 
        '7C78B28D3F8F': 
            {'model': 'WLPA19C', 'brightness': 51, 'color': 'FFD87D', 'color_temperature': 4065, 'is_on': True, 'is_online': False, 'name': 'Bedroom overhead'}, 
        '7C78B28D9EF6': 
            {'model': 'WLPA19C', 'brightness': 40, 'color': 'AA336A', 'color_temperature': 5687, 'is_on': True, 'is_online': True, 'name': 'Ikea Lamp'}}