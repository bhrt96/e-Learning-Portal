#!/Python27/python

import cgi
import MySQLdb

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>'

form=cgi.FieldStorage()
subject ="daa"#form.getvalue('dropdown')

db = MySQLdb.connect('localhost','root','','quiz')  # Your DB details here
cursor = db.cursor()

sql = "select question,optionA,optionB,optionC,optionD from questionbank where subject='%s'" % (subject)
cursor.execute(sql)
var = cursor.fetchall()
j=cursor.rowcount
k=1


for i in var:	
	print """<table>                                                                                                 														
			<tr>Ques:%d &nbsp
			<form action="/cgi-bin/result.py" method="post">
			%s<br>	
			<input type="radio" name="q[%d]" value="a">%s 
			<input type="radio" name="q[%d]" value="b">%s 
			<input type="radio" name="q[%d]" value="c">%s 
			<input type="radio" name="q[%d]" value="d">%s
			</tr></table>""" % (k,i[0],k,i[1],k,i[2],k,i[3],k,i[4])																																																																													
	print '<br>'
	k=k+1
print """<input type="submit" value="submit"></form>"""

print'</body>'
print'</html>'