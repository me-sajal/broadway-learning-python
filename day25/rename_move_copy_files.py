folder_path = "C:\\Users\\sajal\\OneDrive\\Desktop\\python\\practice"
# crating 5 files named
# for i in range(1,6):
#     fp = open(f"{folder_path}\\file{i}.txt","w")

import os
os.chdir(folder_path)
print(os.listdir())

# change name of the files
for count, file in enumerate(os.listdir(), start=1):
    name, ext = os.path.splitext(file)
    newname = f"test{count}{ext}"
    os.rename(file,newname)
    