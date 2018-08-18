from decimal import Decimal

bevType = [ 'Beer', 'Wine', 'Liquor' ]
beerBrand = {'Budweiser':5.2 , 'Bud Light':4.2, 'Miller Genuine Draft':4.6 , 'Miller Lite':4.2, 'Coor\'s Original Banquet':5,
'Coor\'s Light':4.2, 'Brooklyn Lager':5.2, 'Dogfish Head 60 Min. IPA':6, 'Dogfish Head 90 Min. IPA':9, 'Dogfish Head 120 Min. IPA':18,
'Lagunitas IPA':6.2, 'Miller High Life':4.6, 'Fat Tire':5.2, 'Stella Artois':5.2 }
beerAmount = { 'Pony':7, 'Standard':12, 'Pint':14, 'Tall Boy':16, 'Big Boy':24 }
wineAmount = { 'Standard':6, 'Large':7.5, '750ml Bottle':25.4, 'Large 1,500ml Bottle':50.07 }
liquorAmount = { 'Shot':1.5, 'Standard Mixed Drink':2.5, 'Large Mixed Drink':3.75 }
stats = []

bev = input('Beer, Wine, or Liquor: ')
if bev == bevType[0]:
    stats.append(str(bevType[0]))                                       # (0) Type
    stats.append(beerAmount[input('Size: ')])                           # (1) Size
    stats.append(float(input('Quantity: ')))                            # (2) Qty
    stats.append(stats[1] * stats[2])                                   # (3) Total Ounces ( Size * Qty)
    stats.append(float(input('abv%: ')) / 100 )                         # (4) abv%
    stats.append(round(stats[3] * stats[4], 2))                         # (5) Total Ethynol (total ounces * abv%)
    stats.append(round(stats[5] / .6, 2))                               # (6) Units (Total Ethynol / .6 )
    print('That\'s ' + str(stats[6]) + ' units of alcohol.')
elif bev == bevType[1]:
    stats.append(str(bevType[0]))
    stats.append(wineAmount[input('Glass size: ')])
    stats.append(float(input('Quantity: ')))
    stats.append(stats[1] * stats[2])
    stats.append(float(input('abv%: ')) / 100 )
    stats.append(round(stats[3] * stats[4], 2))
    stats.append(round(stats[5] / .6, 2))
    print('That\'s ' + str(stats[6]) + ' units of alcohol.')
elif bev == bevType[2]:
    stats.append(str(bevType[0]))
    stats.append(liquorAmount[input('Drink type: ')])
    stats.append(float(input('Quantity: ')))
    stats.append(stats[1] * stats[2])
    stats.append(float(input('Proof: ')) / 2  / 100)
    stats.append(round(stats[3] * stats[4], 2))
    stats.append(round(stats[5] / .6, 2))
    print('That\'s ' + str(stats[6]) + ' units of alcohol.')



