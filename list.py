#การแสดงค่าในlist
fruits = ["apple","banana","cherry","watermelon","blueberry"]
print(fruits[1])
#การเปลี่ยนค่าในlist
fruits[1] = "blackcurrant"
print(fruits[1])
#การเปลี่ยนค่าในlistหลายตำแหน่ง
fruits[1:3] = ["kiwi","mango","pineapple"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("orange")
print(fruits)
fruits.insert(3, "grape")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#การลบค่าในlist
fruits.remove("watermelon")
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#ภรัณยู ผันสันเทียะ 18