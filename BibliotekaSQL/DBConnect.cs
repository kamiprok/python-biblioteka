using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;
using MySql.Data;

namespace BibliotekaSQL
{
    class DBConnect
    {
        private MySqlConnection connection;
        private string server;
        private string database;
        private string user;
        private string password;
        private string port;
        private string sslM;
        private string connectionString;

        public DBConnect()
        {
            Initialize();
        }

        private void Initialize()
        {
            server = "localhost";
            database = "biblioteka";
            user = "root";
            password = "admin123";
            port = "3306";
            sslM = "none";

            connectionString = String.Format("Server={0};UserId={1};Database={2}", server, user, database);
            //connectionString = String.Format("server={0};port={1};uid={2}; pwd={3}; database={4}; SslMode={5}", server, port, user, password, database, sslM);

            connection = new MySqlConnection(connectionString);
        }

        public bool OpenConnection()
        {
            try
            {
                connection.Open();
                Console.WriteLine("Połączenie nawiązane");
                return true;
            }
            catch(MySqlException ex)
            {
                switch (ex.Number)
                {
                    case 0:
                        Console.WriteLine("Nie można połączyć się z serwerem.");
                        break;
                    case 1045:
                        Console.WriteLine("Niewłaściwa nazwa użytkownika/hasło, spróbuj ponownie");
                        break;
                }
                return false;
            }
        }
        private bool CloseConnection()
        {
            try
            {
                connection.Close();
                return true;
            }
            catch(MySqlException ex)
            {
                Console.WriteLine(ex.Message);
                return false;
            }
        }
        public void conexion()
        {
            try
            {
                connection.Open();

                Console.WriteLine("successful connection");

                connection.Close();
            }
            catch (MySqlException ex)
            {
                Console.WriteLine(ex.Message + connectionString);
            }
        }
        public void Insert(string tablename, List<String> tables, List<String> values)
        {
            string table = "";
            string value = "";
            foreach (string x in tables) {
                table = table + x + ",";
            }
            table = table.Remove(table.Length - 1, 1);
            foreach (string x in values)
            {
                value = value + "'" + x + "'" + ",";
            }
            value = value.Remove(value.Length - 1, 1);

            string query = "INSERT INTO " + tablename + "(" + table + ") VALUES(" + value + ");";
            Console.WriteLine(query);
            if(this.OpenConnection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, connection);
                cmd.ExecuteNonQuery();
                this.CloseConnection();
            }
            else
            {
                Console.WriteLine("Brak połączenia");
            }
        }
        public void Update() { }
        //public void Update() { }
        public void Delete() { }
        //public List<string> [] Select() { }
        //public int Count() { }
        public void Backup() { }
        public void Restore() { }

    }
}
