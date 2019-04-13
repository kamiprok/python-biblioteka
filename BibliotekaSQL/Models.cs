using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BibliotekaSQL
{
    public class Models
    {
        string[] autorzy = { "imie", "nazwisko", "narodowosc", "liczba_dziel", "zyciorys" };
        string[] ksiazki = { "id_autora", "wydawnictwo", "gatunek", "tytul" };
        string[] wypozyczenia = { "id_czytelnika", "id_ksiazki", "data_zamowienia", "data_wypozyczenia", "data_zwrotu", "status" };
        string[] wydawnictwa = { "nazwa", "kraj", "miasto" };
        string[] gatunki = { "nazwa" };
    }
}
