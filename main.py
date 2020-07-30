#Function_1
### START FUNCTION 1
def dictionary_of_metrics(items):
    """A function that calculates the dictionary of metrics including mean,
    median, standard deviation, variance, minimum value, and a maximum value from a list
    """
    mean = np.mean(items).round(2)
    median = np.median(items).round(2)
    std = np.std(items, ddof=1).round(2)
    var = np.var(items, ddof=1).round(2)
    min = np.min(items).round(2)
    max = np.max(items).round(2)
 
    
    #dictionary of metrics
    dict = {'mean':mean, 'median':median, 'std':std, 'var':var, 'min':min, 'max':max, }
    
    
    return  dict

### END FUNCTION



#Function_2



#Function_3



#Function_4


d
#Function_5




#Function_6




#Function_7