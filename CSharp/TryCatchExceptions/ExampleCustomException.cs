using System;
using System.Collections.Generic;
using System.Text;

namespace TryCatchExceptions
{
    public class ExampleCustomException : Exception
    {
        public ExampleCustomException() { }
        public ExampleCustomException(string message) : base(message){ }
        public ExampleCustomException(string message, Exception innerException) : base(message, innerException) { }
    }
}
