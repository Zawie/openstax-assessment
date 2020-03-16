#Adam Zawierucha
#OpenStax Internship Assessment
#March 15th 2020

from xml.dom import minidom
import sys

def exclaim(greeting):
    """
    Input: greeting (tuple): (prefix,target)
    Output: None
    Prints desired output
    """
    prefix = greeting[0]
    target = greeting[1]
    print("{}, {}!".format(prefix,target).title())

def getGreetings(file_name):
    """
    Input: filname_name (string): name of the file to parse
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

#Get arguments from Docker run command
args = sys.argv
if len(args) != 2:
    print("Invalid number of arguments passed!")
else:
    #Get file from arguments
    FILE_NAME = args[1]
    #Get and exlaim all the greetings
    for greeting in getGreetings(FILE_NAME):
        exclaim(greeting)
