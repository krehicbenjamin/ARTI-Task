using ARTI.Services;
using Python.Runtime;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
Runtime.PythonDLL = @"C:\Users\User\AppData\Local\Programs\Python\Python311\python311.dll"; //Needed path (would be handled on Virtual Machine in ideal scenario)
PythonEngine.PythonHome = @"C:\Users\User\AppData\Local\Programs\Python\Python311";
PythonEngine.Initialize();
PythonEngine.BeginAllowThreads();

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddScoped<PythonTimeSeriesService>();
builder.Services.AddScoped<PythonRegressionService>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Lifetime.ApplicationStopped.Register(() =>
{
    PythonEngine.Shutdown();
});

app.Run();

