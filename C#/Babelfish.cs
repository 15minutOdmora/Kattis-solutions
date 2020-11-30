using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class Babelfish
    {
        static void Eigth(string[] args) 
        {
            Dictionary<string, string> dict = new Dictionary<string, string>();
            string line;
            bool validator = true;
            while ((line = Console.ReadLine()) != null)
            {
                if (line == "")
                {
                    validator = false;
                }
                else if (validator)
                {
                    string[] dictInput = line.Split(' ');
                    dict[dictInput[1]] = dictInput[0];
                }
                else
                {
                    if (dict.ContainsKey(line))
                    {
                        Console.WriteLine(dict[line]);
                    }
                    else 
                    {
                        Console.WriteLine("eh");
                    }
                }
            }
        }
    }
}