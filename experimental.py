file = {
    'Data Type': '.png',
    'Saved To': '/Users/user1/desktop',
    'Size': '8 Mb',
    'Date Saved': '11:45 02.10.2026',
    'Device': 'Computer'
}

print(file.get('Data Type', 'Unknown')) 
file['Device'] = 'Mobile'
file['Last Change'] = '17:12 03.10.2026'

print(
    '== Values of dictionary ==\n',
    '== Keys ==\n', file.keys(), '\n\n',
    '== Values ==\n', file.values(), '\n\n'
    '== Full List ==\n', file.items(), '\n' 
)

print('\n=============================\n')
for key, value in file.items():
    print(key, value)
