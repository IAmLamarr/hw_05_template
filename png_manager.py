import png
from copy import deepcopy

RGBAPixel = list[int, int, int, int]
PNGData = list[list[RGBAPixel]]


def read_data(filename: str) -> PNGData:
    reader = png.Reader(filename=filename)

    height, width, pixels_data, params = reader.asRGBA()

    data = []
    for scan in pixels_data:
        row = []
        pixel = []
        i = 0
        for value in scan:
            if i > 0 and i % 4 == 0:
                row.append(deepcopy(pixel))
                pixel = []
            pixel.append(value)
            i += 1
        row.append(deepcopy(pixel))
        data.append(deepcopy(row))

    return data


def write_data(pixel_data: PNGData, filename: str) -> None:
    write_pixel_data = []
    for row in pixel_data:
        row_data = []
        for pixel in row:
            row_data = [*row_data, *pixel]
        write_pixel_data.append(deepcopy(row_data))

    png.from_array(write_pixel_data, 'RGBA').save(filename)
