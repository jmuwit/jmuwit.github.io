<?php

// Replace with your email
$mail_to = 'jmuwit@gmail.com';

if (isset($_POST['name']) && isset($_POST['email']) && filter_var($_POST['email'], FILTER_VALIDATE_EMAIL) && isset($_POST['message']))
{
    // Collect POST data from form
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Prefedined Variables  
    $subject = 'WIT Notification Mailer: Message from ' . $name . '!';

    // Collecting all content in $content
    $content = 'Contact Details:' . "\r\n" ;
    $content .= 'Name: ' . $name . "\r\n" ;
    $content .= 'Email: ' . $email . "\r\n" ;
    $content .= 'Message: ' . $message . "\r\n" ;

    // Detect & prevent header injections
    $test = "/(content-type|bcc:|cc:|to:)/i";
    foreach ($_POST as $key => $val)
    {
        if (preg_match($test, $val))
        {
            exit;
        }
    }

    $headers = 'From: ' . $name . '<' . $email . '>' . "\r\n" .
        'Reply-To: ' . $email . "\r\n" .
        'X-Mailer: PHP/' . phpversion();

    // Send the message
    $send = false;
    if (mail($mail_to, $subject, $content, $headers))
    {
        $send = true;
    }

    echo json_encode($send);
}
