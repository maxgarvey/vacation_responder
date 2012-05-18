#! /usr/bin/python

try:
    from vacation.vacation_responder import vacation_util
except:
    from vacation_responder import vacation_util

v = vacation_util()

print '\nproperly authed.'

#the relevant data items
username      = raw_input(               '\nvacationer\'s username:')

try:
    v.responder_off(username)
    print '\nSuccess.'
except Exception, err:
    print '\nCouldn\'t set vacation responder.'
    print 'err: ' + str(err)
