def solution(new_id):
    
    new_id = new_id.lower()
    for c in new_id:
        if  (c != '-') and (c != '_') and (c != '.') and \
            (c not in [chr(a) for a in range(48,58)]) and \
            (c not in [chr(a) for a in range(97,123)]):
            new_id = new_id.replace(c,'')

    for i in range(15,1,-1):
        if '.'*i in new_id:
            new_id=new_id.replace('.'*i,'.')

    if new_id=='.' or new_id=='':
        new_id=''
        
    elif new_id[0]=='.' and new_id[-1]=='.':
        new_id= new_id[1:]
        new_id= new_id[:-1]

    elif new_id[-1]=='.':
        new_id= new_id[:-1]

    elif new_id[0]=='.':
        new_id= new_id[1:]
    
    if len(new_id)==0:
        new_id='a'
    
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1]=='.':
            new_id= new_id[:-1]
    if len(new_id)<3:
        while(len(new_id)<3):
            new_id = new_id+new_id[-1]
    
        
    return new_id