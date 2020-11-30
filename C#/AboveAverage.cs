using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class AboveAverage
    {
        static void Third(string[] args)
        {
            string firstInput = Console.ReadLine();
            int testCases = Int32.Parse(firstInput);
            for (int i = 0; i < testCases; i++)
            {
                string line = Console.ReadLine();
                int[] array = line.Split(' ').Select(int.Parse).ToArray();

                // int[] percentages = array[1..];
                decimal num = array[0];
                IEnumerable<int> Percentages = array.Skip(1).Take(decimal.ToInt32(num));
                decimal avg = Percentages.Sum() / num;
                decimal aboveAvg = 0;
                foreach (int item in Percentages)
                {
                    if (item > avg)
                    {
                        aboveAvg++;
                    }
                }
                string output = Math.Round((aboveAvg / num) * 100.000M, 3).ToString().Replace(",", ".");
                Console.WriteLine("{0}%", output);
            }
        }
    }
}
