eto_list = ['子', "丑", "寅"] 
eto_list.append('卯')
eto_list.remove('丑')
print(eto_list)

eto_str = '子丑寅卯辰巳午未申酉戌亥'
index = eto_str.find('辰')
replaced = eto_str.replace('子', '猫')
print(replaced)