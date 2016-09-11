from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import NewPost
import getpass
import sys


site_choice = raw_input("""Which site do you want to update:
(Defaults to [1] Saluting Pigs)
[1] Saluting Pigs
[2] Adventures in Programming
[3] Quit
> """)

if site_choice == "3" or site_choice == "q":
    print "Goodbye"
    sys.exit()
elif site_choice == "2":
    siteURL = 'https://lashedblog.wordpress.com/xmlrpc.php'
else:
    site_choice = "1"
    siteURL = 'https://chewie23.wordpress.com/xmlrpc.php'
        
pw = getpass.getpass("Please type your password: ")
wp = Client(siteURL, 'Chewie23', pw)
print "Got Client"

#TODO:
#Need to functionalize the repeated code

while True:    
    if site_choice == "1":
        usr_choice = raw_input("""Please enter your category:
(Defaults to [1] 100 word stories)
[1] 100 word stories
[2] Long Form
[3] Quit
> """)
        if usr_choice == "3" or usr_choice.lower() == "q":
            print "Goodbye!"
            break
        elif usr_choice == "2":
            choice = "Long Form"
            title = raw_input("Enter a title for the Long Form story: ")
        else:
            usr_choice = "1"
            choice = "100 word stories"
            print "You chose [%s]" % usr_choice
    
            print """Accessing WPS.txt...
Please note that you can only use 'single quotes' for the file to be valid"""
        with open("WPS.txt", "r") as f:
            story = f.read()
        
            post = WordPressPost()
            post.title = title
            post.content = story
            post.terms_names = {
                'category': [choice]
            }
            print "Connecting..."
            post.id = wp.call(posts.NewPost(post))
            print "Posting..."
            post.post_status = 'publish'
            wp.call(posts.EditPost(post.id, post))
            print """Finished!
""" 
    elif site_choice == "2":
        usr_choice = raw_input("""Please enter your category:
(Defaults to [1] Opinion)
[1] Opinion
[2] C++
[3] Quit
> """)
        if usr_choice == "3" or usr_choice.lower() == "q":
            print "Goodbye!"
            break
        elif usr_choice == "2":
            choice = "C++"
        else:
            usr_choice = "1"
            choice = "Opinion"
        title = raw_input("Enter a title for the blog post: ")
        print "You chose [%s]" % usr_choice
    
        print """Accessing WPS.txt...
Please note that you can only use 'single quotes' for the file to be valid"""
        with open("WPS.txt", "r") as f:
            story = f.read()
        
            post = WordPressPost()
            post.title = title
            post.content = story
            post.terms_names = {
                'category': [choice]
            }
            print "Connecting..."
            post.id = wp.call(posts.NewPost(post))
            print "Posting..."
            post.post_status = 'publish'
            wp.call(posts.EditPost(post.id, post))
            print """Finished!
"""
        