using ARTI.Models;
using Python.Runtime;

namespace ARTI.Services
{
    public class PythonRegressionService
    {
        public dynamic Predict(RegressionInputModel input)
        {
            using (Py.GIL())
            { 
                
                dynamic os = Py.Import("os");
                dynamic sys = Py.Import("sys");
                
                string currentDir = os.getcwd();
                Console.WriteLine($"Python working directory: {currentDir}");

                
                bool fileExists = os.path.exists("Services/RegressionModel.py");
                Console.WriteLine($"RegressionModel.py exists: {fileExists}");

                
                if (fileExists)
                {
                    sys.path.append(os.path.join(currentDir, "Services"));
                    dynamic regressionModel = Py.Import("RegressionModel");
                    
                    dynamic result = regressionModel.predict_regression(input.Features);

                    
                    List<double> predictions = new List<double>();
                    foreach (var value in result)
                    {
                        predictions.Add((double)value);  
                    }
                    return predictions;
                }
                else
                {
                    Console.WriteLine("RegressionModel.py not found in the current directory.");
                    return null;
                }
            }
        }
       
    }
}
