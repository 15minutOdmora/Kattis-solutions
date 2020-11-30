using System;
using System.Collections.Generic;
using System.Text;

namespace Kattis
{
    class BasketballOneOn0ne
    {
        static void Ninth(string[] args) 
        {
            string game = Console.ReadLine();
            Dictionary<char, int> dict = new Dictionary<char, int>() { 
                {'1', 1},
                {'2', 2},
                {'A', 0},
                {'B', 0}};
            for (int i = 1; i < game.Length; i += 2) 
            {
                dict[game[i - 1]] += dict[game[i]];
                int a = dict['A'];
                int b = dict['B'];
                if (Math.Max(a, b) >= 11)
                {
                    if (a < b - 1)
                    {
                        Console.WriteLine("B");
                        break;
                    }
                    else if (b < a - 1)
                    {
                        Console.WriteLine("A");
                        break;
                    }
                }
            }
            
        }
    }
}
