import urllib2             # For BasicHTTPAuthentication
import feedparser         # For parsing the feed
from textwrap import wrap # For pretty printing assistance
import getpass

_URL = "https://mail.google.com/gmail/feed/atom"

def auth():
    user_name = raw_input("Please enter your email id:\n");
    user_password = getpass.getpass("Please enter your password:\n");
    
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='mail.google.com',
        uri='https://mail.google.com',
	    user = user_name,
        passwd = user_password
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    f = urllib2.urlopen(_URL)
    feed = f.read()
    return feed

def fill(text, width):
    '''A custom method to assist in pretty printing'''
    if len(text) < width:
        return text + ' '*(width-len(text))
    else:
        return text

def readmail(feed):
    
    entry = {} 
    
    atom = feedparser.parse(feed)

    print "Dear user you have %s new mails" % len(atom.entries)
    
    
    for i in xrange(len(atom.entries)):
        entry[fill(wrap(atom.entries[i].title)[0],55)]=fill(wrap(atom.entries[i].author)[0], 100);

    return entry,len(atom.entries);
    


#if __name__ == "__main__":
#    f = auth()  # Do auth and then get the feed

#    readmail(f) # Let the feed be chewed by feedparser
