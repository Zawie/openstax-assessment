#Adam Zawierucha
#OpenStax Internship Assessment
#March 15th 2020

from xml.dom import minidom
import sys

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
    Input: filname_name (string): name of the file
    Output: a list of tuples, where each tuple is a greeting (prefix,target)
    """
    greetings = list()
    xmldoc = minidom.parse(file_name)
    root = xmldoc.documentElement
    #Loop through all elements of root
    for child in root.childNodes:
        #Check if child is a greeting element
        if child.localName == 'greeting':
            #get sub-elements
            prefixes = child.getElementsByTagName("prefix")
            targets = child.getElementsByTagName("target")
            #extract value from first instance of each element class
            prefix = prefixes[0].firstChild.nodeValue
            target = targets[0].firstChild.nodeValue
            #add tuple to greetings list
            greetings.append((prefix,target))
    return greetings

#Get file from docker command
FILE_NAME = sys.argv[1]

#Get and exlaim all the greetings
for greeting in getGreetings(FILE_NAME):
    exclaim(greeting)
