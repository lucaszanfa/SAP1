with open('SAP_MELHORADO.circ', 'r', encoding='utf-8') as f:
    data = f.read()
start = data.index('<lib desc="#Memory" name="4">')
end = data.index('</lib>', start) + len('</lib>')
print(data[start:end])
