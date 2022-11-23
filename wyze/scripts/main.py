import os
from wyze_sdk import *
from wyze_sdk.errors import WyzeApiError
from color_settings import *
from modify_lighting import *
from helpers import *

def main():
    if os.environ.get('WYZE_EMAIL') and os.environ.get('WYZE_PASSWORD'):
        client = Client(email=os.environ['WYZE_EMAIL'], password=os.environ['WYZE_PASSWORD'])
        light_bulbs = get_bulbs(client)

        # response = change_lighting_pattern(client, light_bulbs, get_lighting("bi-color-1")["colors"], get_lighting("rainbow")["brightness"])
        change_lighting_environment(client, gaming_setting())
        # turn_off_all_lights(client, light_bulbs)
    else:
        print("Need to give email and password to authenticate")
        print("export WYZE_EMAIL=<email>")
        print("export WYZE_PASSWORD=<password>")

main()