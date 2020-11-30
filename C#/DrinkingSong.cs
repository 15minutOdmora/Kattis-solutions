using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class DrinkingSong
    {
        static void Mainolino() 
        {
            int number = Int32.Parse(Console.ReadLine());
            string word = Console.ReadLine();
            for (int i = 0; i < number; i++) 
            {
                if (i == number - 1)
                {
                    Console.WriteLine("1 bottle of {0} on the wall, 1 bottle of {0}.", word);
                    Console.WriteLine("Take it down, pass it around, no more bottles of {0}.", word);
                }
                else if (i == number - 2) 
                {
                    Console.WriteLine("{0} bottles of {1} on the wall, {0} bottles of {1}.", number - i, word);
                    Console.WriteLine("Take one down, pass it around, {0} bottle of {1} on the wall.", number - i - 1, word);
                    Console.WriteLine();
                }
                else
                {
                    Console.WriteLine("{0} bottles of {1} on the wall, {0} bottles of {1}.", number - i, word);
                    Console.WriteLine("Take one down, pass it around, {0} bottles of {1} on the wall.", number - i - 1, word);
                    Console.WriteLine();
                }
            }
        }
    }
}
