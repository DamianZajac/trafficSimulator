# Obecny stan projektu
1. Wszystkie obiekty œciœle powi¹zane
2. Podstawowa logika gry zaimplementowana
3. Podstawowy test dzia³ania
4. Wszystko obecnie podstawowo w konsoli
5. Generatory pomagaj¹ w kreacji nowych obiektów (ulic/samochodów [daje unikalne nazwy oraz pozycje])
6. Grafika ulic, samochodów, œwiate³
7. 1 tura = 1 ruch dla samochodu
# Wygl¹d przyk³adowego testu

Gdzie cyfry oznaczaj¹ poszczegolne ulice, które s¹ po³¹czone z s¹siednimi (góra, prawo, dó³, lewo)

			15  16  17

9	8   7   6   12  18

10		  	5	   	19

0   1   3   4

	2	   	14

	11	  	13
	
Wypuszczane jest 10 samochodów, które wariuj¹ sobie po mieœcie, jeœli dotr¹ do celu, dodawany jest kolejny (obecnie do 200 samochodów)

# Co ma zostaæ dodane/dorobione/jak to bêdzie wygl¹da³o/cokolwiek
1. Aplikacja jednak w oknie, z relacyjnym dodawaniem ulic jak i równie¿ samochodów (zapewne Tkinter, albo jakieœ inne GUI któe pozwala na relacyjne wstawianie .png)
2. Eksport/Import symulacji/samochodów/ulic
3. Mo¿liwoœæ pauzowania/resumeowania symulacji
4. Mo¿liwoœæ wyœwietlania grafów dla ró¿nych ustawieñ œwiate³, równie¿ mierzenia czasów przejazdów
5. Wybór trybu miêdzy zombie(samochody je¿d¿a randomowo) a do celu (po prostu najkrótsz¹ tras¹ do celu) a œcie¿kami predefiniowanymi
7. ??????
8. Zmiany ustawieñ w szybkoœci wykonywania tur
9. Safety w¹tkowe zachowane
10. Nie by³o punktu 6


# Jak uruchomiæ

Uruchomiæ main.py