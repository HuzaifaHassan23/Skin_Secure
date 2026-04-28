# os module import kiya,jo hume computer ke files aur folders ke sath kaam karne deta hai.
import os

# dataset path jaha mai na dataset para howa hai
# \ is liya hai error na aya, aur r ka matlab hai rew string
data_path = r"C:\Users\ITG LAB\Downloads\archive (1)"

# dataset ka andr jitna b folder hain in ka naam print hon ga
print("Folders:", os.listdir(data_path))

# part-1 aur part-2 ke andar images count karo
for folder in os.listdir(data_path):
    folder_path = os.path.join(data_path, folder)
    if os.path.isdir(folder_path):
        print(folder, ":", len(os.listdir(folder_path)), "images")
import os

# dataset path
data_path = r"C:\Users\ITG LAB\Downloads\archive (1)"

# andar ke folders check karo
print("Folders:", os.listdir(data_path))

# part-1 aur part-2 ke andar images count kara ga aur in ki counting output mais show kara ga,
# like this, Folders: ['part1', 'part2'] , part1 : 100 images,   part2 : 150 images
for folder in os.listdir(data_path):
    folder_path = os.path.join(data_path, folder)
    if os.path.isdir(folder_path):
        print(folder, ":", len(os.listdir(folder_path)), "images")
