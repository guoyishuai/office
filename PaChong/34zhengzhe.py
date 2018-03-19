import re
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print match.group(0)

re.split(r'[1-9]\d{5}', "bit 100081 tsu 100084")

print re.split(r'[1-9]\d{5}', "bit 100081 tsu 100084")

print re.sub(r'[1-9]\d{5}', ":gys", "100561henshuai,1000000548zhentamashuai")