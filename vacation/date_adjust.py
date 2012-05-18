import datetime

def plus_one(date_str):
    '''this method takes a date as a string in format "YYYY-MM-DD".
        it just takes one param, a string of the date'''
    date_elements = date_str.split('-')
    init_date = datetime.date(int(date_elements[0]),int(date_elements[1]),int(date_elements[2]))
    try:
        #try incrementing the day
        adjusted_date = init_date.replace(day=init_date.day+1)
    except Exception, err:
        #if the date after incrementing the day falls in the next month, it will throw an
        #exception, so then we just set the month to the next month, and the day to the first
        adjusted_date = init_date.replace(day=1,month=init_date.month+1)
    return '-'.join([str(adjusted_date.year),str(adjusted_date.month),str(adjusted_date.day)])
