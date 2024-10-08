<?php


use Bookstore\Domain\Book ;
use Bookstore\Domain\Customer;

spl_autoload_register(function ($classname) {
    
    $lastSlash = strrpos($classname, '\\') + 1;
    $classname = substr($classname, $lastSlash);
    $directory = str_replace('\\', '/', $classname);
    $filename = __DIR__ . '/Bookstore/Domain/' . $directory . '.php';
    // echo''. $filename .'';
    require_once($filename);
});

$book1 = new Customer(); 

?>
