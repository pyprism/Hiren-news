<?php
/**
 * Created by PhpStorm.
 * User: prism
 * Date: 5/25/14
 * Time: 10:01 AM
 */

/*URL: http://api.ihackernews.com/post/{id}
{id} is the integer ID of the post.*/

error_reporting(-1);
ini_set('display_errors', 'On');

require '../vendor/autoload.php';

use GuzzleHttp\Client;

$client = new Client();
$response = $client->get('http://api.ihackernews.com/page');
$body = json_decode($response->getBody(), true);
$counter = count($body['items']);
for($a = 0 ; $a < $counter ; $a++ ){
    $url = $client->get('http://api.ihackernews.com/post/' . $body['items'][$a]['url'] );
    //echo $body['items'][$a]['title'] ." " .$body['items'][$a]['url'] . '<br>';
    echo $body['items'][$a]['title'] . "    " .$url;
}
//echo  $response->getBody();
//echo count($body['items']);
//echo $body['items'][0]['title'];

