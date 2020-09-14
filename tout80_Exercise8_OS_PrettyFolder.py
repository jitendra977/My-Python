import os
import datetime

Current_Date = datetime.datetime.today().strftime('%d-%b-%Y')
path = 'JITU'
i = 0
for filename in os.listdir(path):
    extension = os.path.splitext(filename)[1][1:]
    print(extension)
    if extension == "txt":
        os.rename(os.path.join(path, filename),
                  os.path.join(path, filename[0] + str(i) + str("_") + str(Current_Date) + '.txt'))
        i = i + 1
    if extension == "jpg":
        os.rename(os.path.join(path, filename),
                  os.path.join(path, 'Photo_' + str(i) + str("_") + str(Current_Date) + '.jpg'))
        i = i + 1
    if extension == "png":
        os.rename(os.path.join(path, filename),
                  os.path.join(path, 'Photo2_' + str(i) + str("_") + str(Current_Date) + '.png'))
        i = i + 1