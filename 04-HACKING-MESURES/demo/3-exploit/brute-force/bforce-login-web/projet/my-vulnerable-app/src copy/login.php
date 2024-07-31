<?php
session_start();

$users = include 'users.php';

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

if (isset($users[$username]) && $users[$username] === $password) {
    echo "Login successful! Welcome, " . htmlspecialchars($username) . "!";
} else {
    echo "Invalid username or password.";
}
?>
