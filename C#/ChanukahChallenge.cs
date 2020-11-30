using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class ChanukahChallenge
    {
        static public int CalculateDays(int n) 
        {
            return (n * (n + 1)) / 2 + n;
        }
        static void Sixteenth() 
        {
            int testCases = Int32.Parse(Console.ReadLine());
            for (int i = 0; i < testCases; i++) 
            {
                int[] numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
                Console.WriteLine("{0} {1}", numbers[0], CalculateDays(numbers[1]));
            }
        }
    }
}
