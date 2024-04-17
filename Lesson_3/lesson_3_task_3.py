from address import Address
from mailing import Mailing
letter = Mailing(Address("123456", "Москва", "Арбат", "12", "1"),
                        Address("789000", "Новосибирск", "Ленина", "24", "15"),
                        "516", "456210987654")
print(f'Отправление {letter.track} из {letter.from_address} в {letter.to_address}. Стоимость {letter.cost} рублей.')
