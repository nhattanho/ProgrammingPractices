using System;
using System.IO;

// EXCEPTIONS are objects derived from SYSTEM.EXCEPTION
// Many exception types for different scenarios, such as
// NULLREFERENCE, DIVIDEBYZERO, FILENOTFOUND,

namespace TryCatchExceptions
{
    class Program
    {
        static void Main(string[] args)
        {
            // For each try, only one catch is caught
            // the catch throw the error will be caught by outside try-catch
            try
            {
                Console.WriteLine("First Try!");
                try
                {
                    Console.WriteLine("Second Try!");
                    int total = 0;
                    string numberAsString = "two";
                    if (int.TryParse(numberAsString, out total))
                    {
                        Console.WriteLine("Parsing correctly!");
                    }
                    else
                    {
                        //throw new Exception("Parsing incorrectly!");
                        throw new ExampleCustomException("Parsing incorrectly!");
                    }
                }
                catch (FileNotFoundException ex)
                {
                    Console.WriteLine($"Error reading file. Error detail: {ex.Message}");
                }
                catch (FormatException ex)
                {
                    Console.WriteLine("Error reading number " + ex.Message);
                }
                catch (ExampleCustomException ex)
                {
                    Console.WriteLine("ExampleCustomException " + ex.Message);
                    //throw new Exception("Go to last Catch!"); // can't be caught in the current catch block
                    // need to rethrow to be caught in the next Catch
                    //throw;      // preserves the original stack trace of exception
                    // throw ex; // update the StackTrace
                    throw new Exception("Go to outside Catch!"); // update the StackTrace
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Last Catch - " + ex.Message);
                }
                finally // always be touched for the try-catch
                {
                    Console.WriteLine("Done Second Try!");
                }
            }
            catch(Exception ex)
            {
                Console.WriteLine("Last Catch - " + ex.Message);
            }
        }
    }
}
/*Result
First Try!
Second Try!
ExampleCustomException Parsing incorrectly!
Done Second Try!
Last Catch - Go to outside Catch!
*/