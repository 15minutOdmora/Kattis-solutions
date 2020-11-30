using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class ClimbingWorm
    {
        static void Sevenenteeth() 
        {
            int[] numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int up = numbers[0]; int down = numbers[1]; int height = numbers[2];
            int c = 0; int y = 0;
            while (true) {
                y += up;
                c += 1;
                if (y >= height) { Console.WriteLine(c); break; }
                y -= down;
            }
        }
    }
}
