#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    import itertools
    ages = list(itertools.chain(*ages))
    predictions = list(itertools.chain(*predictions))
    net_worths = list(itertools.chain(*net_worths))
    cleaned_data = []
    i = 0
    
    ### your code goes here
    while i < 90:
        cleaned_data.append((ages[i],net_worths[i],abs(predictions[i] - net_worths[i])))
        i = i + 1
    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])
    
    
    final = []
    i = 0
    while i < 81:
        final.append(cleaned_data[i])
        i = i + 1
    print len(final)
    return final

