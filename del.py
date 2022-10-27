#C:\win>scp ff8.csh usernamex@10.12.168.12:/path/Abdulla
#removing null indexes from devicenumbering by reading configuration       
for i in range(len(configuration)):
    for j in range(len(configuration[i])):
                if configuration[i][j] == ' null_x8':
                   del devicenumbering[i][j]
                elif configuration[i][j] == ' null_x4':
                   del devicenumbering[i][j]
                elif configuration[i][j] == ' null_x2':
                   del devicenumbering[i][j]
print("new list",devicenumbering)
