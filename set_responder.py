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
just_contacts = raw_input(  'only send to existing contacts (y/n)?')
just_domain   = raw_input('only send to addresses @ pdx.edu (y/n)?')

if just_contacts.startswith('y') or (just_contacts.lower() == 'true'):
    just_contacts = True
else:
    just_contacts = False

if just_domain.startswith('y')   or (just_domain.lower()   == 'true'):
    just_domain = True
else:
    just_domain = False

try:
    v.set_responder(username,subject,response,start_date,end_date,
        just_contacts,just_domain)
    print '\nSuccess.'
except Exception, err:
    print '\nCouldn\'t set vacation responder.'
    print 'err: ' + str(err)
