import requests
import json
import os

webhook_url1 = 'https://script.google.com/macros/s/AKfycbzZ18jdzpAoMQw7q8Ie9z5ren9Y5QUdv9jAq27gvTTijmc8jLBfg0eomYZJF8JwEpof/exec?grade=1'
webhook_url2 = 'https://script.google.com/macros/s/AKfycbzZ18jdzpAoMQw7q8Ie9z5ren9Y5QUdv9jAq27gvTTijmc8jLBfg0eomYZJF8JwEpof/exec?grade=2'

r1=requests.get(url=webhook_url1)
r2=requests.get(url=webhook_url2)


print('1')
data1=json.dumps(json.loads(r1.text), ensure_ascii=False, indent=4)
print(data1)

print('\n2')
data2=json.dumps(json.loads(r2.text), ensure_ascii=False, indent=4)
print(data2)

os.system('rm -R Kagakugijutu-Scratch')

os.system('git clone https://github.com/TAMAGO55123/Kagakugijutu-Scratch.git')

gradefile='Kagakugijutu-Scratch/json/'

with open(gradefile+'grade1.json', mode='w') as f:
    f.write(data1)

with open(gradefile+'grade2.json', mode='w') as f:
    f.write(data2)

with open(gradefile+'grade.js', mode='w') as f:
    f.write('var gradedata=['+data1+','+data2+'];')

os.system("git config user.name github-actions")
os.system("git config user.email github-actions@github.com")
os.system("git add .")
os.system("git commit -m \"update grade files\"")
os.system("git push")
