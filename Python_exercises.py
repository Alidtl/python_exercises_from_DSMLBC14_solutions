#####################################################################################################################
print("Görev 1:")
# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

# Outputs

vars = [x, y, z, a, b, c, l, d, t, s]

for var in vars:
    var_name = [name for name, value in locals().items() if value is var][0]
    print(f"{var_name} değişkeninin veri Tipi: {type(var)}")

print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 2:")

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight"

print(text.upper().replace(",", " ").replace(".", " ").split())

print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 3:")
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.

print(len(lst))

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

print(lst[0], lst[10])

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

print([letter for letter in lst if letter == "D" or letter == "A" or letter == "T"])

# Adım 4: Sekizince indeksteki elemanı siliniz.

lst.pop(8)

# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("S")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")

print(lst)
print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 4:")
# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.

print(dict.keys())

# Adım 2: Value değerlerine erişiniz.

print(dict.values())

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"][1] = 13

print(dict["Daisy"])

# Adım 4: Key değeri Ahmet value değeri [Turkey, 24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Turkey", 24]})

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")

print(dict)
print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 5:")


# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu
# listeleri return eden fonksiyon yazınız.

def even_or_odd(l):
    return [number for number in l if number % 2 == 0], [number for number in l if number % 2 == 1]


even_list, odd_list = even_or_odd([1, 2, 3, 4, 5])

print(even_list, odd_list)
print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 6:")
# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakültelerinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi
# öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
eng_enum_students = list(enumerate(students[0:3], 1))
med_enum_students = list(enumerate(students[3:], 1))

for student in eng_enum_students:
    print("Mühendislik Fakültesi " + str(student[0]) + ". öğrenci: " + student[1])

for student in med_enum_students:
    print("Tıp Fakültesi " + str(student[0]) + ". öğrenci: " + student[1])
print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 7:")
# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri
# yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

info = list(zip(ders_kodu, kredi, kontenjan))

for inf in info:
    print("Kredisi {1} olan {0} kodlu dersin kontenjanı {2} kişidir.".format(inf[0], inf[1], inf[2]))
print("-----------------------------------------------------------------------------")
#######################################################################################################################
print("Görev 8:")


# Görev 8: Aşağıda iki adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsıyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

def set_control(set1, set2):
    if set1.issuperset(set2):
        print(set.intersection(set1, set2))
    else:
        print(set.difference(set2, set1))


kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

set_control(kume1, kume2)
print("-----------------------------------------------------------------------------")
#######################################################################################################################
