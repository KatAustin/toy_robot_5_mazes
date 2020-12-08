#global obstacle list so that any function can call and alter its value
turtle_obstacles = []


def y_axis(x ,y , y1):
    """
    calls in global turtle_obstacles , as long as the starting y co-ordinate
    is a smaller int than y1 , it will append that obstacle tuple to the 
    obstacle list
    """
    global turtle_obstacles
    #start point of y will always be smaller than end point of y 
    #so it will always append the obstacle to the list
    while y < y1:
        #appending to list
        turtle_obstacles.append((x,y))
        
        y+=4


def x_axis(x, x1, y):
    """
    calls in global turtle_obstacles , as long as the starting y co-ordinate
    is a smaller int than y1 , it will append that obstacle tuple to the 
    obstacle list
    """
    
    global turtle_obstacles
    while x < x1:
        turtle_obstacles.append((x,y))
        x+=4


def get_obstacles():
    """
    This is its own function to make importing the maze obstacles smooth

    functions x_axis and y_axis are called for each hardcoded object ,these functions
    will then append the obstacles to the global "turtle_obstacles"
    """
    
    global turtle_obstacles
    
    #first arg : starting point on x axis in GUI grid
    #second arg: ending point on x axis on GUI grid
    #third arg : position wherex and y axis meet?


    x_axis(-100,-10,196)
    x_axis(10,96,196)
    x_axis(20,100,180)
    x_axis(-12,12,180)
    x_axis(-100,-20,180)
    x_axis(68,100,150)
    x_axis(-15,28,150)
    x_axis(-88,-56,150)
    x_axis(-100,92,126)
    x_axis(-68,72,100)
    x_axis(-30,44,60)
    x_axis(-100,-44,60)
    x_axis(-70,70,20)
    x_axis(-70,70,-20)
    x_axis(-30,44,-60)
    x_axis(-100,-44,-60)
    x_axis(-68,72,-100)
    x_axis(-100,92,-126)
    x_axis(68,100,-150)
    x_axis(-15,28,-150)
    x_axis(-88,-56,-150)
    x_axis(20,100,-180)
    x_axis(-12,12,-180)
    x_axis(-100,-20,-180)
    x_axis(-100,-10,-200)
    x_axis(10,96,-200)
    
    y_axis(-70,10,20)
    y_axis(66,10,20)
    y_axis(-70,-20,-10)
    y_axis(66,-20,-10)
    y_axis(-100,-190,162)
    y_axis(96,150,180)
    y_axis(96,-200,-150)
    y_axis(96,-150,130)
    y_axis(-100,180,196)
    y_axis(96,180,200)
    return turtle_obstacles


def is_position_blocked(pos_x, pos_y):
    """
    iterates through global obstacle list
    for x in range + 5
    for y in range + 5
    either x or y == the pos_x or pos_y , return true if blocked
    otherwise return false
    """

    for obs in turtle_obstacles:
        for x in range(obs[0], obs[0]+5):
            for y in range(obs[1], obs[1]+5):
                if pos_x == x and pos_y == y:
                    return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    if x1 == x2:
        y_cords = ([y1, y2])
        for loc in range(y_cords[0], (y_cords[1] + 1)):
            if is_position_blocked(x1, loc):
                return True
    elif y1 == y2:
        x_cords = sorted([x1, x2])
        for loc in range(x_cords[0], (x_cords[1] + 1)):
            if is_position_blocked(loc, y1):
                return True
    return False

    """
    Credits! 

    completed with pair programming assisstance from:
    @Mgillwald @jkokot @PandaGears @Rvandemerwe
    """