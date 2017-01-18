import yaml
with open('test.yaml', 'r') as f:
    doc = yaml.load(f)
    mul= doc["technologies"]
data = ["company_name", "unit_type", "footer_quote", "technologies"]
for i in range(0,len(data)):
    if data[i] is 'technologies':
        for j in range(0,len(mul)):
            f=open("file.txt", 'r')
            contents =f.read()
            f.close()
            f=open("file.txt", 'w')
            txt=contents.replace('$'+data[i]+'$',doc [mul[j]])
            f.write('')
            f.write(txt)
            f.close()
    f=open("file.txt", 'r')
    contents =f.read()
    f.close()
    f=open("file.txt", 'w')
    txt=contents.replace('$'+data[i]+'$',doc [data[i]])
    f.write('')
    f.write(txt)
    f.close()