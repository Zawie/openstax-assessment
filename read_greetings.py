#Adam Zawierucha
#OpenStax Internship Assessment
#March 15th 2020
from xml.dom import minidom

def exclaim(greeting):
    """
    Input: greeting (tuple): from xml
    Output: None
    Prints desired output
    """
    prefix = greeting[0]
    target = greeting[1]
    print("{}, {}!".format(prefix,target))

def getGreetings(file_name):
    """
    Input: filname_name (string): name of the final
    Output: a list of tuples, where each tuple is a greeting (prefix,target)
    """
    greetings = list()
    xmldoc = minidom.parse(file_name)
    root = xmldoc.documentElement
    #Loop through all elements of root
    for child in root.childNodes:
        #Check if child is a greeting element
        if child.localName == 'greeting':
            prefixes = child.getElementsByTagName("prefix")
            targets = child.getElementsByTagName("target")
            prefix = prefixes[0].firstChild.nodeValue
            target = targets[0].firstChild.nodeValue
            greetings.append((prefix,target))
    return greetings

for greeting in getGreetings("greetings.xml"):
    exclaim(greeting)
