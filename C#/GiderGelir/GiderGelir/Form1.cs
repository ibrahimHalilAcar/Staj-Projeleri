namespace GiderGelir
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public void ToplamlariGuncelle()
        {
            decimal toplamGelir = 0, toplamGider = 0;

            foreach (DataGridViewRow row in dataGridView1.Rows)
            {
                if (row.IsNewRow) continue;
                decimal g = 0, gid = 0;
                decimal.TryParse(Convert.ToString(row.Cells[1].Value), out g);
                decimal.TryParse(Convert.ToString(row.Cells[2].Value), out gid);

                toplamGelir += g;
                toplamGider += gid;
            }

            label1.Text = "Toplam Gelir: " + toplamGelir.ToString("N2");
            label2.Text = "Toplam Gider: " + toplamGider.ToString("N2");
            label3.Text = "Bakiye: " + (toplamGelir - toplamGider).ToString("N2");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridView1.Columns.Clear();
            dataGridView1.ColumnCount = 3;
            dataGridView1.Columns[0].Name = "Tarih";
            dataGridView1.Columns[1].Name = "Gelir";
            dataGridView1.Columns[2].Name = "Gider";
            dataGridView1.AllowUserToAddRows = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            decimal gelir = 0, gider = 0;
            bool gelirOk = decimal.TryParse(textBox1.Text, out gelir);
            bool giderOk = decimal.TryParse(textBox2.Text, out gider);

            if (gelirOk || giderOk)
            {
                dataGridView1.Rows.Add(
                    dateTimePicker1.Value.ToShortDateString(),
                    gelirOk ? gelir.ToString("N2") : "0",
                    giderOk ? gider.ToString("N2") : "0"
                );

                ToplamlariGuncelle();

                textBox1.Clear();
                textBox2.Clear();
            }
            else
            {
                MessageBox.Show("Lütfen en az bir alana geçerli deðer girin!");
            }
        }
    }
}
