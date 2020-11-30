using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Kattis
{
    class CostumeContest
    {
        static void Mainnifico() 
        {
            IDictionary<string, int> costumes = new Dictionary<string, int>();
            int numResponses = Int16.Parse(Console.ReadLine());
            for (int i = 0; i < numResponses; i++) 
            {
                string str = Console.ReadLine();
                if (costumes.ContainsKey(str))
                {
                    costumes[str] += 1;
                }
                else 
                {
                    costumes.Add(str, 1);
                }
            }
            var ordered = costumes.OrderBy(x => x.Value).ToDictionary(pair => pair.Key, pair => pair.Value);
            // ordered.Select(i => $"{i.Key}: {i.Value}").ToList().ForEach(Console.WriteLine);
            var first = ordered.First();
            int minimum = first.Value;
            List<string> best = new List<string>();
            foreach (KeyValuePair<string, int> entry in ordered)
            {
                if (entry.Value == minimum) { best.Add(entry.Key); }
            }
            foreach (string str in best.OrderBy(x => x).ToList()) {
                Console.WriteLine(str);
            }
        }
    }
}
