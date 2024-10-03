using ARTI.Models;
using ARTI.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace ARTI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TimeSeriesForecastController : ControllerBase
    {
        private readonly PythonTimeSeriesService _pythonTimeSeriesService;

        public TimeSeriesForecastController(PythonTimeSeriesService pythonTimeSeriesService)
        {
            _pythonTimeSeriesService = pythonTimeSeriesService;
        }

        [HttpGet("predict")]
        public IActionResult Predict([FromQuery] TimeSeriesInputModel input)
        {
            var prediction = _pythonTimeSeriesService.Predict(input);
            return Ok(prediction);
        }
    }
}
