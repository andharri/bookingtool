<?php

define('ROOT_DIR', '../');

require_once(ROOT_DIR . 'Pages/TermsOfServicePage.php');

$page = new TermsOfServicePage();
$page->PageLoad();
