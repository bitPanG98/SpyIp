#!/usr/bin/python

#### INFO ####

"""
SCRIPT=> SpyIp
Job=> Get Any IP Addr
BY=> Oseid Aldary
"""

# IMPORT LIBRARIES #

try:

   import socket,dns.resolver,optparse,subprocess,multiprocessing
   from json import load; from urllib2 import urlopen; from copy import copy; from os import devnull; from time import sleep as se; from os import system as sy

except KeyboardInterrupt:
        print("[!] Something Went Wrong!\n[>] Please Try Again :)")
        exit(1)
except:
     print("Some Modules Is Missing In Your Python !!!\n")
     print("[1] Dnspython> pip install dnspython\n[2] Json> pip install simplejson")
     exit(1)
from Core.examples import examp
## Check Internet Connection.....
server = "www.google.com"
def check():
  try:
    ip = socket.gethostbyname(server)
    con = socket.create_connection
    return True
  except KeyboardInterrupt:
        print("[!] Something Went Wrong!\n[>] Please Try Aagain :)")
        exit(1)
  except:
	pass
  return False
check = check()

#1: Find User Local IP address
def locip():
  try:
     locip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
     return locip
  except:
	return "[!] Error Your Not Connect To Any Network !!!\n[!] Please Check Your Connection!"
#2: Find User Puplic IP Address
def pupip():
 if check == True:
  pupip = urlopen('http://ip.42.pl/raw').read()
  print("[P] Puplic IP: "+str(pupip))
 else:
   print("[!] Error: Your Not Connect To Internet !!!\n[!] Please Check Your Internet Connection!")
   exit(1)
#3: Find Network Hosts

def pinger(job_q, results_q):
    DEVNULL = open(devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass
def map_network(pool_size=255):
 try:
    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = locip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list

 except:
    return "[!] Error Your Not Connect To Any Network !!!\n[!] Please Check Your Connection!"

########################

# Know Server Name From He Port Or Know Server Port From Server Name Service :)
def serpor(x):
  try:
     try:
	sname = socket.getservbyport(int(x))
	print('\n[~] Server Name Is: {} '.format(sname))
     except:
        sport = socket.getservbyname(x)
        print('\n[~] Server Port Is: {} '.format(str(sport)))
  except:
	print("\n[!] Unknown This ==> {}".format(str(x)))

parse = optparse.OptionParser("""\
\033[1;37m
Usage:
     python SoyIp.py [OPTIONS...]
=================================
IPs  OPTIONS:
------------
       -t --target         >>  Get Target Website Server IPs
       -a --all            >>  Scan For All Servers On Wbsites
       -f --found-me       >>  Found Your Local IP And Your Puplic IP
       -n --network        >>  scan network and Found IPs Of Hosts
==============
Other Options:
--------------
       -c --check 	   >>  Know Server Name From Port OR Know Server Port From Name
       -e --examples       >>  Show Examples
       -v --version	   >>  Show Script Version""",version='\n[>] Version>> 1.0\nWait New Version Soon :)')
def main():
  parse.add_option('-t','-T','--TARGET','--target',dest="target",type="string")
  parse.add_option("-a","-A","--ALL",'--all',action='store_true',dest="all",default=False)
  parse.add_option("-f","-F","--FOUND-ME",'--found-me',action='store_true',dest="fme",default=False)
  parse.add_option("-n","-N","--NETWORK",'--network',action='store_true',dest="network",default=False)
  parse.add_option('-c','-C','--CHECK','--check',dest="check",type="string")
  parse.add_option("-e","-E","--EXAMPLES",'--examples',action='store_true',dest="ex",default=False)
  parse.add_option("-v","-V","--VERSION",action='store_true',dest="ve",default=False)
  (options,args) = parse.parse_args()
  if options.target !=None and not options.all:
	target = options.target
	try:
           test = open(target, 'r')
	   res = True
	except:
 	   res = False
	if res == False:
 	 if target[:8] == "https://":
             host = target[8:]
	 elif target[:7] == "http://":
             host = target[7:]
	 else:
            host = target
	 target = host
         def SpyIp(target):
             if check ==True:
              if ',' in target:
	         targets = target.split(',')
                 print("[@] Scanning [ {} ] Sites...".format(str(len(targets))))
                 for i in targets:
                  try:
                    ip = socket.gethostbyname(i)
                    print("[*] TARGET> {}\n[*] IP> {}\n========".format(i,ip))
                  except socket.error:
	            print("[*] TARGET> {}\n[!] IP> Cod404: Server Not Found !!!".format(i))
		  except KeyboardInterrupt:
			  print(" ")
			  break
              else:
		  print("[~] Connecting....{}\n".format(target))
		  try:
		     ip = socket.gethostbyname(target)
                     print("[*] TARGET> {}\n[*] IP> {}\n========".format(target,ip))
		  except socket.error:
			print("[~] TARGET> {}\n[!] IP> Cod404: Server Not Found !!!".format(target))
		  except KeyboardInterrupt:
			  pass
			  exit(1)
             else:
		 print("[!] Please Check Your Internet Connection !!!")
		 exit(1)
	 SpyIp(target)
	else:
		targets = open(target, 'r')
                for t in targets:
		   t = t.strip()
                   def checker():
	            try:
	               if t[:8] == "https://":
		             host = t[8:]
	               elif t[:7] == "http://":
		             host = t[7:]
	               else:
		            host = t

	               ip = socket.gethostbyname(host)
		       run = socket.create_connection((ip, 80), 2)
		       return True
                    except:
	                   pass
                    return False
                   if checker() == True:
                        if t[:8] == "https://":
                             host = t[8:]
                        elif t[:7] == "http://":
                             host = t[7:]
                        else:
                             host = t
			try:
                           ip = socket.gethostbyname(host)
                           print("[*] TARGET> {}\n[*] IP> {}\n========".format(t,ip))
			except socket.error:
	               			pass
			except KeyboardInterrupt:
				pass

  elif options.target !=None and options.all:
   target = options.target
   if check ==True:
	 try:
	    test = open(target, 'r')
	    res = True
	 except:
	    res = False
	 if res ==True:
	     targets = open(target, 'r').readlines()
	     for t in targets:
		   t = t.strip()
                   def checker():
	            try:
	               if t[:8] == "https://":
		             host = t[8:]
	               elif t[:7] == "http://":
		             host = t[7:]
	               else:
		            host = t

	               ip = socket.gethostbyname(host)
		       run = socket.create_connection((ip, 80), 2)
		       return True
                    except:
	                   pass
                    return False
                   if checker() == True:
                        if t[:8] == "https://":
                             host = t[8:]
                        elif t[:7] == "http://":
                             host = t[7:]
                        else:
                             host = t
		        found = []
		        for address_type in ['A', 'AAAA']:
		           try:
		              answers = dns.resolver.query(host, address_type)
		              for rdata in answers:
			        found.append(rdata)
		           except dns.resolver.NoAnswer:
			           pass
		        le = len(found)
		        if len(found) > 0:
			 print("\n[~]> Target[ {} ]".format(t))
			 print("[+] Servers Found({}):".format(str(le)))
			 loop = 1
			 for i in found:
			   print("\tSERVER[{}]   >   {}".format(loop,i))
			   loop +=1
			 print("======================\n")
		        else:
		           print("\n[!] No Servers Found !!!")
		           exit(1)
                   else:
	               pass
	 elif ',' in target:
		targets = target.split(',')
                for t in targets:
                   def checker():
	            try:
	               if t[:8] == "https://":
		             host = t[8:]
	               elif t[:7] == "http://":
		             host = t[7:]
	               else:
		            host = t

	               ip = socket.gethostbyname(host)
		       run = socket.create_connection((ip, 80), 2)
		       return True
                    except:
	                   pass
                    return False
                   if checker() == True:
                        if t[:8] == "https://":
                             host = t[8:]
                        elif t[:7] == "http://":
                             host = t[7:]
                        else:
                             host = t
		        found = []
		        for address_type in ['A', 'AAAA']:
		           try:
		              answers = dns.resolver.query(host, address_type)
		              for rdata in answers:
			        found.append(rdata)
		           except dns.resolver.NoAnswer:
			           pass
		        le = len(found)
		        if len(found) > 0:
			 print("\n[~]> Target[ {} ]".format(t))
			 print("[+] Servers Found({}):".format(str(le)))
			 loop = 1
			 for i in found:
			   print("\tSERVER[{}]   >   {}".format(loop,i))
			   loop +=1
			 print("======================\n")
		        else:
		           print("\n[!] No Servers Found !!!")
		           exit(1)
                   else:
		       pass
         else:	 
           def checker():
	     try:
	        if target[:8] == "https://":
		  host = target[8:]
	        elif target[:7] == "http://":
		   host = target[7:]
	        else:
		     host = target

	        ip = socket.gethostbyname(host)
		run = socket.create_connection((ip, 80), 2)
		return True
             except:
	          pass
             return False
           if checker() == True:
                if target[:8] == "https://":
                  host = target[8:]
                elif target[:7] == "http://":
                   host = target[7:]
                else:
                     host = target
		found = []
		print("[#]~[Finding Servers IP Of TARGET[ {} ].....\n".format(target))
		for address_type in ['A', 'AAAA']:
		  try:
		     answers = dns.resolver.query(host, address_type)
		     for rdata in answers:
			found.append(rdata)
		  except dns.resolver.NoAnswer:
			pass
		le = len(found)
		if len(found) > 0:
			print("[@]~[Found [ {} ] Server(s) Status> UP ".format(str(le)))
			print("[+] Servers:\n")
			loop = 1
			for i in found:
			  print("SERVER[{}]   >   {}".format(loop,i))
			  loop +=1
		else:
		    print("\n[!] No Servers Found !!!")
		    exit(1)
           else:
	       print("\n[!] CodeError:404 >> No Server Found !!!")
	       exit(1)
   else:
        print("[!] Please Check Your Internet Connection !!!")
	exit(1)

  elif options.fme:
	print("\n[@]~[Finding Your IPs....\n")
	locipe = locip()
	if locipe !="[!] Error Your Not Connect To Any Network !!!\n[!] Please Check Your Connection!":
	 print("[L] Local IP: {}".format(locipe))
	else:
	  print(" ")
	  print(locipe)
	  exit(1)
	pupip()
  elif options.network:
	ips_list = map_network()
	if ips_list !="[!] Error Your Not Connect To Any Network !!!\n[!] Please Check Your Connection!":
          print("Mapping...")
	  se(1)
          loop = 1
          up = "UP"
          print("======================================")
          print("ID\t\tIP\t\tSTATUS")
          print("==\t\t==\t\t======")
          for ip in ips_list:
            print("{}\t   {}    \t  {}".format(loop,ip,copy(up)))
            loop +=1
          result = loop -1
          print("\nI Found <{}> Device In Network !".format(result))
        else:
	  print(ips_list)

  elif options.ve:
	print("\n[>] Version>> 1.0\nWait New Version Soon :)")
	exit(1)
  elif options.ex:
        sy("printf '\e[8;70;180;t' || mode 800")
        sy("clear || cls")
	examp()
	exit(1)
  elif options.check !=None:
	sp = options.check
	serpor(sp)
	exit(1)
  else:
      print(parse.usage)
      exit(1)

if __name__=="__main__":
	main()

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
