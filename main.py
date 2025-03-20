import json

# Öffnen und Lesen der Dateien
with open('Mirand_Gashi.json', 'r', encoding="utf-8") as file:
    content_1 = file.read()
    json_dict1 = json.loads(content_1)

with open('Rafi_xxx.json', 'r', encoding="utf-8") as file:
    content_2 = file.read()
    json_dict2 = json.loads(content_2)

with open('Yazan_Shreteh.json', 'r', encoding="utf-8") as file:
    content_3 = file.read()
    json_dict3 = json.loads(content_3)

with open('abdulsalam_alhammoud.json', 'r', encoding="utf-8") as file:
    content_4 = file.read()
    json_dict4 = json.loads(content_4)

# Extrahieren der Daten aus den Dateien
mirand = json_dict1["name"] + "\n" + json_dict1["email"] + "\n" + json_dict1["course"]
rafi = json_dict2["name"] + "\n" + json_dict2["email"] + "\n" + json_dict2["course"]
yazan = json_dict3["name"] + "\n" + json_dict3["email"] + "\n" + json_dict3["course"]
abdulsalam = json_dict4["name"] + "\n" + json_dict4["email"] + "\n" + json_dict4["course"]

# Kombinieren der Inhalte der Dateien in ein neues Format
content_combined = f"[{content_1},\n{content_2},\n{content_3},\n{content_4}]"

# Kombinieren der extrahierten Daten in einen Text
# e= json_dict1["name"] + "\n" + json_dict1["email"] + "\n" + json_dict1["course"] +"\n"+"\n" + json_dict2["name"] + "\n" + json_dict2["email"] + "\n" + json_dict2["course"]
e = mirand + "\n\n" + rafi + "\n\n" + yazan + "\n\n" + abdulsalam


# Ausgabe des Ergebnisses
print(e)

# Schreiben des kombinierten Inhalts in eine neue Datei
with open('team_Mirand_Rafi_Yazan_Abdulsalam.json', 'w') as file:
    file.write(content_combined)


'''
import json

file1 = open("Mirand_Gashi.json","r")
file2 = open("Rafi_xxx.json","r")

content1 = file1.read()
content2 = file2.read()

json_dict1 = json.loads(content1)
json_dict2 = json.loads(content2)


e= json_dict1["name"] + "\n" + json_dict1["email"] + "\n" + json_dict1["course"] +"\n" + json_dict2["name"] + "\n" + json_dict2["email"] + "\n" + json_dict2["course"]

file1.close()
file2.close()

print(e)


import json

json_dict1 = json.loads('{"a":1, "b":2}')
json_dict2 = json.loads('{"a":1, "b":4, "c":5}')
json_dict3 = json.loads('{"a":1, "b":2, "c":5}')

a = set(json_dict1.items())
b = set(json_dict2.items())
c = set(json_dict3.items())
a & b & c
{('a', 1)}'
'''
