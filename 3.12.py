using System;
using System.Collections.Generic;
using System.Diagnostics;

class Jugador
{
    public int Id { get; set; }
    public string Nombre { get; set; }

    public Jugador(int id, string nombre)
    {
        Id = id;
        Nombre = nombre;
    }

    public override string ToString()
    {
        return $"ID: {Id}, Nombre: {Nombre}";
    }
}

class Torneo
{
    private Dictionary<string, HashSet<Jugador>> equipos;
    
    public Torneo()
    {
        equipos = new Dictionary<string, HashSet<Jugador>>();
    }

    public void AgregarEquipo(string nombreEquipo)
    {
        if (!equipos.ContainsKey(nombreEquipo))
        {
            equipos[nombreEquipo] = new HashSet<Jugador>();
            Console.WriteLine($"Equipo '{nombreEquipo}' registrado con éxito.");
        }
        else
        {
            Console.WriteLine($"El equipo '{nombreEquipo}' ya existe.");
        }
    }

    public void AgregarJugador(string nombreEquipo, Jugador jugador)
    {
        if (equipos.ContainsKey(nombreEquipo))
        {
            if (!equipos[nombreEquipo].Add(jugador))
            {
                Console.WriteLine($"El jugador '{jugador.Nombre}' ya está en el equipo '{nombreEquipo}'.");
            }
            else
            {
                Console.WriteLine($"Jugador '{jugador.Nombre}' agregado al equipo '{nombreEquipo}'.");
            }
        }
        else
        {
            Console.WriteLine($"El equipo '{nombreEquipo}' no existe.");
        }
    }

    public void MostrarEquipos()
    {
        foreach (var equipo in equipos)
        {
            Console.WriteLine($"\nEquipo: {equipo.Key}");
            foreach (var jugador in equipo.Value)
            {
                Console.WriteLine($"  - {jugador}");
            }
        }
    }

    public void AnalizarTiempoEjecucion()
    {
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();

        // Simulación de búsqueda en la estructura de datos
        foreach (var equipo in equipos)
        {
            _ = equipo.Value.Contains(new Jugador(0, "Ejemplo"));
        }

        stopwatch.Stop();
        Console.WriteLine($"\nTiempo de ejecución de búsqueda: {stopwatch.ElapsedTicks} ticks.");
    }
}

class Program
{
    static void Main()
    {
        Torneo torneo = new Torneo();

        torneo.AgregarEquipo("Tigres");
        torneo.AgregarEquipo("Leones");

        torneo.AgregarJugador("Tigres", new Jugador(1, "Carlos Pérez"));
        torneo.AgregarJugador("Tigres", new Jugador(2, "Luis Gómez"));
        torneo.AgregarJugador("Leones", new Jugador(3, "Ana Torres"));

        torneo.MostrarEquipos();

        torneo.AnalizarTiempoEjecucion();
    }
}
