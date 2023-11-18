from napari_plugin_engine import napari_hook_implementation
from napari_tools_menu import register_function

@napari_hook_implementation
def napari_experimental_provide_function():
    return [create_gui, vary_gui, replace_gui]



@register_function(menu="Generate > Create new image (DALL-E 2, OpenAI, Darth-D)",
                   prompt={"widget_type": "TextEdit"},
                   image_size={"choices": [256, 512, 1024]})
def create_gui_dalle2(prompt:str, image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._create import create

    image = create(prompt=prompt, image_width=image_size, image_height=image_size, num_images=num_images, model='dall-e-2')

    return image


@register_function(menu="Generate > Create new image (DALL-E 3, OpenAI, Darth-D)",
                   prompt={"widget_type": "TextEdit"},
                   image_size={"choices": ["1024x1024", "1024x1792", "1792x1024"]},
                   quality={"choices": ["standard", "hd"]},
                   style={"choices": ["vivid", "natural"]}
                   )
def create_gui_dalle3(prompt:str, image_size:int="1024x1024", quality:str="standard", style:str="vivid") -> "napari.types.ImageData":
    from ._create import create

    image_size = image_size.split("x")
    image_width = int(image_size[0])
    image_height = int(image_size[1])

    image = create(prompt=prompt, image_width=image_width, image_height=image_height, model='dall-e-3')

    return image




@register_function(menu="Generate > Vary image (DALL-E 2, OpenAI, Darth-D)",
                   image_size={"choices": [256, 512, 1024]})
def vary_gui_dalle2(input_image:"napari.types.ImageData", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._vary import vary
    image = vary(input_image=input_image, image_width=image_size, image_height=image_size, num_images=num_images, model='dall-e-2')

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the vary function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image
    

@register_function(menu="Generate > Vary image (DALL-E 3, OpenAI, Darth-D)",
                   image_size={"choices": ["1024x1024", "1024x1792", "1792x1024"]})
def vary_gui_dalle3(input_image:"napari.types.ImageData", image_size:str="1024x1024") -> "napari.types.ImageData":
    from ._vary import vary

    image_size = image_size.split("x")
    image_width = int(image_size[0])
    image_height = int(image_size[1])

    image = vary(input_image=input_image, image_width=image_width, image_height=image_height, model='dall-e-3')

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the vary function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image


@register_function(menu="Generate > Replace masked region (DALL-E 2, OpenAI, Darth-D)",
                   prompt={"widget_type": "TextEdit"},
                   image_size={"choices": [256, 512, 1024]})
def replace_gui_dalle2(input_image:"napari.types.ImageData", mask:"napari.types.LabelsData", prompt:str = "A similar pattern like in the rest of the image", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._replace import replace
    image = replace(input_image=input_image, mask=mask, prompt=prompt, image_width=image_size, image_height=image_size, num_images=num_images, model='dall-e-2')

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image
    


@register_function(menu="Generate > Replace masked region (DALL-E 3, OpenAI, Darth-D)",
                   prompt={"widget_type": "TextEdit"},
                   image_size={"choices": ["1024x1024", "1024x1792", "1792x1024"]})
def replace_gui_dalle3(input_image:"napari.types.ImageData", mask:"napari.types.LabelsData", prompt:str = "A similar pattern like in the rest of the image", image_size:str="1024x1024") -> "napari.types.ImageData":
    from ._replace import replace

    image_size = image_size.split("x")
    image_width = int(image_size[0])
    image_height = int(image_size[1])

    image = replace(input_image=input_image, mask=mask, prompt=prompt, image_width=image_width, image_height=image_height, model='dall-e-3')

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image


@register_function(menu="Generate > Replace entire image (DALL-E 2, OpenAI, Darth-D)",
                   prompt={"widget_type": "TextEdit"},
                   image_size={"choices": [256, 512, 1024]})
def replace_entire_image_gui_dalle2(input_image:"napari.types.ImageData", prompt:str = "A similar pattern like in the rest of the image", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._replace import replace
    image = replace(input_image=input_image, mask=None, prompt=prompt, image_size=image_size, num_images=num_images)

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image


@register_function(menu="Generate > Replace entire image (DALL-E 3, OpenAI, Darth-D)",
                   prompt={"widget_type": "TextEdit"},
                   image_size={"choices": ["1024x1024", "1024x1792", "1792x1024"]})
def replace_entire_image_gui_dalle2(input_image:"napari.types.ImageData", prompt:str = "A similar pattern like in the rest of the image", image_size:str="1024x1024") -> "napari.types.ImageData":
    from ._replace import replace

    image_size = image_size.split("x")
    image_width = int(image_size[0])
    image_height = int(image_size[1])

    image = replace(input_image=input_image, mask=None, prompt=prompt, image_width=image_width, image_height=image_height, model='dall-e-3')

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image
