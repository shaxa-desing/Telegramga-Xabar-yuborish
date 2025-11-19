<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Form</title>
</head>
<body>
    <h2>Contact Form</h2>
    <form action="/send" method="POST">
        <label>Name</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email</label><br>
        <input type="email" name="email" required><br><br>

        <label>Message</label><br>
        <textarea name="message" required></textarea><br><br>

        <button type="submit">Send</button>
    </form>
</body>
</html>
