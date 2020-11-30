using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class Abc
    {
        static void Fourth(string[] args)
        {
            string line = Console.ReadLine();
            int[] arr = line.Split(' ').Select(int.Parse).ToArray();
            Array.Sort<int>(arr, new Comparison<int>((i1, i2) => i2.CompareTo(i1)));
            Dictionary<char, int> data = new Dictionary<char, int>()
            {
                {'C', arr[0]},
                {'B', arr[1]},
                {'A', arr[2]}
            };

            string abc = Console.ReadLine();
            Console.WriteLine("{0} {1} {2}", data[abc[0]], data[abc[1]], data[abc[2]]);
        }
    }
}
