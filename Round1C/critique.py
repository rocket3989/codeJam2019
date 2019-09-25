
"""
def delete_multi(c,idx): 
    popped_count = 0 
    for i in range(0,len(idx)): 
        pop_index = idx[i] - popped_count 
        c.pop(pop_index) 
        popped_count +=1 
    return c 


    This is very slow. 
    first you have to iterate through each index that you want to remove O(n)
    then for each of those, you pop an element out, which is also linear time (a new list has to be created)
    so this ends up taking O(n^2)
    avoid poping elements out of lists- if you are, use a different data structure

"""
T = int(input())


#for some reason you looped through all of the inputs, stored, then output. you do not need to do this- you can output at anytime
for i in range(T): #range function can be called with one var, 0 is implied 
    N = int(input()) 
    c = [] #give your variables more meaningful names
    #max_len = 0 you use this to determine how many itereations to use, but it is better to just check if you have won
    for j in range(N): 
        C = input() 
        c.append(C) 

    
    #output = '' strings are immutable in python, so a new string is made when you add elements
    output = []# much better to use an array


    #loop until break 
    index = 0 # posistion in arrays
    while True: 

        #if(len(c)==0): this check is not needed. you break if only one type was played last round

        #this_column= [] 
        #you are using this as a set, initialize a set
        this_column = set()

        counter = '' 
        
        # r_index, s_index, p_index = [],[],[] you store indicies, why not store the whole move
        r, s, p = [],[],[]



        #for k in range(0,len(c)):  This is a c style loop
            #series = c[k] 

        #if you need the index, use 
        #for i, series in enumerate(c):


        for series in c:
            ele = index % len(series) #this is only used once, could be compacted
            play = series[ele] 
            if(play=='R'): 
                #r_index.append(k) ah this is why you wanted the index
                r.append(series)
            elif(play=='P'): 
                p.append(series)
            elif(play=='S'): 
                s.append(series) 

            this_column.add(play) #add element to set
        
        # x = list(set(this_column)) 
            
       
       
        if(len(this_column)>2): 
            output = "IMPOSSIBLE"
            break 
        elif(len(this_column)==1): 
            if('R' in this_column): 
                counter = 'P' 
                # c = delete_multi(c,r_index) 
                # there is no need to delete these, you already won
            if('S' in this_column): 
                counter = 'R' 
            if('P' in this_column): 
                counter = 'S' 
            output.append(counter)
            # you won, so break out
            break
                
        else: 
            if(('R' in this_column) and ('S' in this_column)): 
                counter = 'R' 
                # c = delete_multi(c,s_index) 
                # instead of deleting unwanted el, why not just keep the ones we used
                c = r
            elif(('P' in this_column) and ('S' in this_column)): 
                counter = 'S' 
                c = s
            elif(('R' in this_column) and ('P' in this_column)): 
                counter = 'P' 
                c = p 

        output.append(counter) 
        index += 1 # move forawrd

    print("Case #%i: %s"%((i+1),''.join(output)))


