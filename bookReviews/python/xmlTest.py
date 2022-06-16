import xml.dom.minidom

def main():
   #use parse() function to load XML file
   doc = xml.dom.minidom.parse("/Users/krush/git/kml/bookReviews/PaulBooksReadButNotReviewed.xml");

   #print out document
   print (doc.nodeName)
   #print (doc.firstChild.tagName)

#if __name__ == “__main__”:
main();
