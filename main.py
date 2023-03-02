from dotenv import load_dotenv
import os
import spotipy
import asyncio
from spotipy.oauth2 import SpotifyOAuth
from pywizlight import wizlight, PilotBuilder, discovery

load_dotenv()

def spotify_testing():

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    SCOPE = "user-read-currently-playing"

    print(client_id, client_secret, redirect_uri)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

    # results = sp.current_user_saved_tracks()
    current = sp.currently_playing()

    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['artists'][0]['name'], " – ", track['name'])


async def pywiz_testing():
    # Discover all bulbs in the network via broadcast datagram (UDP)
    # function takes the discovery object and returns a list of wizlight objects.
    bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    # Print the IP address of the bulb on index 0
    print(f"Bulb IP address: {bulbs[0].ip}")

    # Iterate over all returned bulbs
    for bulb in bulbs:
        print(bulb.__dict__)
        await bulb.turn_off()

    # Set up a standard light
    light = wizlight("192.168.1.10")

    # Turn the light on into "rhythm mode"
    # await light.turn_on(PilotBuilder())

    # # Set bulb brightness
    # await light.turn_on(PilotBuilder(brightness = 255))

    # # Set bulb brightness (with async timeout)
    timeout = 500
    await asyncio.wait_for(light.turn_on(PilotBuilder(brightness = 10)), timeout)

    # # Set bulb to warm white
    # await light.turn_on(PilotBuilder(warm_white = 255))

    # # Set RGB values. red to 0 = 0%, green to 128 = 50%, blue to 255 = 100%
    # await light.turn_on(PilotBuilder(rgb = (0, 128, 255)))
    
    # # Get the current color temperature, RGB values
    # state = await light.updateState()
    # print(state.get_colortemp())
    # red, green, blue = state.get_rgb()
    # print(f"red {red}, green {green}, blue {blue}")

    # # Start a scene
    # await light.turn_on(PilotBuilder(scene = 4)) # party

    # # Get the name of the current scene
    # state = await light.updateState()
    # print(state.get_scene())

    # # Get the features of the bulb
    # bulb_type = await bulbs[0].get_bulbtype()
    # print(bulb_type.features.brightness) # returns True if brightness is supported
    # print(bulb_type.features.color) # returns True if color is supported
    # print(bulb_type.features.color_tmp) # returns True if color temperatures are supported
    # print(bulb_type.features.effect) # returns True if effects are supported
    # print(bulb_type.kelvin_range.max) # returns max kelvin in INT
    # print(bulb_type.kelvin_range.min) # returns min kelvin in INT
    # print(bulb_type.name) # returns the module name of the bulb

    # # Turn the light off
    # await light.turn_off()

def main():

    # spotify_testing()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pywiz_testing())

if __name__ == '__main__':
    main()