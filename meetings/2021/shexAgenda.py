import datetime

for weeknumber in range(41, 52, 2):
	d = "2021-W"+str(weeknumber)+str("-3")
	r = datetime.datetime.strptime(d, "%Y-W%W-%w")



	minutes = "# ShEx Telecon "+r.strftime("%Y-%m-%d")
	minutes += "\n*Wednesday "+r.strftime("%B %d, %y")+" 14, 2020 14:00 CET / 08:00 EDT / 05:00 PDT for 1 hour (in [Other timezones](https://www.timeanddate.com/worldclock/fixedtime.html?msg=ShEx+CG&iso="+r.strftime("%Y%m%d")+"T14&p1=195&ah=1))*\n\n"
	minutes += "## Minutes"
	minutes += "\n https://etherpad.wikimedia.org/p/shexcg_minutes/"+r.strftime("%Y%m%d")+".etherpad\n"
	minutes += """

	*Connection details*:

	* Audio: https://us02web.zoom.us/j/441496948?pwd=OUdBT25vK0NIc2ZER3BnRGVTblIzdz09
	* Gitter: https://gitter.im/shapeExpressions/Lobby
	* Minutes: https://etherpad.wikimedia.org/p/shexcg_minutes

	*Next meetings*: [calendar](https://calendar.google.com/event?action=TEMPLATE&tmeid=N2VyOGMyYjJnZTVma25qMWhlYWF2YmYycHFfMjAyMDAxMDhUMTMwMDAwWiBtaWNlbGlvLmJlX2FjM2xqNzNqdTA0YTY3OGIwaHRsMXBpamRvQGc&tmsrc=micelio.be_ac3lj73ju04a678b0htl1pijdo%40group.calendar.google.com&scp=ALL)

	The meeting is open for participation. Being a [Shex community group member](https://www.w3.org/community/shex/participants) is not a requirement to attend.

	Chair: Andra

	Attendees: 

	Regrets:

	## Agenda

	* Introductions

	* Community updates
	   
	* Discussion

	* AOB

	## Next meeting
	Help us prepare the next meeting on 
	"""
	file = open(r.strftime("%Y%m%d")+"-agenda.md", "w+")

	d = "2021-W"+str(weeknumber+2)+str("-3")
	r = datetime.datetime.strptime(d, "%Y-W%W-%w")
	minutes += " *Wednesday "+r.strftime("%B %d, %y")+" 14, 2021 14:00 CET / 08:00 EDT / 05:00 PDT for 1 hour (in [Other timezones](https://www.timeanddate.com/worldclock/fixedtime.html?msg=ShEx+CG&iso="+r.strftime("%Y%m%d")+"T14&p1=195&ah=1))* "
	minutes += "by editing updates here: "
	minutes += " https://etherpad.wikimedia.org/p/shexcg_minutes\n"


	file.write(minutes)
	file.close()
