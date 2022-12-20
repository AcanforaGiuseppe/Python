import sys
import pngDecoder as pngDec
from PIL import Image, ImageDraw


def run():
    decoder = pngDec.PngDecoder()
    for index, arg in enumerate(sys.argv[1:]):
        try:
            data, width, height = decoder.decode(arg)
            draw_image(data, width, height)
        except pngDec.PngDecoder.InvalidSignatureException as ex:
            print(ex.message)
        except FileNotFoundError as ex:
            print(f"No such file: {arg}")


def draw_image(raw_data, width, height):
    image = Image.frombytes("RGBA", (width, height), raw_data)
    draw = ImageDraw.Draw(image)
    image.show()


if __name__ == "__main__":
    run()
