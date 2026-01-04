using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace BasicEfCore.Models
{
    public class Personal
    {
        [Key]
        public int PersonalNo { get; set; }
        public string? Ad { get; set; }
        public string? Soyad { get; set; }
        public string? Adres { get; set; }
        public decimal Maas { get; set; }

    }
}