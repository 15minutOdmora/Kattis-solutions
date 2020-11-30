using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class Cetiri
    {
        static void Fourteenth() 
        {
            // d as in data
            int[] d = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            Array.Sort(d);
            int d1 = d[1] - d[0];
            int d2 = d[2] - d[1];
            if (d1 == d2) { Console.WriteLine(d[2] + d1); }
            else {
                if (Math.Max(d1, d2) == d1) { Console.WriteLine(d[0] + d2); }
                else { Console.WriteLine(d[1] + d1); }
            }
        }
    }
}
