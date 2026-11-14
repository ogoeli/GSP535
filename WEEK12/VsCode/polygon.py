def calculateArea(coordlist): 
    np = len(coordlist) 
    if np <= 2: 
        return 0.0 
     
    if coordlist[np-1] != coordlist[0]: 
        coordlist.append(coordlist[0]) 
        np = len(coordlist) 
         
    p1, p2 = None, None 
    A = 0.0 
    for p2 in coordlist: 
        if p1 != None: 
            A += (p2[1] + p1[1]) * (p2[0] - p1[0]) 
        p1 = p2 
    area = abs(A / 2) 
    return area 
 
if __name__ == "__main__":         # testing code 
    # create a list of [x, y] coordinates of a polygon 
    vlist = [[0, 0], [0, 1], [1, 1], [1, 0], [0.5, 0.5], [0, 0]] 
    area = calculateArea(vlist)    # calls the function to calculate area 
#print(area) 
