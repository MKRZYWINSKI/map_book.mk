from tkinter import *

def prosta_funkcja():
    print("Prosta funkcji")

root=Tk()
root.geometry("800x700")
root.title("Map Book")

# ramki do porządkowania struktury
ramka_lista_uzytkownikow=Frame(root,)
ramka_formularza=Frame(root,)
ramka_pokaz_szczegoly=Frame(root,)
ramka_mapa=Frame(root,)

ramka_lista_uzytkownikow.grid(row=0, column=0)
ramka_formularza.grid(row=0, column=1)
ramka_pokaz_szczegoly.grid(row=1, column=0,columnspan=2, padx=50, pady=20)
ramka_mapa.grid(row=2, column=0)


#ramkalista użytkowników

label_lista_uzytkownikow=Label(ramka_lista_uzytkownikow,text="Lista obiektów:")
listbox_lista_uzytkownikow=Listbox(ramka_lista_uzytkownikow,width=50)
buttom_pokaz_szczegoly=Button(ramka_lista_uzytkownikow, text="Pokaz szczególy")
buttom_usun_uzytkownika=Button(ramka_lista_uzytkownikow, text="usun uzytkownika")
buttom_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow, text="edytuj uzytkownika")

listbox_lista_uzytkownikow.grid(row=0, column=0, columnspan=3)
label_lista_uzytkownikow.grid(row=1, column=0)
buttom_usun_uzytkownika.grid(row= 2, column=2)
buttom_pokaz_szczegoly.grid(row=2, column=0)
buttom_edytuj_uzytkownika.grid(row=2, column=2)

#ramka_formularz
label_formularz_uzytkownikow=Label(ramka_lista_uzytkownikow,text="Formularz edycji i dodawania")
label_imie=Label(ramka_mapa,text="Imie:")
label_nazwisko=Label(ramka_mapa,text="Nazwisko:")
label_miejscowosc=Label(ramka_mapa,text="Miejscowosc:")
label_posty=Label(ramka_mapa,text="Posty:")
entry_imie=Entry(ramka_formularza)
entry_nazwisko=Entry(ramka_formularza)
entry_miejscowosc=Entry(ramka_formularza)
entry_posty=Entry(ramka_formularza)




label_formularz_uzytkownikow.grid(row=0, column=0)
label_imie.grid(row=1, column=0)
label_nazwisko.grid(row=2, column=0)
label_miejscowosc.grid(row=3, column=0)


entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_miejscowosc.grid(row=3, column=1)
entry_posty.grid(row=4, column=1)
button_dodaj_uzytkownika.grid(row=5, column=0)

label_opis_uzytkownika=Label(ramka_mapa,text="Opis uzytkownika:")
label_imie_szczegoly=Label(ramka_mapa,text="Imie:")
label_imie_szczegoly_wartosc=Label(ramka_mapa,text="...")

label_nazwisko_szczegoly=Label(ramka_pokaz_szczegoly,text="Nazwisko:")
label_nazwisko_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="...")
label_posty_szczegoly=Label(ramka_mapa,text="POsty:")
label_posty_szczegoly_wartosc=Label(ramka_mapa,text="...")
label_miejscowosc_szczegoly=Label(ramka_mapa,text="Miejscowosc:")
label_miejscowosc_szczegoly_wartosc=Label(ramka_mapa,text="...")

label_opis.uzytkownika.grid(row=0, column=0)
label_nazwisko.grid(row=1, column=1)
label_nazwisko_szczegoly_wartosc.grid(row=1, column=2)
label_posty_szczegoly.grid(row=1, column=3)
label_posty_szczegoly_wartosc.grid(row=1, column=4)
label_imie_szczegoly.grid(row=1, column=5)
label_miejscowosc_szczegoly_wartosc.grid(row=1, column=6)



























root.mainloop()