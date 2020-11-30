using System;
using System.Globalization;
using System.Collections.Generic;
using System.Linq;

namespace Kattis
{
    class ANewAlphabet
    {
        static readonly Dictionary<char, string> data = new Dictionary<char, string>(){
            {'a', "@"},
            {'n', @"[]\[]"},
            {'b', "8"},
            {'o', "0"},
            {'c', "("},
            {'p', "|D"},
            {'d', "|)"},
            {'q', "(,)"},
            {'e', "3"},
            {'r', "|Z"},
            {'f', "#"},
            {'s', "$"},
            {'g', "6"},
            {'t', "']['"},
            {'h', "[-]"},
            {'u', "|_|"},
            {'i', "|"},
            {'v', @"\/"},
            {'j', "_|"},
            {'w', @"\/\/"},
            {'k', "|<"},
            {'x', "}{"},
            {'l', "1"},
            {'y', "`/"},
            {'m', @"[]\/[]"},
            {'z', "2"}
            };
        static char[] arrayOfAllKeys = data.Keys.ToArray();
        static void Secondary(string[] args)
        {
            var input = Console.ReadLine();
            var output = "";
            foreach (char letter in input)
            {
                if (arrayOfAllKeys.Contains(Char.ToLower(letter, CultureInfo.InvariantCulture)))
                {
                    output += data[Char.ToLower(letter, CultureInfo.InvariantCulture)];
                }
                else
                {
                    output += letter;
                }
            }
            Console.WriteLine(output);
        }
    }
}
