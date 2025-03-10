
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Catálogo de revistas
        List<string> catalogo = new List<string>
        {
            "National Geographic", "Scientific American", "Time", "Nature",
            "Forbes", "The Economist", "Popular Science", "New Scientist",
            "IEEE Spectrum", "Wired"
        };

        // Ordenamos el catálogo para realizar búsqueda binaria
        catalogo.Sort();

        while (true)
        {
            Console.WriteLine("\nMenú:");
            Console.WriteLine("1. Buscar un título");
            Console.WriteLine("2. Salir");
            Console.Write("Seleccione una opción: ");
            string opcion = Console.ReadLine();

            if (opcion == "1")
            {
                Console.Write("Ingrese el título de la revista: ");
                string titulo = Console.ReadLine();

                bool encontrado = BusquedaBinaria(catalogo, titulo, 0, catalogo.Count - 1);
                Console.WriteLine(encontrado ? "Título encontrado" : "Título no encontrado");
            }
            else if (opcion == "2")
            {
                break;
            }
            else
            {
                Console.WriteLine("Opción no válida, intente de nuevo.");
            }
        }
    }

    // Búsqueda binaria recursiva
    static bool BusquedaBinaria(List<string> catalogo, string titulo, int inicio, int fin)
    {
        if (inicio > fin)
            return false;

        int medio = (inicio + fin) / 2;
        int comparacion = string.Compare(catalogo[medio], titulo, StringComparison.OrdinalIgnoreCase);

        if (comparacion == 0)
            return true;
        else if (comparacion > 0)
            return BusquedaBinaria(catalogo, titulo, inicio, medio - 1);
        else
            return BusquedaBinaria(catalogo, titulo, medio + 1, fin);
    }
}
