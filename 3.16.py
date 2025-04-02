Primero, vamos a definir las clases necesarias para el gráfico:

using System;
using System.Collections.Generic;
using System.Linq;

public class Vuelo
{
    public string CiudadDestino { get; set; }
    public int Costo { get; set; }

    public Vuelo(string ciudadDestino, int costo)
    {
        CiudadDestino = ciudadDestino;
        Costo = costo;
    }
}

public class Grafo
{
    private Dictionary<string, List<Vuelo>> adjacencias;

    public Grafo()
    {
        adjacencias = new Dictionary<string, List<Vuelo>>();
    }

    // Agregar un vuelo (arista) entre dos ciudades
    public void AgregarVuelo(string ciudadOrigen, string ciudadDestino, int costo)
    {
        if (!adjacencias.ContainsKey(ciudadOrigen))
            adjacencias[ciudadOrigen] = new List<Vuelo>();

        adjacencias[ciudadOrigen].Add(new Vuelo(ciudadDestino, costo));
    }

    // Obtener los vuelos desde una ciudad
    public List<Vuelo> ObtenerVuelosDesde(string ciudad)
    {
        return adjacencias.ContainsKey(ciudad) ? adjacencias[ciudad] : new List<Vuelo>();
    }
}


Ahora implementamos el algoritmo de Dijkstra para encontrar el vuelo más barato entre dos ciudades:

public class Dijkstra
{
    public static int EncontrarVueloMasBarato(Grafo grafo, string ciudadOrigen, string ciudadDestino)
    {
        // Diccionario para almacenar el costo mínimo hasta cada ciudad
        var costos = new Dictionary<string, int>();
        // Diccionario para almacenar el nodo anterior (para reconstruir el camino)
        var anteriores = new Dictionary<string, string>();
        // Cola de prioridad para elegir el siguiente nodo más barato
        var prioridad = new SortedSet<(int costo, string ciudad)>();

        // Inicializar el costo de todas las ciudades como infinito, excepto el origen
        foreach (var ciudad in grafo.ObtenerVuelosDesde(ciudadOrigen))
        {
            costos[ciudadOrigen] = 0;
        }
        
        costos[ciudadOrigen] = 0;
        prioridad.Add((0, ciudadOrigen));

        while (prioridad.Count > 0)
        {
            // Obtener la ciudad con el costo más bajo
            var (costoActual, ciudadActual) = prioridad.Min;
            prioridad.Remove(prioridad.Min);

            // Si llegamos a la ciudad destino, devolvemos el costo
            if (ciudadActual == ciudadDestino)
            {
                return costoActual;
            }

            // Revisar todos los vuelos desde la ciudad actual
            foreach (var vuelo in grafo.ObtenerVuelosDesde(ciudadActual))
            {
                int nuevoCosto = costoActual + vuelo.Costo;
                if (!costos.ContainsKey(vuelo.CiudadDestino) || nuevoCosto < costos[vuelo.CiudadDestino])
                {
                    costos[vuelo.CiudadDestino] = nuevoCosto;
                    anteriores[vuelo.CiudadDestino] = ciudadActual;
                    prioridad.Add((nuevoCosto, vuelo.CiudadDestino));
                }
            }
        }

        // Si no se encontró un camino, devolver -1 (o algún valor indicativo)
        return -1;
    }
}


Vamos a crear un pequeño ejemplo donde tenemos algunas ciudades y vuelos entre ellas.


public class Program
{
    public static void Main(string[] args)
    {
        // Crear el grafo de vuelos
        var grafo = new Grafo();
        grafo.AgregarVuelo("CiudadA", "CiudadB", 100);
        grafo.AgregarVuelo("CiudadA", "CiudadC", 300);
        grafo.AgregarVuelo("CiudadB", "CiudadC", 50);
        grafo.AgregarVuelo("CiudadB", "CiudadD", 200);
        grafo.AgregarVuelo("CiudadC", "CiudadD", 150);

        // Encontrar el vuelo más barato de CiudadA a CiudadD
        var costo = Dijkstra.EncontrarVueloMasBarato(grafo, "CiudadA", "CiudadD");

        if (costo != -1)
        {
            Console.WriteLine($"El vuelo más barato de CiudadA a CiudadD cuesta: {costo} unidades.");
        }
        else
        {
            Console.WriteLine("No hay un camino disponible entre las ciudades.");
        }
    }
}
