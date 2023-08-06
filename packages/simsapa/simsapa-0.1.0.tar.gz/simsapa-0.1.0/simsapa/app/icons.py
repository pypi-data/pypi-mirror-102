import os.path
import sys
import PIL  # type: ignore
from PIL import Image, ImageOps
import io
import base64
import PySimpleGUI as sg  # type: ignore
from distutils.sysconfig import get_python_lib


def icon(name: str, size: int = 24, invert=False):
    png_dir = os.path.join('simsapa', 'assets', 'icons', 'png')

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        png_dir = os.path.join(sys._MEIPASS, png_dir)

    elif not os.path.exists(png_dir):
        site_packages_dir = get_python_lib()
        png_dir = os.path.join(site_packages_dir, png_dir)

    path = os.path.join(png_dir, f"{name}_24px.png")
    if not os.path.exists(path):
        path = sg.DEFAULT_BASE64_ICON

    if size == 24:
        data = convert_to_bytes(path, resize=None, invert=invert)
    else:
        data = convert_to_bytes(path, resize=(size, size), invert=invert)

    return data


def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    """
    From PySimpleGUI/DemoPrograms/Demo_PIL_Use.py
    """
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


def convert_to_bytes(file_or_bytes, resize=None, fill=False, invert=False):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :param fill: If True then the image is filled/padded so that the image is not distorted
    :type fill: (bool)
    :return: (bytes) a byte-string object
    :rtype: (bytes)

    Based on PySimpleGUI/DemoPrograms/Demo_PIL_Use.py
    """
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception:  # as e
            # print(e)
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    if invert:
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            rgb_image = Image.merge('RGB', (r, g, b))

            inverted_image = PIL.ImageOps.invert(rgb_image)

            r2, g2, b2 = inverted_image.split()

            img = Image.merge('RGBA', (r2, g2, b2, a))
        else:
            img = ImageOps.invert(img)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.ANTIALIAS)
    if fill:
        if resize is not None:
            img = make_square(img, resize[0])
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

