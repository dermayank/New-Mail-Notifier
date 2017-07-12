import time
import notify2
from recent_mail import readmail,auth

# path to notification window icon
ICON_PATH = "/home/mayank/Downloads/new_mail_notifier/gmail_icon.png"

feeds = auth();
entries,mails_count = readmail(feeds)

# initialise the d-bus connection
notify2.init("News Notifier")
# create Notification object
n = notify2.Notification(None, icon = ICON_PATH)
# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)
# set timeout for a notification
n.set_timeout(10000)

n.update("You have %s new mails"%mails_count);
n.show()
time.sleep(4)

for i in entries:
    # update notification data for Notification object 
    n.update(i,entries[i]);
    # show notification on screen
    n.show()
    # short delay between notifications
    time.sleep(15)

print "done";