import requests
import dns
import dns.resolver
from pprint import pprint
#import whois
#import whois


#obj = whois.whois('74.125.225.229')
#omain = whois.query('themaniac.co.in')

#print(domain)

import ssl, socket

hostname = 'benn.tv'
ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
    s.connect((hostname, 443))
    cert = s.getpeercert()
    pprint(cert)

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
print('issued_to:  ', issued_to)
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']
print('issued_by:  ', issued_by)

result = dns.resolver.resolve(hostname, 'A')
for ipval in result:
    print('IP', ipval.to_text())

'''result = dns.resolver.query('canfor.com', 'AAAA')
for ipval in result:
	print('IPV6', ipval)'''

try:
	result = dns.resolver.resolve('benn.tv', 'MX')

	for exdata in result:
		print('MX Record:', exdata)
except:
	print("NO MX Record FOUND")
	pass

try:
	result = dns.resolver.resolve('benn.tv', 'NS')
	for exdata in result:
		print('NS Record:', exdata)

except:
	print("NO NS Record FOUND")
	pass

try:
	result = dns.resolver.resolve('benn.tv', 'TXT')
	for val in result:
		print('TXT Record : ', val.to_text())

except:
	print("NO TXT Record FOUND")
	pass