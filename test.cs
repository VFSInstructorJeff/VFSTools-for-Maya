using System;
using System.Diagnostics;
using System.IO;

class Program
{
    static void Main()
    {
        string cwd = Directory.GetCurrentDirectory();       // get cwd
        string filePath = cwd + "/workspaces/VFS_LD.json";  // append workspaces and the JSON file to edit 
        filePath.Replace(@"\", "/");                        // replace all backslashes with forward slashes
        string comparePath = "\"C:/Users/lrenis/Documents/maya/VFSTools/modular_kit\""; // look for specific string in JSON

        try
        {
            // Read lines one by one as you iterate
            IEnumerable<string> lines = File.ReadLines(filePath);
            
            foreach (string line in lines)
            {
                if (line.Contains(comparePath))
                {
                    line = filePath;
                }
                else
                {
                    continue;
                }
            }
        }
        catch (IOException e)
        {
            Console.WriteLine($"An I/O error occurred: {e.Message}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"An error occurred: {e.Message}");
        }
    }
}
