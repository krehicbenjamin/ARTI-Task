using ARTI.Services;
using Python.Runtime;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
Runtime.PythonDLL = builder.Configuration["PythonSettings:PythonDLL"];
PythonEngine.PythonHome = builder.Configuration["PythonSettings:PythonHome"];
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

