def repetidos(txt, dsp):
    dictionary = {}
    for i in txt:
        if txt.count(i) >= 3:
            dictionary[i] = str(txt.count(i)).strip()
    for i in dictionary:
        dsp += i
    return ' '.join(dsp.strip().replace(' ', ''))


cazados = ""

while "-1" not in cazados:
    empleado = input().strip()
    cazados += empleado

despedidos = ''
cazados = ''.join(sorted(cazados.split()))
despedidos = repetidos(cazados, despedidos)
print(despedidos)
