def boxBlur(image):
    box = []
    for i in range(1,len(image)-1):
        row = []
        for j in range(1,len(image[0])-1):
            copy = [image[k][l] for k in (i-1,i,i+1) for l in (j-1,j,j+1)]
            row.append(sum(copy)//9) 
        box.append(row)
    return box
