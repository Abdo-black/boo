import os

COUNT = 100000000000
folder = os.path.dirname(os.path.abspath(__file__))

for i in range(1, COUNT + 1):
    path = os.path.join(folder, f"file_{i}.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write("Hello World")

print(f"تم إنشاء {COUNT} ملف في نفس مكان ملف Python.")
input("اضغط Enter للخروج...")