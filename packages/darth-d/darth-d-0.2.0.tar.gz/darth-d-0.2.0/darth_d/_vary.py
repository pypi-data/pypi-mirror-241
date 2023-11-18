from stackview import jupyter_displayable_output

@jupyter_displayable_output(library_name='darth-d', help_url='https://github.com/haesleinhuepf/darth-d')
def vary(input_image, image_size:int=256, num_images:int = 1):
    """Varies an image using OpenAI's DALL-E 2.

    Parameters
    ----------
    input_image: 2D image, potentially RGB
    image_size: int, optional (only 256, 512, 1024 allowed)
    num_images: int, optional

    See Also
    --------
    https://platform.openai.com/docs/guides/images/variations

    Returns
    -------
    single 2D image or 3D image with the first dimension = num_images
    """
    from openai import OpenAI
    from ._utilities import numpy_to_bytestream
    from ._utilities import images_from_url_responses
    
    from stackview._image_widget import _img_to_rgb
    from warnings import warn

    warn("Using the replace function on scientific images could be seen as scientific misconduct. Handle this function with care.")
    client = OpenAI()

    response = client.images.create_variation(
      image=numpy_to_bytestream(_img_to_rgb(input_image)),
      n=num_images,
      size=f"{image_size}x{image_size}"
    )

    # bring result in right format
    return images_from_url_responses(response, input_image.shape)
    