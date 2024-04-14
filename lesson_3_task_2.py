from smartphone import Smartphone
first_smartphone = Smartphone('Apple', 'iphone 14', '+79000012112')
second_smartphone = Smartphone('Samsung', 'Galaxy A35', '+79888889900')
third_smartphone = Smartphone('Xiaomi', 'Redmi 12', '+79111112112')
fourth_smartphone = Smartphone('Google', 'Pixel 7a', '+79778889900')
fifth_smartphone = Smartphone('OnePluse', 'Nord 3', '+79667778888')
catalog = [first_smartphone, second_smartphone, third_smartphone, fourth_smartphone, fifth_smartphone]
for x in catalog :
   print(f'{x.brand} - {x.model}. {x.number}')
