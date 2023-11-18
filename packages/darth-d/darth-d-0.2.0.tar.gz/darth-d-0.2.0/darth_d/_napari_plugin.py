from napari_plugin_engine import napari_hook_implementation
from napari_tools_menu import register_function

@napari_hook_implementation
def napari_experimental_provide_function():
    return [create_gui, vary_gui, replace_gui]



@register_function(menu="Generate > Create new image (DALL-E 2, OpenAI, Darth-D)",
                   image_size={"choices": [256, 512, 1024]})
def create_gui(prompt:str, image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._create import create

    image = create(prompt=prompt, image_size=image_size, num_images=num_images)

    return image

@register_function(menu="Generate > Vary image (DALL-E 2, OpenAI, Darth-D)",
                   image_size={"choices": [256, 512, 1024]})
def vary_gui(input_image:"napari.types.ImageData", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._vary import vary
    image = vary(input_image=input_image, image_size=image_size, num_images=num_images)

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the vary function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image
    

@register_function(menu="Generate > Replace masked region (DALL-E 2, OpenAI, Darth-D)",
                   image_size={"choices": [256, 512, 1024]})
def replace_gui(input_image:"napari.types.ImageData", mask:"napari.types.LabelsData", prompt:str = "A similar pattern like in the rest of the image", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._replace import replace
    image = replace(input_image=input_image, mask=mask, prompt=prompt, image_size=image_size, num_images=num_images)

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image
    


@register_function(menu="Generate > Replace entire image (DALL-E 2, OpenAI, Darth-D)",
                   image_size={"choices": [256, 512, 1024]})
def replace_entire_image_gui(input_image:"napari.types.ImageData", prompt:str = "A similar pattern like in the rest of the image", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._replace import replace
    image = replace(input_image=input_image, mask=None, prompt=prompt, image_size=image_size, num_images=num_images)

    try:
        from napari.utils.notifications import show_warning
        show_warning("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    except:
        pass

    return image
