using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class Apaxians
    {
        static void Fifth(string[] args) 
        {
            string input = Console.ReadLine();
            string newString = input[0].ToString();
            char memory = input[0];
            for (int i = 1; i < input.Length; i++) 
            {
                char curr = input[i];
                if (curr != memory) 
                {
                    newString += curr;
                }
                memory = curr;
            }
            Console.WriteLine(newString);
        }
    }
}
