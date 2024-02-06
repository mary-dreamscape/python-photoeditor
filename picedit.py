import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math


def change_brightness(image, value):
    newimage = image.copy()
    
    for x in range(len(image)):
        for y in range(len(image[x])):
            R = int(image[x][y][0] + value)
            G = int(image[x][y][1] + value)
            B = int(image[x][y][2] + value)
            
            if R < 0:
                newimage[x][y][0] = 0
            elif R > 255:
                newimage[x][y][0] = 255
            else:
                newimage[x][y][0] = R
            if G < 0:
                newimage[x][y][1] = 0
            elif G > 255:
                newimage[x][y][1] = 255
            else:
                newimage[x][y][1] = G
            if B < 0:
                newimage[x][y][2] = 0
            elif B > 255:
                newimage[x][y][2] = 255
            else:
                newimage[x][y][2] = B

    return newimage
  
def change_contrast(image, value):
    newimage = image.copy()
    F = (259*(value + 255))/(255*(259 - value))
    
    for x in range(len(image)):
        for y in range(len(image[x])):
            R = int(F * (image[x][y][0] - 128) + 128)
            G = int(F * (image[x][y][1] - 128) + 128)
            B = int(F * (image[x][y][2] - 128) + 128)
            if R < 0:
                newimage[x][y][0] = 0
            elif R > 255:
                newimage[x][y][0] = 255
            else:
                newimage[x][y][0] = R
            if G < 0:
                newimage[x][y][1] = 0
            elif G > 255:
                newimage[x][y][1] = 255
            else:
                newimage[x][y][1] = G
            if B < 0:
                newimage[x][y][2] = 0
            elif B > 255:
                newimage[x][y][2] = 255
            else:
                newimage[x][y][2] = B
    return newimage

def grayscale(image):
    newimage = image.copy()
    for x in range(len(image)):
        for y in range(len(image[x])):
            gray = int(0.3 * image[x][y][0] + 0.59 * image[x][y][1] + 0.11 * image[x][y][2])
            newimage[x][y][0] = gray
            newimage[x][y][1] = gray
            newimage[x][y][2] = gray
    return newimage


def blur_effect(image):
    newimage = image.copy()
    x = 2
    y = 2
    while x < len(image):
        while y < len(image[0]):
            R = 0.0625*image[x-2][y-2][0] + 0.125*image[x-2][y-1][0] + 0.0625*image[x-2][y][0] + 0.125*image[x-1][y-2][0] + 0.25*image[x-1][y-1][0] + 0.125*image[x-1][y][0] + 0.0625*image[x][y-2][0] + 0.125*image[x][y-1][0] + 0.0625*image[x][y][0]
            G = 0.0625*image[x-2][y-2][1] + 0.125*image[x-2][y-1][1] + 0.0625*image[x-2][y][1] + 0.125*image[x-1][y-2][1] + 0.25*image[x-1][y-1][1] + 0.125*image[x-1][y][1] + 0.0625*image[x][y-2][1] + 0.125*image[x][y-1][1] + 0.0625*image[x][y][1]
            B = 0.0625*image[x-2][y-2][2] + 0.125*image[x-2][y-1][2] + 0.0625*image[x-2][y][2] + 0.125*image[x-1][y-2][2] + 0.25*image[x-1][y-1][2] + 0.125*image[x-1][y][2] + 0.0625*image[x][y-2][2] + 0.125*image[x][y-1][2] + 0.0625*image[x][y][2]
            newimage[x-1][y-1][0] = int(R)
            newimage[x-1][y-1][1] = int(G)
            newimage[x-1][y-1][2] = int(B)

            y=y+1
        x=x+1
        y=2
    return newimage

def edge_detection(image):
    newimage = image.copy()
    
    x = 2
    y = 2
    while x < len(image):
        while y < len(image[0]):
            R = ((-1)*image[x-2][y-2][0] + (-1)*image[x-2][y-1][0] + (-1)*image[x-2][y][0] + (-1)*image[x-1][y-2][0] + 8*image[x-1][y-1][0] + (-1)*image[x-1][y][0] + (-1)*image[x][y-2][0] + (-1)*image[x][y-1][0] + (-1)*image[x][y][0]) +128
            if R < 0:
                newimage[x-1][y-1][0] = 0
            elif R > 255:
                newimage[x-1][y-1][0] = 255
            else:
                newimage[x-1][y-1][0] = R
            G = ((-1)*image[x-2][y-2][1] + (-1)*image[x-2][y-1][1] + (-1)*image[x-2][y][1] + (-1)*image[x-1][y-2][1] + 8*image[x-1][y-1][1] + (-1)*image[x-1][y][1] + (-1)*image[x][y-2][1] + (-1)*image[x][y-1][1] + (-1)*image[x][y][1]) +128
            if G < 0:
                newimage[x-1][y-1][1] = 0
            elif G > 255:
                newimage[x-1][y-1][1] = 255
            else:
                newimage[x-1][y-1][1] = G
            B = ((-1)*image[x-2][y-2][2] + (-1)*image[x-2][y-1][2] + (-1)*image[x-2][y][2] + (-1)*image[x-1][y-2][2] + 8*image[x-1][y-1][2] + (-1)*image[x-1][y][2] + (-1)*image[x][y-2][2] + (-1)*image[x][y-1][2] + (-1)*image[x][y][2]) +128    
            if B < 0:
               newimage[x-1][y-1][2] = 0
            elif B > 255:
               newimage[x-1][y-1][2] = 255
            else:
               newimage[x-1][y-1][2] = B
            y=y+1
        x=x+1
        y=2

    return newimage

def embossed(image):
    newimage = image.copy()
    
    x = 2
    y = 2

    while x < len(image):
        while y < len(image[0]):
            R = (-1)*image[x-2][y-2][0] + (-1)*image[x-2][y-1][0] + 0*image[x-2][y][0] + (-1)*image[x-1][y-2][0] + 0*image[x-1][y-1][0] + 1*image[x-1][y][0] + 0*image[x][y-2][0] + 1*image[x][y-1][0] + 1*image[x][y][0]
            G = (-1)*image[x-2][y-2][1] + (-1)*image[x-2][y-1][1] + 0*image[x-2][y][1] + (-1)*image[x-1][y-2][1] + 0*image[x-1][y-1][1] + 1*image[x-1][y][1] + 0*image[x][y-2][1] + 1*image[x][y-1][1] + 1*image[x][y][1]
            B = (-1)*image[x-2][y-2][2] + (-1)*image[x-2][y-1][2] + 0*image[x-2][y][2] + (-1)*image[x-1][y-2][2] + 0*image[x-1][y-1][2] + 1*image[x-1][y][2] + 0*image[x][y-2][2] + 1*image[x][y-1][2] + 1*image[x][y][2]

            newimage[x-1][y-1][0] = int(R) + 128
            newimage[x-1][y-1][1] = int(G) + 128
            newimage[x-1][y-1][2] = int(B) + 128
            
            if newimage[x-1][y-1][0] < 0:
                newimage[x-1][y-1][0] = 0
            elif newimage[x-1][y-1][0] > 255:
                newimage[x-1][y-1][0] = 255
            if newimage[x-1][y-1][1] < 0:
                newimage[x-1][y-1][1] = 0
            elif newimage[x-1][y-1][1] > 255:
                newimage[x-1][y-1][1] = 255
            if newimage[x-1][y-1][2] < 0:
                newimage[x-1][y-1][2] = 0
            elif newimage[x-1][y-1][2] > 255:
                newimage[x-1][y-1][2] = 255

            y=y+1
        x=x+1
        y=2

    return newimage

def rectangle_select(image, x, y):
    (toprow, topcol) = x
    (bottomrow, bottomcol) = y
    mask = np.zeros((len(image), len(image[0])))
    row = toprow
    col = topcol
    while row < bottomrow+1:
        while col < bottomcol+1:
            mask[row][col] = 1
            col = col + 1
        row = row + 1
        col = topcol
           
    return mask # to be removed when filling this function

def magic_wand_select(image, x, thres):
    (row, col) = x
    mask = np.zeros((len(image), len(image[0])))
    mask[row][col] = 1
    selected = [x]
    checked = [x]
    
    # #check for top neighbour
    # if row-1 >= 0:
    #     r = (image[row][col][0] + image[row-1][col][0])/2
    #     diffR = image[row][col][0] - image[row-1][col][0]
    #     diffG = image[row][col][1] - image[row-1][col][1]
    #     diffB = image[row][col][2] - image[row-1][col][2]
    #     dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
    #     if dist <= thres:
    #         selected.append((row-1,col))
    #         checked.append((row-1,col))
    #         mask[row-1][col] = 1
        
    # #check for bottom neighbour
    # if row+1 < len(image):
    #     r = (image[row][col][0] + image[row+1][col][0])/2
    #     diffR = image[row][col][0] - image[row+1][col][0]
    #     diffG = image[row][col][1] - image[row+1][col][1]
    #     diffB = image[row][col][2] - image[row+1][col][2]
    #     dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
    #     if dist <= thres:
    #         selected.append((row+1,col))
    #         checked.append((row+1,col))
    #         mask[row+1][col] = 1

    # #check for left neighbour
    # if col-1 >= 0:
    #     r = (image[row][col][0] + image[row][col-1][0])/2
    #     diffR = image[row][col][0] - image[row][col-1][0]
    #     diffG = image[row][col][1] - image[row][col-1][1]
    #     diffB = image[row][col][2] - image[row][col-1][2]
    #     dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
    #     if dist <= thres:
    #         selected.append((row,col-1))
    #         checked.append((row,col-1))
    #         mask[row][col-1] = 1
        
    # #check for right neighbour
    # if col+1 < len(image[0]):
    #     r = (image[row][col][0] + image[row][col+1][0])/2
    #     diffR = image[row][col][0] - image[row][col+1][0]
    #     diffG = image[row][col][1] - image[row][col+1][1]
    #     diffB = image[row][col][2] - image[row][col+1][2]
    #     dist = math.sqrt((2+(r/256))*(diffR**2)+4*(diffG**2)+(2+((255-r)/256))*(diffB**2))
    #     if dist <= thres:
    #         selected.append((row,col+1))
    #         checked.append((row,col+1))
    #         mask[row][col+1] = 1
            

    while len(checked) > 0:
        newrow = checked[0][0]
        newcol = checked[0][1]
        
        #check for top neighbour
        if (newrow-1,newcol) not in selected:
            if newrow-1 >= 0:
                r = (image[row][col][0] + image[newrow-1][newcol][0])/2
                diffR = image[row][col][0] - image[newrow-1][newcol][0]
                diffG = image[row][col][1] - image[newrow-1][newcol][1]
                diffB = image[row][col][2] - image[newrow-1][newcol][2]
                dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
                if dist <= thres:
                    selected.append((newrow-1,newcol))
                    checked.append((newrow-1,newcol))
                    mask[newrow-1][newcol] = 1
                    
        #check for bottom neighbour
        if (newrow+1,newcol) not in selected:
            if newrow+1 < len(image):
                r = (image[row][col][0] + image[newrow+1][newcol][0])/2
                diffR = image[row][col][0] - image[newrow+1][newcol][0]
                diffG = image[row][col][1] - image[newrow+1][newcol][1]
                diffB = image[row][col][2] - image[newrow+1][newcol][2]
                dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
                if dist <= thres:
                    selected.append((newrow+1,newcol))
                    checked.append((newrow+1,newcol))
                    mask[newrow+1][newcol] = 1
        
        #check for left neighbour
        if (newrow,newcol-1) not in selected:
            if newcol-1 >= 0:
                r = (image[row][col][0] + image[newrow][newcol-1][0])/2
                diffR = image[row][col][0] - image[newrow][newcol-1][0]
                diffG = image[row][col][1] - image[newrow][newcol-1][1]
                diffB = image[row][col][2] - image[newrow][newcol-1][2]
                dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
                if dist <= thres:
                    selected.append((newrow,newcol-1))        
                    checked.append((newrow,newcol-1))
                    mask[newrow][newcol-1] = 1
                    
        #check for right neighbour
        if (newrow, newcol+1) not in selected:
            if newcol+1 < len(image[0]):
                r = (image[row][col][0] + image[newrow][newcol+1][0])/2
                diffR = image[row][col][0] - image[newrow][newcol+1][0]
                diffG = image[row][col][1] - image[newrow][newcol+1][1]
                diffB = image[row][col][2] - image[newrow][newcol+1][2]
                dist = math.sqrt((2+r/256)*(diffR**2)+4*(diffG**2)+(2+(255-r)/256)*(diffB**2))
                if dist <= thres:
                    selected.append((newrow,newcol+1))
                    checked.append((newrow,newcol+1))
                    mask[newrow][newcol+1] = 1
        
        checked.pop(0)
    
        
    return mask

def compute_edge(mask):           
    rsize, csize = len(mask), len(mask[0]) 
    edge = np.zeros((rsize,csize))
    if np.all((mask == 1)): return edge        
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c]!=0:
                if r==0 or c==0 or r==len(mask)-1 or c==len(mask[0])-1:
                    edge[r][c]=1
                    continue
                
                is_edge = False                
                for var in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0<=r_temp<rsize and 0<=c_temp<csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break
    
                if is_edge == True:
                    edge[r][c]=1
            
    return edge

def save_image(filename, image):
    img = image.astype(np.uint8)
    mpimg.imsave(filename,img)

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    mask = np.ones((len(img),len(img[0]))) # create a mask full of "1" of the same size of the laoded image
    img = img.astype(np.int32)
    return img, mask

def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0]=255
                tmp_img[r][c][1]=0
                tmp_img[r][c][2]=0
 
    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))

def menu():
    img = mask = np.array([])
    while True:
        print("What do you want to do?")
        print("e - exit")
        print("l - load a picture")
        choice = str(input("Your choice: "))
        if choice == "e":
            print("Program is exiting.")
            break;
        elif choice == "l":
            while True:
                try:
                    filename = str(input("Filename: "))
                    img = load_image(filename)[0]
                except FileNotFoundError:
                    print("File cannot be found. Please check if the file is in the same directory as this program file.")
                except AttributeError:
                    print("Please enter a filename.")
                else:
                    break;
            mask = load_image(filename)[1]
            display_image(img, mask)
            print("Image loaded!")
            break;    
        else:
            print("Invalid option. Please choose again.")
    if img.size != 0:
        while choice != "e":
            print("What do you want to do?")
            print("e - exit")
            print("l - load a picture")
            print("s - save the current picture")
            print("1 - adjust brightness")
            print("2 - apply contrast")
            print("3 - apply grayscale")
            print("4 - apply blur")
            print("5 - edge detection")
            print("6 - embossed")
            print("7 - rectangle select")
            print("8 - magic wand select")
            choice = str(input("Your choice: "))
            if choice == "e":
                print("Program is exiting.")
            elif choice == "l":
                while True:
                    try:
                        filename = str(input("Filename: "))
                        img = load_image(filename)[0]
                    except FileNotFoundError:
                        print("File cannot be found. Please check if the file is in the same directory as this program file.")
                    except AttributeError:
                        print("Please enter a filename.")
                    else:
                        break;
                mask = load_image(filename)[1]
                display_image(img, mask)
                print("Image loaded!")
            elif choice == "s":
                while True:
                    try:
                        filename = str(input("Filename (with .jpg or .png):"))
                        save_image(filename, img)
                        print("Image saved!")
                        break;
                    except ValueError:
                        print("Unknown file extension!")
            elif choice == "1":
                while True:
                    try:
                        value = int(input("Enter value for brightness (-255 to 255): "))
                        if value < -255 or value > 255:
                            print("Value must be between -255 and 255!")
                        else:
                            break;
                    except ValueError:
                        print("Input must be a value!")
                if np.array_equal(mask,load_image(filename)[1]):
                    img = change_brightness(img, value)
                    display_image(img, mask)
                else:
                    original = img.copy()
                    original = change_brightness(original, value)
                    for x in range(len(img)):
                        for y in range(len(img[0])):
                            if mask[x][y] != 0:
                                img[x][y][0] = original[x][y][0]
                                img[x][y][1] = original[x][y][1]
                                img[x][y][2] = original[x][y][2]
                    originalmask = load_image(filename)[1]
                    display_image(img, originalmask)
                    
                print("Brightness changed!")
            elif choice == "2":
                while True:
                    try:
                        value = int(input("Enter value for contrast (-255 to 255): "))
                        if value < -255 or value > 255:
                            print("Value must be between -255 and 255!")
                        else:
                            break;
                    except ValueError:
                        print("Input must be a value!")
                if np.array_equal(mask,load_image(filename)[1]):
                    img = change_contrast(img, value)
                    display_image(img, mask)
                else:
                    original = img.copy()
                    original = change_contrast(original, value)
                    for x in range(len(img)):
                        for y in range(len(img[0])):
                            if mask[x][y] != 0:
                                img[x][y][0] = original[x][y][0]
                                img[x][y][1] = original[x][y][1]
                                img[x][y][2] = original[x][y][2]
                    originalmask = load_image(filename)[1]
                    display_image(img, originalmask)
                print("Contrast changed!")
            elif choice == "3":
                if np.array_equal(mask,load_image(filename)[1]):
                    img = grayscale(img)
                    display_image(img, mask)
                else:
                    original = img.copy()
                    original = grayscale(original)
                    for x in range(len(img)):
                        for y in range(len(img[0])):
                            if mask[x][y] != 0:
                                img[x][y][0] = original[x][y][0]
                                img[x][y][1] = original[x][y][1]
                                img[x][y][2] = original[x][y][2]
                    originalmask = load_image(filename)[1]
                    display_image(img, originalmask)                    
                print("Applied grayscale effect!")
            elif choice == "4":
                if np.array_equal(mask,load_image(filename)[1]):
                    img = blur_effect(img)
                    display_image(img, mask)
                else:
                    original = img.copy()
                    original = blur_effect(original)
                    for x in range(len(img)):
                        for y in range(len(img[0])):
                            if mask[x][y] != 0:
                                img[x][y][0] = original[x][y][0]
                                img[x][y][1] = original[x][y][1]
                                img[x][y][2] = original[x][y][2]
                    originalmask = load_image(filename)[1]
                    display_image(img, originalmask)   
                print("Applied blurred effect!")
            elif choice == "5":
                if np.array_equal(mask,load_image(filename)[1]):
                    img = edge_detection(img)
                    display_image(img, mask)
                else:
                    original = img.copy()
                    original = edge_detection(original)
                    for x in range(len(img)):
                        for y in range(len(img[0])):
                            if mask[x][y] != 0:
                                img[x][y][0] = original[x][y][0]
                                img[x][y][1] = original[x][y][1]
                                img[x][y][2] = original[x][y][2]
                    originalmask = load_image(filename)[1]
                    display_image(img, originalmask)  
                print("Applied edge detection!")
            elif choice == "6":
                if np.array_equal(mask,load_image(filename)[1]):
                    img = embossed(img)
                    display_image(img, mask)
                else:
                    original = img.copy()
                    original = embossed(original)
                    for x in range(len(img)):
                        for y in range(len(img[0])):
                            if mask[x][y] != 0:
                                img[x][y][0] = original[x][y][0]
                                img[x][y][1] = original[x][y][1]
                                img[x][y][2] = original[x][y][2]
                    originalmask = load_image(filename)[1]
                    display_image(img, originalmask)  
                print("Applied embossed effect!")
            elif choice == "7":
                while True:
                    x = input("Enter the top left pixel position (row,col): ")
                    for i in x:
                        if i == "(":
                            x = x.replace("(", "")
                        if i == ")":
                            x = x.replace(")", "")
                    x = x.split(",")
                    try:
                        for i in x:
                            i = int(i)
                    except ValueError:
                        print("This is not a pixel position. It should be in (x,y) format.")
                        continue
                    else:
                        x = tuple(x)
                        
                    y = input("Enter the bottom right pixel position (row,col): ")
                    for i in y:
                        if i == "(":
                            y = y.replace("(", "")
                        if i == ")":
                            y = y.replace(")", "")
                    y = y.split(",")
                    try:
                        for i in y:
                            i = int(i)
                    except ValueError:
                        print("This is not a pixel position. It should be in (x,y) format.")
                        continue
                    else:
                        y = tuple(y)
                        
                    (rowx,colx) = x
                    (rowy,coly) = y
                    rowx,colx,rowy,coly = int(rowx),int(colx),int(rowy),int(coly)
                    if rowx < 0 or rowx >= len(img) or colx < 0 or colx >= len(img[0]):
                        print("The values are not inside the range of the image pixels!")
                    elif rowy < 0 or rowy >= len(img) or coly < 0 or coly >= len(img[0]):
                        print("The values are not inside the range of the image pixels!")
                    else:
                        break;
                x = (rowx,colx)
                y = (rowy,coly)

                mask = rectangle_select(img, x, y)  
                display_image(img, mask)
                print("Applied rectangle select!")
            elif choice == "8":
                while True:
                    x = input("Enter the pixel position (row,col): ")
                    for i in x:
                        if i == "(":
                            x = x.replace("(", "")
                        if i == ")":
                            x = x.replace(")", "")
                    x = x.split(",")
                    try:
                        for i in x:
                            i = int(i)
                    except ValueError:
                        print("This is not a pixel position. It should be in (x,y) format.")
                        continue
                    else:
                        x = tuple(x)
                        
                    (row,col) = x
                    row,col = int(row),int(col)
                    if row < 0 or row >= len(img) or col < 0 or col >= len(img[0]):
                        print("The values are not inside the range of the image pixels!")
                    else:
                        break;
                while True:
                    try:
                        thres = float(input("Enter the threshold value: "))
                    except ValueError:
                        print("Please input a value!")
                    else:
                        break;
                x = (row,col)
                mask = magic_wand_select(img, x, thres)
                display_image(img, mask)
            else:
                print("Invalid option. Please choose again.")
                
       
if __name__ == "__main__":
    menu()






