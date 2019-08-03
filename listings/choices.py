bedroom_choices = {}
for i in range(1, 11):
    bedroom_choices[f'{i}'] = i

price_choices = {}
for i in range(100000, 1100000, 100000):
    if(i < 1000000):
        price_choices[f'{i}'] = f'${i:,}'
    else:
        price_choices[f'{i}'] = '$1M+'

state_choices = {
    'AK': 'ALASKA',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona'
}
