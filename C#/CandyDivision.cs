using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class CandyDivision
    {
        static void printDivisors(long n)
        {
            List<long> list = new List<long>();
            list.Add(0);
            for (long i = 1; i <= Math.Sqrt(n); i++)
            {
                if (n % i == 0)
                {
                    // If divisors are equal, 
                    // add only one 
                    if (n / i == i)
                    {
                        list.Add(i - 1);  // add one less accounting for Benny
                    }
                    // Otherwise add both 
                    else
                    {
                        list.Add(i-1);
                        list.Add((n / i) - 1);
                    }
                }
            }
            list.Sort((a, b) => a.CompareTo(b));  // Sort the list in ascending order
            for (int i = 1; i < list.Count - 1; i++) {
                Console.Write("{0} ", list[i]);
            }
            Console.Write(n - 1); // Add one number less, n divides n (n-1 because of Benny)
        }
        public static void Eleventh()
        {
            long number = Convert.ToInt64(Console.ReadLine());
            printDivisors(number);
        }
    }
}
