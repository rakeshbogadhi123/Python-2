'''
Input:
6
CSK;RR;win
RR;DD;draw
MI;KKR;win
SH;RR;loss
CSK;DD;draw
MI;DD;draw

Output:
Team                    | MP |  W |  D |  L |  P |
CSK                     |  2 |  1 |  1 |  0 |  4 |
MI                      |  2 |  1 |  1 |  0 |  4 |
RR                      |  3 |  1 |  1 |  1 |  4 |
DD                      |  3 |  0 |  3 |  0 |  3 |
KKR                     |  1 |  0 |  0 |  1 |  0 |
SH                      |  1 |  0 |  0 |  1 |  0 |


---------------------------------------------------'''


n=int(input())
d={};d1={}
for i in range(n):
    ex_a=input().split()
    key=int(ex_a[0])
    value=int(ex_a[1])
    d.update({key:value})

m=int(input())
for j in range(m):
    ex_b=input().split()
    key=int(ex_b[0])
    value=int(ex_b[1])
    d1.update({key:value})


for key in d1:
    if key in d:
        d[key]=d[key]+d1[key]
    else:
        d.update({key:d1[key]})
        

#d_zero=0
#if d.get(0,1)==0:
#    d_zero=1
    
res_d={}
for i in d:
    if d[i]!=0:
        res_d.update({i:d[i]})
res_d=sorted(res_d.items(),key=lambda x:x[0],reverse=True)

if len(res_d)==0:
    print("0")
else:
    r1=[]
    for k,v in res_d:
        r1.append("{}x^{}".format(v,k))
        #print(r1)
        r2=(" + ").join(r1)
        #print(r2)
        r2=r2.replace("x^0","")
        r2=r2.replace(" + -"," - ")
        r2=r2.replace("x^1","x")
        r2=r2.replace("1x^","x^")
        r2=r2.replace("1x","x")
        #r2=r2.replace("x^0","")
    print(r2)
#----------------
n_teams=int(input())
result_dic={}
print('{:<24}'.format('Team')+'| {:>2}'.format('MP')+' |'+' {:>2}'.format('W')+' |'+' {:>2}'.format('D')+' |'+
' {:>2}'.format('L')+' |'+' {:>2}'.format('P')+' |')

for i in range(n_teams):
    team1,team2,outcome=input().split(';')
    if team1 not in result_dic:
        result_dic.update({team1:{'MP':0,'win':0,'draw':0,'loss':0,'p':0}})
    if team2 not in result_dic:
        result_dic.update({team2:{'MP':0,'win':0,'draw':0,'loss':0,'p':0}})
    if outcome=='win':
        result_dic[team1][outcome]+=1
        result_dic[team2]['loss']+=1
        result_dic[team1]['MP']+=1
        result_dic[team2]['MP']+=1
        result_dic[team1]['p']+=3
    elif outcome=='loss':
        result_dic[team1][outcome]+=1
        result_dic[team2]['win']+=1
        result_dic[team1]['MP']+=1
        result_dic[team2]['MP']+=1
        result_dic[team2]['p']+=3
    elif outcome=='draw':
        result_dic[team1][outcome]+=1
        result_dic[team2][outcome]+=1
        result_dic[team1]['MP']+=1
        result_dic[team2]['MP']+=1
        result_dic[team1]['p']+=1
        result_dic[team2]['p']+=1

result_dic=sorted(result_dic.items())
result_dic=sorted(result_dic,key=lambda x:x[1]['p'],reverse=True)

for team,team_attr in result_dic:
    print('{:<24}'.format(team)+
    '| {:>2}'.format(team_attr['MP'])+
    ' |'+' {:>2}'.format(team_attr['win'])+
    ' |'+' {:>2}'.format(team_attr['draw'])+
    ' |'+' {:>2}'.format(team_attr['loss'])+
    ' |'+' {:>2}'.format(team_attr['p'])+' |')

------------------------------------------------------------------------------------------------------------------------------------------------------
import datetime
from datetime import datetime , date
def addyears(d,years):
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        #leap 
        return d+(date(d.year+years,1,1)-date(d.year,1,1))

string = input()
year_in_int = int(input())
date_obj = datetime.strptime(string,'%b %d %Y')
print(addyears(datetime.date(date_obj),year_in_int),end='')


'''
from datetime import datetime  , timedelta
string = input()
year_in_int = int(input())
date_obj = datetime.strptime(string,'%b %d %Y')
date_obj = date_obj.date()
result_date = date_obj + relativedelta(years=1)
#result_date = date_obj.year+year_in_int
#date_obj = date_obj.replace(result_date)
print(result_date,end='')
'''
Input:
Jul 11 2014
-2

Output:
2012-07-11

------------------------------------------------------------------------------------------------------------------------------------------------------


    
    
