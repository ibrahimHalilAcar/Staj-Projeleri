using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using BasicEfCore.Models;

namespace BasicEfCore.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly VeriTabani context;

    public HomeController(ILogger<HomeController> logger, VeriTabani context)
    {
        _logger = logger;
        this.context = context;
    }

    public IActionResult Index()
    {
        var a = context.Personals.ToList();
        return View(a);
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
