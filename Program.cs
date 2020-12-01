using System;
using System.Collections.Generic;

namespace AoC2020
{
    class Program
    {
        static List<int> readInput(string fileName)
        {
            List<int> inputList = new List<int>();
            string[] lines = System.IO.File.ReadAllLines(@"../../Inputs/" + fileName);

            foreach (string line in lines)
            {
                inputList.Add(Int32.Parse(line));
            }

            return inputList;
        }

        static public int day1P1()
        {
            List<int> input = readInput("day1");

            for (int first = 0; first < input.Count; first++)
            {
                for (int second = 0; second < input.Count; second++)
                {
                    if (first != second)
                    {
                        if (input[first] + input[second] == 2020)
                        {
                            return input[first] * input[second];
                        }
                    }
                }
            }

            return 0;
        }

        static public int day1P2()
        {
            List<int> input = readInput("day1");

            for (int first = 0; first < input.Count; first++)
            {
                for (int second = 0; second < input.Count; second++)
                {
                    for (int third = 0; third < input.Count; third++)
                    {
                        if (first != second && first != third && second != third)
                        {
                            if (input[first] + input[second] + input[third] == 2020)
                            {
                                return input[first] * input[second] * input[third];
                            }
                        }
                    }
                }
            }

            return 0;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Day 1 - Part1: " + day1P1());
            Console.WriteLine("Day 1 - Part2: " + day1P2());

            Console.ReadLine();
        }
    }
}
