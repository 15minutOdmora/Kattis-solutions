using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class ARealChallenge
    {
        static void Sixth(string[] args) 
        {
            double squareMeters = Double.Parse(Console.ReadLine());
            Console.WriteLine(Math.Sqrt(squareMeters) * 4);
        }
    }
}
