from PIL import Image
im = Image.open('img.jpg')
width, height = im.size[0], im.size[1]
new_im = Image.new('RGB', (width, height))
new_pix = new_im.load()
pix = im.load()
for j in range(height):
    for i in range(width):
        r, g, b = pix[i, j]
        pix_used = 1
        if i > 0:
            t_r, t_g, t_b = pix[i-1, j]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if i < width-1:
            t_r, t_g, t_b = pix[i+1, j]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j > 0:
            t_r, t_g, t_b = pix[i, j-1]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j < height-1:
            t_r, t_g, t_b = pix[i, j+1]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if i > 0 and j > 0:
            t_r, t_g, t_b = pix[i-1, j-1]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if i < width-1 and j > 0:
            t_r, t_g, t_b = pix[i+1, j-1]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j > 0 and i > 0:
            t_r, t_g, t_b = pix[i-1, j-1]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j < height-1 and i < width-1:
            t_r, t_g, t_b = pix[i+1, j+1]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
            
        if i > 1:
            t_r, t_g, t_b = pix[i-2, j]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if i < width-2:
            t_r, t_g, t_b = pix[i+2, j]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j > 1:
            t_r, t_g, t_b = pix[i, j-2]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j < height-2:
            t_r, t_g, t_b = pix[i, j+2]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if i > 1 and j > 1:
            t_r, t_g, t_b = pix[i-2, j-2]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if i < width-2 and j > 1:
            t_r, t_g, t_b = pix[i+2, j-2]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j > 1 and i > 1:
            t_r, t_g, t_b = pix[i-2, j-2]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        if j < height-2 and i < width-2:
            t_r, t_g, t_b = pix[i+2, j+2]
            r, g, b = (t_r+r, t_g+g, t_b+b)
            pix_used += 1
        new_pix[i, j] = (int(r/pix_used), int(g/pix_used), int(b/pix_used))
new_im.save('new-img-2.png')
