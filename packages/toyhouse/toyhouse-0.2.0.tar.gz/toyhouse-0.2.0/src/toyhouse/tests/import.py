# Reminders: Build the package using 
# py -m build
# py -m pip install -e .
# The dot shows that it's referring to the current file.


import toyhouse
session = toyhouse.Session("ceruloryx", "Winterwatcher566")
session.auth()
u = (toyhouse.User(session, "sema_lives")).favs
def user_comparison(m, u):
    li = [(mine[0], yours[3]) for mine in m for yours in u if mine[1] == yours[1]]
    return li

def folder_filter(id):
    return([i for i in u if str(id) in i[3]])

print(u)