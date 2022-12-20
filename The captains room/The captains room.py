# Enter your code here. Read input from STDIN. Print output to STDOUT
k = input()
room_ids = input()
room_info = {}
room_ids = room_ids.split(' ')
for room_id in room_ids:
    if(room_info.get(room_id)!=None):
        room_info[room_id]+=1
    else:
        room_info[room_id]=1


for (room_number,value) in room_info.items():
    if(value==1):
        print(room_number)
        break
        
