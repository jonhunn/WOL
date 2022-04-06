import pyodbc
from wakeonlan import send_magic_packet

#use this to wake up all machines on the LAN based on a specific site identifer

siteNum = input("Input a site number or computer name: ")
connStr = open("altiris.txt", "r")
sqlQuery = ("SELECT  computer.name, nics.mac_addr FROM     computer INNER JOIN hardware ON computer.computer_id = hardware.computer_id INNER JOIN computer_group ON computer.group_id = computer_group.group_id INNER JOIN computer_group AS computer_group_1 ON computer.group_id = computer_group_1.group_id INNER JOIN nics ON computer.computer_id = nics.computer_id WHERE (computer.name LIKE '%" + siteNum + "%' AND prod_name NOT LIKE '%i500%' AND prod_name NOT LIKE '%x360%' AND computer_name NOT LIKE '%w01') ORDER BY computer.name")


def read(conn):
	cursor.execute(sqlQuery)	
	while True:
		row = cursor.fetchone()
		if not row:
			if row == None:
				print('Packets sent.')
			break
		macs = row.mac_addr
		name = row.name
		count = 0
		print('Sending packets to ' + name + '.')
		while (count < 100):
			count = count + 1
			send_magic_packet(macs)

		
		


conn = pyodbc.connect(
        connStr
	)
	
cursor = conn.cursor()


while True:
	read(conn)
	print("Please allow 5 minutes before re-running.")
	theEnd = input("Press enter to close, or R/r to rerun: ")
	if theEnd != 'r' and theEnd != 'R':
                break
		
