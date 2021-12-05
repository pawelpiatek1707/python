
from models.Pojazd import Pojazd
from models.Kierowca import Kierowca
from models.Odcinek import Odcinek
from models.Kurs import Kurs

kierowca1 = Kierowca('3623ygssw', 'Jan', 'Kowalski')

odcinek1 = Odcinek('3322fjfdi112', 231.5, kierowca1, 'Katowice', 'Krakow')
odcinek2 = Odcinek('543dfwfvef', 315.654, kierowca1, 'Krakow', 'Warszawa')

pojazd1 = Pojazd('Renault', 'czerwony', 8, 20, 110)

kurs = Kurs()
kurs.course_id = 'ovbruvbuon2313dxc'
kurs.name = 'Kurs1'
kurs.driver = kierowca1
kurs.distance = [odcinek1, odcinek2]
kurs.car = pojazd1

print(kurs)
print(kurs.sum_distance())
print(kurs.car)
