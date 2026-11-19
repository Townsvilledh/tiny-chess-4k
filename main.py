import json,os,urllib.request as q
U=os.getenv("MAKEFUN_ENV_URL")or exit()
BUD=int(os.getenv("CHESS_NODES",5e4))
def po(p,b):
 with q.urlopen(q.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"}))as s:return json.load(s)
V=[0,100,320,330,500,900,0]
T="kkkkkkkkuuuuuuuummoqqommllmppmllkkkookkkljikkijllmmggmmlkkkkkkkkaceeeecacgkkkkgcekmnnmkeelnoonleeknoonkeelmnnmlecgkllkgcaceeeecagiiiiiigikkkkkkiiklmmlkiillmmlliikmmmmkiimmmmmmiilkkkkligiiiiiigkkkkkkkklmmmmmmljkkkkkkjjkkkkkkjjkkkkkkjjkkkkkkjjkkkkkkjkkkllkkkgiijjiigikkkkkkiikllllkijkllllkjkkllllkjilllllkiiklkkkkigiijjiigeccaacceeccaacceeccaacceeccaaccegeecceegiggggggiookkkkoooqmkkmqo"
B=[0]*128
def ini():
 for i in range(128):B[i]=-1 if i&136 else 0
 for i,p in enumerate([4,2,3,5,6,3,2,4]):B[i]=p;B[112+i]=p+8;B[16+i]=1;B[96+i]=9
ini()
KN=(-33,-31,-18,-14,14,18,31,33);KI=(-17,-16,-15,-1,1,15,16,17);BI=(-17,-15,15,17);RO=(-16,-1,1,16);M=1e5
S=0;E=-1;N=0
AB=ValueError
def ev():
 s=0
 for i,p in enumerate(B):
  if p>0:
   t=p&7;r=7-(i>>4)if p<8 else i>>4;v=V[t]+(ord(T[(t-1)*64+r*8+i%8])-107)*5
   s+=v if p<8 else-v
 return s if S==0 else-s
def at(x,by):
 for d in(-15,-17)if by==0 else(15,17):
  y=x+d
  if not(y&136)and B[y]==1+8*by:return 1
 for w,pc in((KN,2),(KI,6)):
  for d in w:
   y=x+d
   if not(y&136)and B[y]==(pc if by==0 else pc+8):return 1
 for w,ps in((BI,(3,5)),(RO,(4,5))):
  for d in w:
   y=x+d
   while not(y&136):
    p=B[y]
    if p:
     if(p<8)==(by==0)and(p&7)in ps:return 1
     break
    y+=d
 return 0
def gn(cp=0):
 ms=[]
 for f in range(128):
  if f&136:continue
  p=B[f]
  if not p or(p<8)!=(S==0):continue
  t=p&7
  if t==1:
   d=16-32*S;la=7-7*S
   for t1,cc in((f+d,0),(f+d-1,1),(f+d+1,1)):
    if t1&136:continue
    v=B[t1]
    if cc:
     if not((v and(v<8)!=(S==0))or t1==E):continue
    elif v or(cp and(t1>>4)!=la):continue
    if(t1>>4)==la:ms+=[(f,t1,r)for r in(5,4,3,2)]
    else:
     ms.append((f,t1,0))
     if not cc and(f>>4)==(1+5*S)and B[f+2*d]==0:ms.append((f,f+2*d,0))
  else:
   for dd in(KN if t==2 else KI if t==6 else BI if t==3 else RO if t==4 else BI+RO):
    t1=f+dd
    while not(t1&136):
     v=B[t1]
     if v==0:
      if not cp:ms.append((f,t1,0))
     else:
      if(v<8)!=(S==0):ms.append((f,t1,0))
      break
     if t in(2,6):break
     t1+=dd
 return ms
def mk(m):
 global S,E
 f,t,pr=m;w=B[f];z=B[t];o=E;ec=0
 if w&7==1 and t==E and z==0:
  ec=t-16+32*S;B[ec]=0
 B[t]=pr if pr else w;B[f]=0
 if w&7==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);B[rt]=B[rf];B[rf]=0
 if w&7==1 and abs(t-f)==32:E=(f+t)//2
 else:E=-1
 S=1-S
 return(w,z,o,ec)
def un(m,u):
 global S,E
 f,t,pr=m;w,z,o,ec=u;S=1-S;B[f]=w;B[t]=z;E=o
 if ec:B[ec]=9-8*S
 if w&7==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);B[rf]=B[rt];B[rt]=0
def od(m):
 f,t,pr=m;v=B[t]
 return(10*V[B[t]&7]-V[B[f]&7]+(9e3 if pr else 0))
def sr(d,a,b,y):
 global N,S
 N+=1
 if N&511==0 and N>BUD:raise AB
 wk=B.index(6);bk=B.index(14)
 ck=at(wk if S==0 else bk,1-S)
 if d<=0 and not ck:
  v=ev()
  if v>=b:return b
  if v>a:a=v
 best=-M
 ms=sorted(gn(d<=0 and not ck),key=od,reverse=1)
 ln=0
 for m in ms:
  u=mk(m)
  k=m[1] if u[0]&7==6 else(wk if S==1 else bk)
  if at(k,S):un(m,u);continue
  ln+=1;sc=-sr(d-1,-b,-a,y+1);un(m,u)
  if sc>best:best=sc
  a=max(a,sc)
  if a>=b:return a
 if ln==0:return-M+y if ck else(a if d<=0 else 0)
 return best
def pm(u):return((int(u[1])-1)*16+ord(u[0])-97,(int(u[3])-1)*16+ord(u[2])-97,"nbrq".index(u[4])+2 if len(u)==5 else 0)
def th(mv,lg):
 global N,S,E
 ini();S=0;E=-1
 for u in mv:mk(pm(u))
 lg2=[pm(u)for u in lg]
 if not lg2:return lg[0]
 N=0;best=lg2[0];dep=1
 while 1:
  try:
   a=-M;bm=best
   for m in sorted(lg2,key=od,reverse=1):
    u=mk(m);sc=-sr(dep-1,-M,-a,1);un(m,u)
    if sc>a:a=sc;bm=m
   best=bm;dep+=1
  except AB:break
 f,t,pr=best
 return f"{chr(97+f%8)}{(f>>4)+1}{chr(97+t%8)}{(t>>4)+1}{'nbrq'[pr-2]if pr else''}"
while 1:
 g=po("/game",{});s=g["status"]
 if s=="done":break
 while s=="your_move":
  g=po("/move",{"game":g["game"],"move":th(g["moves"],g["legal_moves"])});s=g["status"]
