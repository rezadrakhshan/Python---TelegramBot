from pyrogram import Client
import time

api_id = ''
api_hash = ''


def convert_to_subscript_numbers(time_str):
    numerals = "₀₁₂₃₄₅₆₇₈₉"
    return ''.join(numerals[int(char)] if char.isdigit() else char for char in time_str)

with Client("my_account", api_id, api_hash) as app:
    while True:
        current_time = time.strftime("%H:%M", time.localtime())
        subscript_time = convert_to_subscript_numbers(current_time)
        app.update_profile(first_name=f"|. 𝓐𝓰𝓱𝓪𝔂𝓮 𝓫𝓸𝔃𝓸𝓻𝓰 .🥀| {subscript_time}")
        time.sleep(60)
