# Obecny stan projektu
1. Wszystkie obiekty �ci�le powi�zane
2. Podstawowa logika gry zaimplementowana
3. Podstawowy test dzia�ania
4. Wszystko obecnie podstawowo w konsoli
5. Generatory pomagaj� w kreacji nowych obiekt�w (ulic/samochod�w [daje unikalne nazwy oraz pozycje])
6. Grafika ulic, samochod�w, �wiate�
7. 1 tura = 1 ruch dla samochodu
# Wygl�d przyk�adowego testu

Gdzie cyfry oznaczaj� poszczegolne ulice, kt�re s� po��czone z s�siednimi (g�ra, prawo, d�, lewo)

			15  16  17

9	8   7   6   12  18

10		  	5	   	19

0   1   3   4

	2	   	14

	11	  	13
	
Wypuszczane jest 10 samochod�w, kt�re wariuj� sobie po mie�cie, je�li dotr� do celu, dodawany jest kolejny (obecnie do 200 samochod�w)

# Co ma zosta� dodane/dorobione/jak to b�dzie wygl�da�o/cokolwiek
1. Aplikacja jednak w oknie, z relacyjnym dodawaniem ulic jak i r�wnie� samochod�w (zapewne Tkinter, albo jakie� inne GUI kt�e pozwala na relacyjne wstawianie .png)
2. Eksport/Import symulacji/samochod�w/ulic
3. Mo�liwo�� pauzowania/resumeowania symulacji
4. Mo�liwo�� wy�wietlania graf�w dla r�nych ustawie� �wiate�, r�wnie� mierzenia czas�w przejazd�w
5. Wyb�r trybu mi�dzy zombie(samochody je�d�a randomowo) a do celu (po prostu najkr�tsz� tras� do celu) a �cie�kami predefiniowanymi
7. ??????
8. Zmiany ustawie� w szybko�ci wykonywania tur
9. Safety w�tkowe zachowane
10. Nie by�o punktu 6


# Jak uruchomi�

Uruchomi� main.py