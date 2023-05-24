<?php
    if (isset($_COOKIE["lang"])) {
        print "lang cookie value: " . $_COOKIE["lang"];
    } else {
        print "lang cookie doesn't exists";
    }
?>