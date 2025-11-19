<?php

$bot_token = "8363619594:AAGr9fCPAyygxN2-9B6H4wPCIAlIuRn1u4A";
$chat_id = "5833828220";

$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

$text = "
🆕 Yangi so‘rov keldi!

👤 *Ismi:* $name
📧 *Email:* $email
💬 *Xabar:* $message
";

$url = "https://api.telegram.org/bot$bot_token/sendMessage";

$data = [
    'chat_id' => $chat_id,
    'text' => $text,
    'parse_mode' => 'Markdown'
];

file_get_contents($url . "?" . http_build_query($data));

echo "OK";
?>
