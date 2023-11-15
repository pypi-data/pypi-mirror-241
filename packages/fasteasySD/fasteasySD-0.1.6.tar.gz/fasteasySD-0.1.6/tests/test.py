import sys
sys.path.append("/home/waganawa/Documents/project_lcm_python/fasteasySD/src/fasteasySD")

from fasteasySD import FastEasySD

test = FastEasySD(device='cpu',use_fp16=False)

"""test.make_image(mode="txt2img",
                model_type="SD",model_path="milkyWonderland_v20.safetensors",
                lora_path=".",lora_name="chamcham_new_train_lora_2-000001.safetensors",
                prompt="sharp details, sharp focus, anime style, masterpiece, best quality, chamcham(twitch), hair bell, hair ribbon, multicolored hair, two-tone hair, 1girl, solo, orange shirt, long hair, hair clip",
                n_prompt="bad hand,text,watermark,low quality,medium quality,blurry,censored,wrinkles,deformed,mutated text,watermark,low quality,medium quality,blurry,censored,wrinkles,deformed,mutated",
                seed=0,steps=8,cfg=2,height=960,width=512,num_images=1)"""

test.make_image(mode="txt2img",
                model_type="SDXL",model_path="x2AnimeFinal_gzku.safetensors",
                lora_path=".",lora_name="ganyu2x_xl.safetensors",
                prompt="sharp details, sharp focus, ganyu (genshin impact),breasts,horns,blue hair,purple eyes,blush,gloves,bell,bare shoulders,bangs,black gloves,detached sleeves,neck bell,ahoge,sidelocks,goat horns,",
                n_prompt="bad hand,text,watermark,low quality,medium quality,blurry,censored,wrinkles,deformed,mutated text,watermark,low quality,medium quality,blurry,censored,wrinkles,deformed,mutated",
                seed=0,steps=8,cfg=2,height=1024,width=1024,num_images=1)

test.make_image(mode="img2img",
                model_type="SD",model_path="milkyWonderland_v20.safetensors",
                prompt="sharp details, sharp focus, glasses, anime style, 1man",
                seed=0,steps=4,cfg=2,height=960,width=512,num_images=1,prompt_strength=0.3,input_image_dir="input.jpg")