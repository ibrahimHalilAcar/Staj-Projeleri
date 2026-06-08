<?php
// Varsayılan renk (beyaz)
$color = "#ffffff";

// Eğer formdan renk seçildiyse al
if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST["color"])) {
    $color = $_POST["color"];
}
?>
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Renk Kodu Seçici</title>
</head>
<body style="background-color: <?= htmlspecialchars($color) ?>;">

    <form method="post">
        <label>Renk Seçin: </label>
        <input type="color" name="color" value="<?= htmlspecialchars($color) ?>">
        <button type="submit">Uygula</button>
    </form>

    <p>Seçilen renk kodu: <?= htmlspecialchars($color) ?></p>

</body>
</html>
