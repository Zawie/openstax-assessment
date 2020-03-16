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
    xmldoc = minidom.parse(file_name)
    greetings = list()
    for greeting_tag in xmldoc.getElementsByTagName("greeting"):
        print(greeting_tag)

exclaim(("hello","world"))
getGreetings("greetings.xml")
