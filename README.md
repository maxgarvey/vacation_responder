vacation_responder
==================

utility to turn on/off users' automated email responses while on vacation in the gdata system.

prerequisites are to have gdata 2.0.17 or later. they changed the number of params that
UpdateVacation takes. Now it's much better.

to use it, call one of the scripts in the top level directory, examples are set_responder
and, turn_off_response, & set_for_everyone.

they will start by authing you withe the pdx instance of gdata. Then, they will ask you for the
necessary params to do the given operation.

python will attempt to get your username from the current shell, but to use a different one,
just enter the alternate username at the first prompt. BTW, using some interpreters/IDE's on
the code can mess with the getpass function. For use in bpython, I had to use [Ctrl]+[Enter]
rather than just enter in order for the password to go through.

Further, I was using an account with superuser access. I'm not sure what exact roles/permissions
are needed to use the application. It might be very hard to set it up; like with the google calendar
api.

It looks like the incrementing of the date may not be necessary... but I'm going to leave it in.

Apparently, when gdata decrements the date by one day, it's because the vacation officially starts
at midnight (24:00) on the date indicated, rather than the start of the day. Although it seems that
for the end of the vacation, we might want the extra day. (If you indicate that the end of the vacation
as the day when you get back, this would mean the vacation message would continue through the whole day).
