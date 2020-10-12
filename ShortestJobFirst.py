class process:
	def __init__(self,pid,at,cputmp):
	 self.pid=pid
	 self.arrival=at
	 self.cput=cputmp

chart=[]

def SJF(plist,n,preemp):
	global chart
	cola=[]
	time=0
	ap=0 #arrived process
	rp=0 #ready process
	done=0 #done process

	if not preemp: 
		while(done<n):
			for i in range(ap,n):
				if time>=plist[i].arrival:
					cola.append(plist[i])
					ap+=1
					rp+=1

			if rp<1:
				time+=1
				chart.append(0)
				continue

			cola.sort(key=lambda x:(x.cput)) #ordena los apuntadores de menor a mayor de acuerdo al tiempo de cpu y al tiempo de llegada

			if cola[0].cput>0:
				for g in range(cola[0].cput):
					chart.append(cola[0].pid)
				time+=cola[0].cput
				cola[0].cput=99999
				done +=1
				rp-=1

plist=[]
plist.append(process(1,2,7))
plist.append(process(2,2,4))
plist.append(process(3,4,1))
plist.append(process(4,5,4))


SJF(plist,len(plist),0)
print(chart)
print(len(chart))
