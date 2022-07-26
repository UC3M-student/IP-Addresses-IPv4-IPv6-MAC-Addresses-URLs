import random as rd


IPv4 = [str(rd.randint(0,255)),str(rd.randint(0,255)),str(rd.randint(0,255)),str(rd.randint(0,255))]
IPv4 = ".".join(IPv4)
print("IPv4:", IPv4)

IPv6 = [str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),str(hex(rd.randint(4096,65535)))[2:].upper(),]
IPv6 = ":".join(IPv6)
print("IPv6: ",IPv6)

MAC = [str(hex(rd.randint(16,255)))[2:].upper(),str(hex(rd.randint(16,255)))[2:].upper(),str(hex(rd.randint(16,255)))[2:].upper(),str(hex(rd.randint(16,255)))[2:].upper(),str(hex(rd.randint(16,255)))[2:].upper(),str(hex(rd.randint(16,255)))[2:].upper()]

MAC = ":".join(MAC)
print("MAC: ",MAC)


#url_ = input("Por favor indique su url: ")

a = input("Por favor indique su url: ")
a = a.replace(":","")
a = a.replace("www.","")
a = a.replace("/","",1)
a = a.split("/")


print("Protocol: ",a[0])
print("Domain Name: ",a[1])
print("Folder Structure: ",a[2])
print("File name: ",*a[3:])
