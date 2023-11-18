"""
Myfreegpt's prodia module
"""

from random import randint
from aiohttp import ClientSession, ClientError
import requests


class Generation:
    

    async def create(self, prompt):
        try:
            url = "https://api.prodia.com/v1/sd/generate"

            payload = {
    "prompt": "prompt",
    "model": "dreamshaper_6BakedVae.safetensors [114c8abb]",
    "negative_prompt": "(nsfw:1.5),verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
    "steps": 50,
    "cfg_scale": 9.5,
    "seed": "randint(1, 10000)",
    "sampler": "Euler",
    "aspect_ratio": "square"
}
            headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

            resp = requests.post(url, json=payload, headers=headers)
        except ClientError as exc:
            raise ClientError("Unable to fetch the response.") from exc
