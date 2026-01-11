import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import re
from contextlib import suppress
import matplotlib.pyplot as plt

ns ={'d': "http://docbook.org/ns/docbook"}

#Date cleanup patterns - assumes:
#     all years > 2000
#     if no day then day = 15
#     if no month, day then month = 9, day = 13
PATTERNS = [
        # 0) 1/12/2003 => 01/12/2003
        (re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})$'), '{0:0>2}/{1:0>2}/{2}'),
        # 1) 1/12/03 => 01/12/2003
        (re.compile(r'(\d{1,2})/(\d{1,2})/(\d{2})$'), '{0:0>2}/{1:0>2}/20{2}'),
        # 2) 1/03 => 01/15/2003
        (re.compile(r'(\d{1,2})/(\d{2})$'), '{0:0>2}/15/20{1}'),
        # 3) 1/2003 => 01/15/2003
        (re.compile(r'(\d{1,2})/(\d{4})$'), '{0:0>2}/15/{1}'),
        # 4) 2008 => 09/13/2008
        (re.compile(r'(\d)(\d)(\d)(\d)$'), '09/13/{0}{1}{2}{4}'),
        # 5) Spring 03 => 04/13/2003
        (re.compile(r'(Spring) (\d{2})$'), '04/13/20{1}'),
]

root1 = ET.parse('/Users/psk/Documents/git/family_history/bookReviews/PaulBookReviews_2001-2009.xml').getroot()
root2 = ET.parse('/Users/psk/Documents/git/family_history/bookReviews/PaulBookReviews_2010-2019.xml').getroot()
root3 = ET.parse('/Users/psk/Documents/git/family_history/bookReviews/PaulBookReviews_2020-.xml').getroot()

#Cleanup date formats
def cleanup(date):
    with suppress(ValueError):
        return str(int(date))

    for pattern, formatter in PATTERNS:
        match = pattern.match(date)
        if match is not None:
            return formatter.format(*match.groups())
    print("FIX = " + date)
    return "FIXME"

#Return Title, Author, Date and Grade from Book Review
#https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.pyplot.hist.html
def parseBookReview (root):
    year_book = []
    for row in root.findall('d:chapter/d:simplesect[@label="review"]', ns):       
        ti=row.find('./d:title/d:emphasis',ns)
        title= " ".join(ti.text.split())
        aut=row.find('./d:simplelist/d:member[1]/d:emphasis',ns)
        author=" ".join(aut.tail.split())
        dt=row.find('./d:simplelist/d:member[2]/d:emphasis',ns)
        date = cleanup(dt.tail.strip())
        #hack until I figure out why pattern match fails
        if len(date) == 4:
            date = "09/13/"+date
        grade=row.find('./d:simplelist/d:member[3]/d:emphasis',ns)
        book_tup = (title, author, date, grade.tail)
        year_book.append(book_tup)
    return year_book

#Display Books by Year
def visualizeBooksByYear(df, column_name='DateFinished', color='#494949', title='Number of Books Read by Year'):
    plt.figure(figsize=(10,5))
    plotFrame=df[column_name].groupby(df[column_name].dt.year).count()
    width=0.7
    x=np.arange(plotFrame.size)
    print(df[column_name].groupby(df[column_name].dt.year).count())
    ax1=(df[column_name].groupby(df[column_name].dt.year).count()).plot(kind="bar", color=color)
    ax1.set_facecolor('#eeeeee')
    ax1.set_xlabel("Year")
    ax1.set_ylabel("# Books Read")
    ax1.set_title(title)
    rects1=ax1.bar(x-width/2, plotFrame,label='Count')
    autolabel(rects1, ax1)
    plt.show()

    #labels=df[column_name].dt.year.drop_duplicates()
    
    
    print (plotFrame.size)
    print("Here")
    #labels=dates.drop_duplicates()                          
    #print (labels)
    
    #x=len(labels))
    fig, ax1=plt.subplots()
    rects1=ax1.bar(x-width/2, df[column_name].groupby(df[column_name].dt.year).count(), width, label='Books')
    ax1.set_ylabel('# Books')
    ax1.set_title('Number of Books Reviewed By Year')
    ax1.set_xticks(x)
    ax1.set_xticklabels(df[column_name].dt.year)
    ax1.legend()
    autolabel(rects1,ax1)
    fig.tight_layout()
    plt.show()

def autolabel(rects,ax1):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax1.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

#Display Count by Grade
def visualizeCountByGrade(grade_list, color='#494949', title='Number of Books Read by Year'):
    x, bins, patches = plt.hist(grade_list, bins=[0,1,2,3,4,5,6], histtype='bar', align='left', color=color)
    plt.xlim(0,6)
    plt.xlabel("Grade")
    plt.ylabel("# Books")
    plt.show()

aughts = parseBookReview(root1)
tens = parseBookReview(root2)
twenties = parseBookReview(root3)

frame1 = pd.DataFrame(data=aughts, columns=['Title','Author','DateFinished','Grade'])
frame2 = pd.DataFrame(data=tens, columns=['Title','Author','DateFinished','Grade'])
frame3 = pd.DataFrame(data=twenties, columns=['Title','Author','DateFinished','Grade'])
inter = pd.merge(frame1, frame2, how="outer")
final = pd.merge(inter, frame3, how="outer")

#Report on empty values
#print(np.where(pd.isnull(final)))

#convert_dict= {'Title': str, 'Author':str, 'Date Finished':str, 'Grade':int}
final.astype({'Title':str}).dtypes
final.astype({'Author':str}).dtypes
             
final.Grade = final.Grade.astype('int')
#print(final.dtypes)
#print (final["Grade"].mean())
#print (final.query("Grade > 0").mean())

#Convert Date Strings to Date
final['DateFinished']=pd.to_datetime(final['DateFinished'], format='%m/%d/%Y')
#print (final.query("Grade == 2"))
#print (final.query("DateFinished > '12/31/2019'"))
#print (final.query("DateFinished > '12/31/2018' and DateFinished < '01/01/2020'").count())

all_grades = final["Grade"].tolist()
#print(final.loc[100])

#visualizeCountByGrade(all_grades)
#print(final.shape)


#Get year from date and plot
visualizeBooksByYear(final)

