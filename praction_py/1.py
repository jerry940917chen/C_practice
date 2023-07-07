RESET='\033[0m'
BLUE='\033[34m'
RED='\033[31m'


message="In the fullness of time MS-DOS begat Windows. And this is the lineage of Windows: CP/M begat QDOS. QDOS begat DOS 1.0. DOS 1.0 begat DOS 2.0 by way of Unix. DOS 2.0 begat Windows 3.11 by way of PARC and Macintosh. IBM and Microsoft begat OS/2, who begat Windows NT and Warp, the lost OS of lore. Windows 3.11 begat Windows 95 after triumphing over Macintosh in a mighty Battle of Licences. Windows NT begat NT 4.0 by way of Windows 95. NT 4.0 begat NT 5.0, the OS also called Windows 2000, The Millenium Bug, Doomsday, Armageddon, The End Of All Things."

personal_names=["MS-DOS", "Windows", "IBM", "Microsoft", "OS/2", "Windows NT", "Warp", "Windows 95", "NT 4.0", "Windows 2000"]
operation_systems=["CP/M", "QDOS", "DOS", "Unix", "PARC", "Macintosh", "NT 5.0", "The Millenium Bug", "Doomsday", "Armageddon", "The End Of All Things"]

for name in personal_names:
    message=message.replace(name,BLUE+name+RESET)
for os in operation_systems:
    message=message.replace(os,RED+os+RESET)
print(message)

'''
print('\033[31m這是前景色1紅')
print('\033[34m這是前景色4藍')
https://www.twblogs.net/a/5c947ff1bd9eee35fc15edde
'''