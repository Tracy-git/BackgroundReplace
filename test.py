from PIL import Image,ImageDraw

def Gradient_color(bg_1,bg_2,size):
    width,height = size
    randint = Image.new(mode = 'RGB',size = (width,height),color = bg_1)
    draw = ImageDraw.Draw(randint)
    step_r = (bg_2[0] - bg_1[0]) / height
    step_g = (bg_2[1] - bg_1[1]) / height
    step_b = (bg_2[2] - bg_1[2]) / height
    for y in range(0,height):
        bg_r = round(bg_1[0] + step_r * y)
        bg_g = round(bg_1[1] + step_g * y)
        bg_b = round(bg_1[2] + step_b * y)
        for x in range(0, width):
            draw.point((x, y), fill=(bg_r, bg_g, bg_b))
    return randint