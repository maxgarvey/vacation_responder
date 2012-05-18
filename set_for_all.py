#! /usr/bin/python

try:
    from vacation.vacation_responder import vacation_util
except:
    from vacation_responder import vacation_util

v = vacation_util()

print '\nproperly authed.'

#the relevant data items
username      = raw_input(               '\nvacationer\'s username:')
subject       = raw_input(       'subject line for response email:')
response      = raw_input(   'message body for the response email:')
start_date    = raw_input(               'start date (YYYY-MM-DD):')
end_date      = raw_input(                 'end date (YYYY-MM-DD):')

try:
    v.set_responder_everyone(username,subject,response,start_date,end_date)
    print '\nSuccess.'
except Exception, err:
    print '\nCouldn\'t set vacation responder.'
    print 'err: ' + str(err)
