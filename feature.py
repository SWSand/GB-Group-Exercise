def project(ls):
    names = ''
    for i in ls:
        names += i +"/"
    return names 
    
print(project(['Adrian', 'Joel', 'Jose']))