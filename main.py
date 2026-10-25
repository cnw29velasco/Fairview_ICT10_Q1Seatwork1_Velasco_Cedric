from pyscript import document, display


def add_name(e):

    first = document.getElementById('first').value  #first name
    last = document.getElementById('last').value    #last name
    full = first + ' ' + last + '(The newest member), ' #full name

    document.getElementById("output1").innerHTML = "" #clears the response after answering

    #list of all the members
    g10 = {"Logan Anaque, ", "Jacob Minguillo, ", "Gavin Ruiz, "}
    g9 = {"Robert Junior, ", "Boberto Junior, ", "Robertido Junior, "}
    g8 = {"Rick Grayson, ", "Bruce Wayne, ", "Clark Kent, "}  
    g7 = {"Wally West, ", "Barry Allen, ", "Oliver Queen, "}

    #combined the list of all the members
    all_members = g10.union(g9, g8, g7)
    all_members.add(full)

    #number of members
    combined_members = len(all_members)

    #the variable of the message
    message = full + ", you are officially a new member of ICT Club, joined by, "

    #it displays the message
    display(message + "".join(sorted(all_members)) + f" Amount of Members: {combined_members}", target = 'output1')



