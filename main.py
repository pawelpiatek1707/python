from Models.Pacjent import Pacjent
from Models.Dietetyk import Dietetyk
from Models.Dieta import Dieta
from Models.Zamowienie import Zamowienie

pacjent1 = Pacjent('p1', 'Jan', 'Nowak', 'cukrzyca')
dietetyk1 = Dietetyk('d1', 'Krzysztof', 'Kowalski', 'dietetyk cukrzycowy')
dieta1 = Dieta('dc1', 'dieta cukrzycowa 1', 123.99, dietetyk1, 2500)
dieta2 = Dieta('dc2', 'dieta cukrzycowa 2', 55.99, dietetyk1, 3100)
zamowienie = Zamowienie()
zamowienie.order_id = 'z1'
zamowienie.date = '15.01.2021',
zamowienie.client = pacjent1
zamowienie.diets = [dieta1, dieta2]

print(f"order price: {zamowienie.get_price()}")
print(f"sum of calories: {zamowienie.get_calories()}")
