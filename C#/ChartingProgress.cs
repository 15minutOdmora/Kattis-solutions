using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class ChartingProgress
    {
        static void Sextomany() 
        {
            string line;
            int counter = 0;
            while ((line = Console.ReadLine()) != null) 
            {
                if (line == "") 
                {
                    counter = 0;
                    Console.WriteLine("");
                }
                int length = line.Length;
                int number = line.Split('*').Length - 1;
                counter += number;
                string output1 = new String('.', length - counter);
                string output2 = new string('*', number);
                string output3 = new string('.', counter - number);
                Console.WriteLine(output1 + output2 + output3);
            }
        }
    }
}
