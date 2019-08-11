a = ['Dac nhan', 'dac', 'dan', 'nhan']
str = "Dac nhan tam"
for v in a:
    if v.lower() in str.lower():
        print('some of the strings found in str')
    else:
        print('no strings found in str')