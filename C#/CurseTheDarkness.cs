using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class CurseTheDarkness
    {
        static void Mainnifested() 
        {
            int cases = Int16.Parse(Console.ReadLine());
            double[] book;
            double[] candle;
            bool verificator;
            for (int i = 0; i < cases; i++) 
            {
                book = Console.ReadLine().Split(' ').Select(double.Parse).ToArray();
                int numberOfCandles = Int32.Parse(Console.ReadLine());
                verificator = false;
                for (int j = 0; j < numberOfCandles; j++) 
                {
                    candle = Console.ReadLine().Split(' ').Select(double.Parse).ToArray();
                    if (Math.Sqrt(Math.Pow(book[0] - candle[0], 2) + Math.Pow(book[1] - candle[1], 2)) <= 8) { verificator = true; }
                }
                if (verificator) { Console.WriteLine("light a candle"); }
                else { Console.WriteLine("curse the darkness");} 
            }
        }
    }
}
