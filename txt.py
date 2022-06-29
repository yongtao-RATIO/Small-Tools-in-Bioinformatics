# RMSD 氨基酸序列剔除保守site

txt=[]
for i in range(129,195):
    txt.append(i)
print(txt)
for i in [129,184,194]:
    txt.remove(i)
print(txt)