countries = ['Bahrain', 'Australia','Bangladesh', 'Austria', 'Armenia', 'Botswana','Azerbaijan', 'Canada', 'Angola' ]
countries_and_capitals = {
 'Australia': 'Canberra',
 'Armenia': 'Yerevan',
 'Botswana': 'Gaborone',
 'Canada': 'Ottawa',
 'Chile': 'Santiago',
 'Cuba': 'Havana',
 'Egypt': 'Cairo',
 'France': 'Paris'
}
for i in countries:
 if i in countries_and_capitals:
  print(countries_and_capitals[i])
 else:
  print('Nothing was found!')