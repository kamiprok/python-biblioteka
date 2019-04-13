using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace BibliotekaSQL
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("1. Dodaj rekord");
            Console.WriteLine("2. Usuń rekord");

            DBConnect conn = new DBConnect();

            List<String> tabele = new List<string>();
            List<String> wartosci = new List<string>();

            tabele.Add("id_autora");
            tabele.Add("imie");
            tabele.Add("nazwisko");
            tabele.Add("narodowosc");
            tabele.Add("liczba_dziel");
            tabele.Add("zyciorys");

            wartosci.Add("10000");
            wartosci.Add("Henryk");
            wartosci.Add("Sienkiewicz");
            wartosci.Add("Polska");
            wartosci.Add("21");
            wartosci.Add("Krótki opis jego życia");

            conn.Insert("autorzy", tabele, wartosci);

            Console.WriteLine("Dopisane");

            Console.ReadLine();
        }
    }
}
