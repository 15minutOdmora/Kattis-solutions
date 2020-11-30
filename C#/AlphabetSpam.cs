using Microsoft.CSharp.RuntimeBinder;
using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Text;

namespace Kattis
{
    class AlphabetSpam
    {
        static void Fifth(string[] args)
        {
            string input = Console.ReadLine();
            decimal upper = 0;
            decimal space = 0;
            decimal symbol = 0;
            decimal lower = 0;
            foreach (char chr in input) 
            {
                if (Char.IsUpper(chr))
                {
                    upper++;
                }
                else if (chr == '_')
                {
                    space++;
                }
                else if (!Char.IsLetter(chr)) 
                {
                    symbol++;
                }
                else
                {
                    lower++;
                }
            }
            decimal sum = upper + space + symbol + lower;
            Console.WriteLine(Math.Round(space /sum, 16));
            Console.WriteLine(Math.Round(lower /sum, 16));
            Console.WriteLine(Math.Round(upper /sum, 16));
            Console.WriteLine(Math.Round(symbol /sum, 16));
        }
    }
}
