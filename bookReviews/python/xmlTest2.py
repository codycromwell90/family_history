from lxml import etree

tree = etree.parse('/Users/krush/git/kml/bookReviews/PaulBooksReadButNotReviewed.xml')
#r = tree.xpath('//d:entry', namespaces={'d': 'http://docbook.org/ns/docbook'})
#r2 = tree.xpath("//d:entry/colname[.='Title']/text()", namespaces={'d': 'http://docbook.org/ns/docbook'})
r3 = tree.xpath("//d:entry[@colname[.='Title']]/text()", namespaces={'d': 'http://docbook.org/ns/docbook'})

for title in r3:
   if (title != 'Title'):
      print(title)
#mydoc.findall("//d:entry/@xcolname[.='Title']")
