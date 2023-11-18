from stackview import jupyter_displayable_output

@jupyter_displayable_output(library_name='darth-d', help_url='https://github.com/haesleinhuepf/darth-d')
def create(prompt:str=None, image_size:int=256, num_images:int=1):
    """Create an image from scratch using OpenAI's DALL-E 2.

    Parameters
    ----------
    prompt: str, text explaining what the image should show
    image_size: int, optional (only 256, 512, 1024 allowed)
    num_images: int, optional

    See Also
    --------
    https://platform.openai.com/docs/guides/images/generations

    Returns
    -------
    single 2D image or 3D image with the first dimension = num_images
    """
    from openai import OpenAI
    from ._utilities import images_from_url_responses

    client = OpenAI()

    response = client.images.generate(
      prompt=prompt,
      n=num_images,
      size=f"{image_size}x{image_size}"
    )

    # bring result in right format
    return images_from_url_responses(response)
