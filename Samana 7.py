Algoritmo

using System;
using System.Collections.Generic;

public class BalanceChecker
{
    public static bool IsBalanced(string expression)
    {
        Stack<char> stack = new Stack<char>();

        foreach (char c in expression)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                stack.Push(c);
            }
            else if (c == ')' || c == '}' || c == ']')
            {
                if (stack.Count == 0 || !IsMatchingPair(stack.Pop(), c))
                {
                    return false;
                }
            }
        }

        return stack.Count == 0;
    }

    private static bool IsMatchingPair(char opening, char closing)
    {
        return (opening == '(' && closing == ')') ||
               (opening == '{' && closing == '}') ||
               (opening == '[' && closing == ']');
    }
}



Torres de Hanoi en C# usando Pilas


public class Hanoi
{
    public static void SolveHanoi(int n, char source, char auxiliary, char destination)
    {
        if (n == 1)
        {
            Console.WriteLine($"Mover disco 1 de {source} a {destination}");
        }
        else
        {
            SolveHanoi(n - 1, source, destination, auxiliary);
            Console.WriteLine($"Mover disco {n} de {source} a {destination}");
            SolveHanoi(n - 1, auxiliary, source, destination);
        }
    }
}
