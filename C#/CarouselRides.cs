using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class CarouselRides
    {
        // Could be done faster and smoother, but eh, it works.
        static void thirteenth() 
        {
            string line;
            while ((line = Console.ReadLine()) != "0 0") 
            {
                int[] array = line.Split(' ').Select(int.Parse).ToArray();
                int maxTickets = array[1];
                List<double[]> offers = new List<double[]>();
                for (int i = 0; i < array[0]; i++) 
                {
                    double[] offer = Console.ReadLine().Split(' ').Select(double.Parse).ToArray();
                    if (offer[0] <= maxTickets) 
                    {
                        offers.Add(offer);
                    }
                }
                if (offers.Count == 0) { Console.WriteLine("No suitable tickets offered"); }
                else if (offers.Count == 1) { Console.WriteLine("Buy {0} tickets for ${1}", offers[0][0], offers[0][1]); }
                else 
                {
                    double[] bestOffer = {0, 0};
                    double bestValue = 10000d;
                    foreach (double[] item in offers) 
                    {
                        double value = item[1] / item[0];
                        if (value == bestValue)
                        {
                            if (item[0] > bestOffer[0]) { bestOffer = item; bestValue = value; }
                        }
                        else if (value < bestValue) { bestOffer = item; bestValue = value; }
                    }
                    Console.WriteLine("Buy {0} tickets for ${1}", bestOffer[0], bestOffer[1]);
                }
            }
        }
    }
}
