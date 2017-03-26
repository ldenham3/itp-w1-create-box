"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ""
    if width >= 1 & height >= 1:
        for x in range(height):
            for y in range(width):
                box += character
            box += "\n"
        return box
    else:
        return "Need a valid width and height"

if __name__ == '__main__':
    create_box(3, 4, '*')
