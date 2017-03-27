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
        
        
def create_hollow(height, width, character):
    box = ""
    if height >= 1 and width >= 1:
        if height == 1: #height of one is just a line
            box += character*width
        else: #height of box is at least 2, make box
            if height == 2:
                box += (character*width) + '\n' + (character*width)
            else:
                for x in range(height):
                    if x == 0:
                        box += character * width + '\n'
                    elif x == height-1:
                        box += character * width + '\n'
                    else:
                        for y in range(width):
                            if y == 0:
                                box += character
                            elif y == width-1:
                                box += character + '\n'
                            else:
                                box += " "
    else:
        box = "Not a valid box height and/or width"

    return box
    
    
def main():
    create_box(3, 4, '*')
    create_hollow(3, 4, '*')

if __name__ == "__main__":
    main()
    

