using BasicEfCore.Models;
using Microsoft.EntityFrameworkCore;

namespace BasicEfCore.Models {
    public class VeriTabani : DbContext {
        public VeriTabani() { }
        public VeriTabani(DbContextOptions<VeriTabani> options) : base (options) { }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlite("Data Source=PersonalYonetimi.db");
        }

        public DbSet<Personal> Personals { get; set; }
    }
}