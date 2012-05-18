'''this script holds the vacation util class'''
from gdata.apps.emailsettings.client import EmailSettingsClient
from getpass import getpass, getuser

#this will be different depending where module is executed from
try:
    from vacation.date_adjust import plus_one
except Exception, err:
    from date_adjust import plus_one

class vacation_util():
    '''this class is the utility to update users\' vacation responder in email settings'''

    def __init__(self):
        '''initializes the client object with proper auth credentials. Prompts the user for
            their credens.'''
        #initialize the client
        self.client = EmailSettingsClient('pdx.edu')
        username = getuser()

        proceed = raw_input('user: ' + username + ' OK? [press enter or enter username]\n\t:')
        if not proceed == '':
            username = proceed

        password = getpass('password:\n\t:')

        authed = False

        while not authed:
            try:
                self.client.ClientLogin(username+'@pdx.edu',password,'')
                authed = True
            except Exception, err:
                print '\ncouldn\'t authenticate w/ credens: \n\t'  + \
                        'username: ' + username + '@pdx.edu\n\t' + \
                        'password: ' + password + '\n'+\
                        'err: ' + str(err) + \
                        '\nPlease try again.\n'
                username = raw_input('\nusername:\n\t')
                password = getpass('\npassword:')

    def responder_off(self,user):
        '''this method turns the vacation responder off for a given user.
            user: the username of the account for which you would like to turn off the vacation
                response.'''
        try:
            self.client.UpdateVacation(username=user,enable=False)
        except Exception, err:
            print 'error disabling vacation responder for user: ' + str(user)
            print str(err)

    def set_responder(self,user,resp_subject,resp_message,start,end,just_contacts,just_domain):
        '''this method takes all the params to set the user\'s vacation response to be sent to everyone:
              user: the username of the acct whose vacation response you would like to set
              resp_subject: the subject line for the response email
              resp_message: the message body of the response email
              start: the start date of the vacation
              end: the end date of the vacation
              just_contacts: boolean; should the vacation responder just be sent to existing contacts
              just_domain: boolean; should the vacation responder just be sent to other @pdx.edu
                  addresses.'''
        try:
            self.client.UpdateVacation(username=user,enable=True,subject=resp_subject,message=resp_message,
                start_date=plus_one(start),end_date=plus_one(end),contacts_only=just_contacts,domain_only=just_domain)
        except Exception, err:
            print 'error setting vacation responder for user: ' + str(user)
            print str(err)

    def set_responder_everyone(self,user,resp_subject,resp_message,start,end):
        '''this method takes the params to set the user\'s vacation response to be sent to everyone:
              user: the username of the acct whose vacation response you would like to set
              resp_subject: the subject line for the response email
              resp_message: the message body of the response email
              start: the start date of the vacation
              end: the end date of the vacation'''
        try:
            self.client.UpdateVacation(username=user,enable=True,subject=resp_subject,message=resp_message,
                start_date=plus_one(start),end_date=plus_one(end),contacts_only=False,domain_only=False)
        except Exception, err:
            print 'error setting vacation responder for user: ' + str(user)
            print str(err)
