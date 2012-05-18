import datetime

def plus_one(date_str):
    '''this method takes a date as a string in format "YYYY-MM-DD".
        it just takes one param, a string of the date'''
    
    date_elements = date_str.split('-') #split the date to subsections
    #get a datetime object based on input string
    init_date = datetime.date(int(date_elements[0]),int(date_elements[1]),int(date_elements[2]))
    #use the datetime timedelta to logically add a day
    adjusted_date = init_date + datetime.timedelta(days=1)
    #join and return
    return '-'.join([str(adjusted_date.year),str(adjusted_date.month),str(adjusted_date.day)])
