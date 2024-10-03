using ARTI.Models;
using Python.Runtime;

namespace ARTI.Services
{
    public class PythonTimeSeriesService
    {
        public dynamic Predict(TimeSeriesInputModel input)
        {
                using (Py.GIL()) 
                {
                    
                    dynamic os = Py.Import("os");
                    dynamic sys = Py.Import("sys");
                    
                    string currentDir = os.getcwd();
                    Console.WriteLine($"Python working directory: {currentDir}");

                    
                    bool fileExists = os.path.exists("Services/TimeSeriesModel.py");
                    Console.WriteLine($"TimeSeriesModel.py exists: {fileExists}");

                    
                    if (fileExists)
                    {
                        sys.path.append(os.path.join(currentDir, "Services"));
                        dynamic timeSeriesModel = Py.Import("TimeSeriesModel");
                        

                        dynamic np = Py.Import("numpy");

                        
                        dynamic npInputArray = np.array(input.Features); 
                        
                        dynamic result = timeSeriesModel.predict_timeseries(npInputArray);

                        
                        List<double> predictions = new List<double>();
                        foreach (var value in result)
                        {
                            predictions.Add((double)value[0]);  
                        }

                        return predictions;
                    }
                    else
                    {
                        Console.WriteLine("TimeSeriesModel.py not found in the current directory.");
                        return null;
                    }
                }
         
        }
    }
}
