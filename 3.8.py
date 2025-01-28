
using System;
using System.Collections.Generic;

class AtraccionParque
{
    static void Main(string[] args)
    {
        // Definimos una cola para representar la línea de espera
        Queue<string> colaDeEspera = new Queue<string>();

        // Simulamos que 35 personas llegan a la cola
        for (int i = 1; i <= 35; i++)
        {
            colaDeEspera.Enqueue($"Persona {i}");
        }

        Console.WriteLine("Asignación de asientos para la atracción:\n");

        // Simulamos la asignación de los 30 asientos disponibles
        int numeroDeAsiento = 1;
        while (numeroDeAsiento <= 30 && colaDeEspera.Count > 0)
        {
            string persona = colaDeEspera.Dequeue();
            Console.WriteLine($"Asiento {numeroDeAsiento}: {persona}");
            numeroDeAsiento++;
        }

        // Verificamos si quedaron personas en la cola sin subir
        if (colaDeEspera.Count > 0)
        {
            Console.WriteLine("\nPersonas que no pudieron subir a la atracción:");
            foreach (var persona in colaDeEspera)
            {
                Console.WriteLine(persona);
            }
        }
        else
        {
            Console.WriteLine("\nTodos los asientos han sido asignados y no hay más personas en la cola.");
        }
    }
}
