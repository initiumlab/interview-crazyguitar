s = "k:1 |k1:2|k2:3|k3:4"
print({v.split(":")[0].strip(): v.split(":")[1].strip() for v in s.split('|')})
