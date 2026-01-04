<?php
// anket.php - Basit tek dosyalık anket
$soru = "Hangi programlama dilini tercih edersiniz?";
$secenekler = ["PHP", "JavaScript", "Python", "Java"];
$dosya = __DIR__ . '/oylar.txt';

// Eğer dosya yoksa oluştur (her satır: "Seçenek:0")
if (!file_exists($dosya)) {
    $satirlar = [];
    foreach ($secenekler as $s) $satirlar[] = $s . ':0';
    file_put_contents($dosya, implode(PHP_EOL, $satirlar));
}

// Oyları varsayılan 0 ile başlat
$oylar = array_fill_keys($secenekler, 0);

// Dosyadan güvenli şekilde oku (bozuk satırları yok say)
if (is_readable($dosya)) {
    $lines = file($dosya, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lines as $line) {
        $parts = explode(':', $line, 2); // limit 2, böylece hata olmaz
        if (count($parts) === 2) {
            $isim = trim($parts[0]);
            $sayi = (int) trim($parts[1]);
            if (array_key_exists($isim, $oylar)) {
                $oylar[$isim] = $sayi;
            }
        }
    }
}

$message = "";

// POST geldiyse ve seçim yapılmışsa kaydet
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['secenek']) && $_POST['secenek'] !== '') {
        $secim = (int) $_POST['secenek'];
        if (isset($secenekler[$secim])) {
            $isim = $secenekler[$secim];
            $oylar[$isim]++;

            // Dosyaya yaz (her satır "Seçenek:oy")
            $out = [];
            foreach ($secenekler as $s) {
                $out[] = $s . ':' . $oylar[$s];
            }
            // LOCK_EX ile yaz
            file_put_contents($dosya, implode(PHP_EOL, $out), LOCK_EX);

            $message = "Oyunuz kaydedildi.";
        } else {
            $message = "Geçersiz seçim.";
        }
    } else {
        $message = "Lütfen bir seçenek seçin.";
    }
}

// Toplam oy
$toplam = array_sum($oylar);
?>
<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <title>Basit Anket</title>
</head>
<body>
  <h2><?= htmlspecialchars($soru) ?></h2>

  <!-- Anket formu (çok basit, eski görünümle aynı) -->
  <form method="post">
    <?php foreach ($secenekler as $i => $sec): ?>
      <label>
        <input type="radio" name="secenek" value="<?= $i ?>"> <?= htmlspecialchars($sec) ?>
      </label><br>
    <?php endforeach; ?>
    <button type="submit">Oy Ver</button>
  </form>

  <?php if ($message !== ""): ?>
    <p><em><?= htmlspecialchars($message) ?></em></p>
  <?php endif; ?>

  <h3>Sonuçlar</h3>
  <?php if ($toplam > 0): ?>
    <ul>
      <?php foreach ($oylar as $isim => $sayi): 
        $yuzde = round(($sayi / $toplam) * 100, 1);
      ?>
        <li><?= htmlspecialchars($isim) ?>: <?= $sayi ?> oy (<?= $yuzde ?>%)</li>
      <?php endforeach; ?>
    </ul>
    <p><strong>Toplam Oy:</strong> <?= $toplam ?></p>
  <?php else: ?>
    <p>Henüz oy kullanılmadı.</p>
  <?php endif; ?>
</body>
</html>
