using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        // Crear un conjunto ficticio de 500 ciudadanos (nombres de ejemplo)
        HashSet<string> ciudadanos = new HashSet<string>();
        for (int i = 1; i <= 500; i++)
        {
            ciudadanos.Add("Ciudadano " + i);
        }

        // Crear un conjunto ficticio de 75 ciudadanos vacunados con Pfizer
        HashSet<string> vacunadosPfizer = new HashSet<string>();
        for (int i = 1; i <= 75; i++)
        {
            vacunadosPfizer.Add("Ciudadano " + i);
        }

        // Crear un conjunto ficticio de 75 ciudadanos vacunados con Astrazeneca
        HashSet<string> vacunadosAstrazeneca = new HashSet<string>();
        for (int i = 76; i <= 150; i++)
        {
            vacunadosAstrazeneca.Add("Ciudadano " + i);
        }

        // Listado de ciudadanos que no se han vacunado
        HashSet<string> noVacunados = new HashSet<string>(ciudadanos);
        noVacunados.ExceptWith(vacunadosPfizer);
        noVacunados.ExceptWith(vacunadosAstrazeneca);

        Console.WriteLine("Ciudadanos que no se han vacunado:");
        foreach (var ciudadano in noVacunados)
        {
            Console.WriteLine(ciudadano);
        }

        // Listado de ciudadanos que han recibido las dos vacunas (Pfizer y Astrazeneca)
        HashSet<string> vacunadosAmbas = new HashSet<string>(vacunadosPfizer);
        vacunadosAmbas.IntersectWith(vacunadosAstrazeneca);

        Console.WriteLine("\nCiudadanos que han recibido las dos vacunas:");
        foreach (var ciudadano in vacunadosAmbas)
        {
            Console.WriteLine(ciudadano);
        }

        // Listado de ciudadanos que solamente han recibido la vacuna de Pfizer
        HashSet<string> soloPfizer = new HashSet<string>(vacunadosPfizer);
        soloPfizer.ExceptWith(vacunadosAstrazeneca);

        Console.WriteLine("\nCiudadanos que solamente han recibido la vacuna de Pfizer:");
        foreach (var ciudadano in soloPfizer)
        {
            Console.WriteLine(ciudadano);
        }

        // Listado de ciudadanos que solamente han recibido la vacuna de Astrazeneca
        HashSet<string> soloAstrazeneca = new HashSet<string>(vacunadosAstrazeneca);
        soloAstrazeneca.ExceptWith(vacunadosPfizer);

        Console.WriteLine("\nCiudadanos que solamente han recibido la vacuna de Astrazeneca:");
        foreach (var ciudadano in soloAstrazeneca)
        {
            Console.WriteLine(ciudadano);
        }
    }
}
