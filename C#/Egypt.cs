using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class Egypt
    {
        static void Mainminmain() 
        {
            string line;
            int[] sides;
            while ((line = Console.ReadLine()) != "0 0 0") 
            {
                sides = line.Split(' ').Select(int.Parse).ToArray();
                Array.Sort(sides);
                if (Math.Pow(sides[0], 2) + Math.Pow(sides[1], 2) == Math.Pow(sides[2], 2)) { Console.WriteLine("right"); }
                else { Console.WriteLine("wrong"); }
            }
        }
    }
}
