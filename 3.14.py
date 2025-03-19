
using System;

class Nodo
{
    public int valor;
    public Nodo izquierdo, derecho;

    public Nodo(int valor)
    {
        this.valor = valor;
        izquierdo = derecho = null;
    }
}

class ArbolBinario
{
    public Nodo raiz;

    public ArbolBinario()
    {
        raiz = null;
    }

    // Insertar un nuevo valor en el árbol binario
    public void Insertar(int valor)
    {
        raiz = InsertarRecursivo(raiz, valor);
    }

    private Nodo InsertarRecursivo(Nodo raiz, int valor)
    {
        // Si el árbol está vacío, devuelve un nuevo nodo
        if (raiz == null)
        {
            raiz = new Nodo(valor);
            return raiz;
        }

        // Si el valor es menor que el valor de la raíz, lo insertamos en el subárbol izquierdo
        if (valor < raiz.valor)
        {
            raiz.izquierdo = InsertarRecursivo(raiz.izquierdo, valor);
        }
        // Si el valor es mayor que el valor de la raíz, lo insertamos en el subárbol derecho
        else if (valor > raiz.valor)
        {
            raiz.derecho = InsertarRecursivo(raiz.derecho, valor);
        }

        // Retorna la raíz del árbol (sin cambios)
        return raiz;
    }

    // Recorrido en orden (Inorder traversal)
    public void RecorridoInorden()
    {
        RecorridoIn
