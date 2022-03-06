import xml.etree.ElementTree as ET
import json

data = """
<person>
    <name>Check</name>
    <phone type="intl">
        +1 734 303 45456
    </phone>
    <email hide="yes"/>
</person>
"""

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))

data = """{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "23456"
    },
    "email" : {
        "hide" : "yes"
    }
}
"""

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])

data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])

