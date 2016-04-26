#!/usr/bin/python

import cgi
import MySQLdb

print "Content-type:text/html\r\n\r\n"
print '<html>'


print '<head>'

#script for pie chart


print '</head>'

print '<body>'


db = MySQLdb.connect('localhost','root','1315','quiz', unix_socket="/opt/lampp/var/mysql/mysql.sock")
cursor = db.cursor()

form=cgi.FieldStorage()

k=3 #int(form.getvalue('rows'))


#inserting values in studentAnswer table from form
for i in range(1,k):
	sql="""insert into studentAnswer(studentId,questionId,answer) values (%d,%d,'%s')""" % (14,3,'a')#int(form.getvalue('qid[%d]'%i)) ,form.getvalue('q[%d]'%i))
	cursor.execute(sql)
	db.commit()	

#setting points to 4 for correct answer in studentAnswer table
sql2="""update studentAnswer as sa 
		join questionBank as qb on sa.questionId=qb.questionId and sa.answer=qb.answer
		set sa.points = %d """ % (4)
cursor.execute(sql2)

#setting points to 4 for correct answer in studentAnswer table
sql3= "update studentAnswer set points=0 where answer='none' "
cursor.execute(sql3)
                                

sql4= """select subject from questionBank where questionId=%d"""%(3)#int(form.getvalue('qid[%d]'%i)))
cursor.execute(sql4)
sub=cursor.fetchall()

# #obtaining marks scored
# sql5="""select sum(points) from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where studentId=%d"""%(14)
# cursor.execute(sql5)
# marks=cursor.fetchall()

#obtaining max marks
sql6="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where studentId=%d"""%(14)
cursor.execute(sql6)
mm1=cursor.rowcount
mm=4*mm1

print mm

# perc=(marks[0]/mm)*100

# if(perc > 33.0):
# 	result="pass"
# else:
# 	result="fail"

# #inserting values in result table
# sql8= """insert into result(StudentId,subject,marks,'max marks',percent,result) values(%d,%s,%d,%d,%f,%s)"""%(14,sub[0],marks[0],mm,perc,result)
# cursor.execute(sql8)

# #calculating number of correct answers
# sql9="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where studentId=%d and points=%d"""%(14,4)
# cursor.execute(sql9)
# correct=cursor.rowcount

# #calculating number of unattempted questions
# sql9="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where studentId=%d and points=%d"""%(14,0)
# cursor.execute(sql9)
# not_att=cursor.rowcount

# #calculating number of wrong answers
# sql10="""select * from studentAnswer as sa join questionBank as qb on sa.questionId=qb.questionId where studentId=%d and points=%d"""%(14,-1)
# cursor.execute(sql10)
# wrong=cursor.rowcount(sql10)

db.commit()	

#print result

# print """<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
#     <script type="text/javascript">
#       google.charts.load('current', {'packages':['corechart']});
#       google.charts.setOnLoadCallback(drawChart);
#       function drawChart() {

#         var data = google.visualization.arrayToDataTable([
#           ['Response', 'Number'],
#           ['Correct',   %d],
#           ['Not attempted', %d],
#           ['Wrong',%d]
#         ]);

#         var options = {
#           title: 'Detailed Marksheet'
#         };

#         var chart = new google.visualization.PieChart(document.getElementById('piechart'));

#         chart.draw(data, options);
#       }
#     </script>""" % (correct,not_att,wrong)


print "</body>"
print "</html>"