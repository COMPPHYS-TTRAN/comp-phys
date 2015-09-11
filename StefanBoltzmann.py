import math 

#check this

def stefboltz (a, b, dy):
    
    answer = ((math.pi)**4.)/15.
    print 'running...'
    step_value(a, b, dy)
    mid_point(a, b, dy)
    find_area(a, b, dy)

def step_value(a, b, dy):
    a = float(a)
    b = float(b)
    dy = float(dy)
    
    n = (b-a)/dy
    w = (b-a)/n #n is arbitrary
    return w
    
def mid_point(a, b, dy): 
    w = step_value(a, b, dy)
    mdpoints = []
    y = a
   
    while y < b:
        mdpoints.append((2.0*y+w)/2)
        y += w
        return mdpoints
        return y
    
def find_area(a, b, dy):
    
    w = step_value(a, b, dy)
    mdpoints = []
    y = a
   
    while y < b:
        mdpoints.append((2.0*y+w)/2)
        y += w
        return mdpoints
        return y
    
    f_mdpoints = 0.0
    for y in mdpoints:
        f_mdpoints += (y**3)/((math.exp(y))-1)
        area = f_mdpoints*w
        if y == len(mdpoints)-2:
            prev_area = area
        frac_diff = (abs(area - prev_area)/area)*100
        return area 
        return frac_diff
    
    frac_error = (answer - area)*100
    return frac_error
    
    answer = ((math.pi)**4.)/15.
    
    if frac_diff < 1e-6:
        print 'The integral evaluated to within specified accuracy ', '{0:.7f}' .format(area) 
        print 'The upper limit of its fractional error is estimated to be: ', '{0:.7f}' .format(frac_diff)
        print 'The correct answer is ', '{4.1f}'.format(answer)
        print 'The actual fractional error is: ', '{0:7f}' .format(frac_error)
    else:
        stefboltz(a, b, dy)
        print 'number of steps: ', dy*100
        print 'dy = ', '{:4.1f}' .format(dy), ',', 'integral = ', prev_area
        print 'frac_diff = ', frac_diff
    
    
stefboltz (1, 100, 1)