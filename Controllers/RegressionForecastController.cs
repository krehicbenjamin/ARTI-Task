using ARTI.Models;
using ARTI.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace ARTI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RegressionForecastController : ControllerBase
    {
        private readonly PythonRegressionService _pythonRegressionService;

        public RegressionForecastController(PythonRegressionService pythonRegressionService)
        {
            _pythonRegressionService = pythonRegressionService;
        }

        [HttpGet("predict")]
        public IActionResult Predict([FromQuery] RegressionInputModel input)
        {
            var prediction = _pythonRegressionService.Predict(input);
            return Ok(prediction);
        }
    }
}
