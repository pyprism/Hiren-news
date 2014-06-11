<?php
error_reporting(-1);
ini_set('display_errors', 'On');
require 'vendor/autoload.php';

session_start();

/*require_once( 'Facebook/FacebookSession.php' );
require_once( 'Facebook/FacebookRedirectLoginHelper.php' );
require_once( 'Facebook/FacebookRequest.php' );
require_once( 'Facebook/FacebookResponse.php' );
require_once( 'Facebook/FacebookSDKException.php' );
require_once( 'Facebook/FacebookRequestException.php' );
require_once( 'Facebook/FacebookAuthorizationException.php' );
require_once( 'Facebook/GraphObject.php' );*/
/*
use Facebook\FacebookSession;
use Facebook\FacebookRedirectLoginHelper;
use Facebook\FacebookRequest;
use Facebook\FacebookResponse;
use Facebook\FacebookSDKException;
use Facebook\FacebookRequestException;
use Facebook\FacebookAuthorizationException;
use Facebook\GraphObject;



FacebookSession::setDefaultApplication('721830601168795', 'ad40de14362bf1b4152d2f128dcc640a');

$app = new \Slim\Slim();




//echo $body;

$app->get('/', function () {
    $helper = new FacebookRedirectLoginHelper('https://hiren-news.herokuapp.com/');
    $loginUrl = $helper->getLoginUrl();
    echo $loginUrl;
});
$app->run();*/


use Facebook\FacebookSession;
use Facebook\FacebookRedirectLoginHelper;
use Facebook\FacebookRequest;
use Facebook\FacebookResponse;
use Facebook\FacebookSDKException;
use Facebook\FacebookRequestException;
use Facebook\FacebookAuthorizationException;
use Facebook\GraphObject;

// init app with app id (APPID) and secret (SECRET)
FacebookSession::setDefaultApplication('721830601168795','ad40de14362bf1b4152d2f128dcc640a');

// login helper with redirect_uri
$helper = new FacebookRedirectLoginHelper( 'http://hiren-prism.rhcloud.com/' );

try {
    $session = $helper->getSessionFromRedirect();
} catch( FacebookRequestException $ex ) {
    // When Facebook returns an error
    echo $ex;
} catch( Exception $ex ) {
    // When validation fails or other local issues
    echo $ex;
}

// see if we have a session
if ( isset( $session ) ) {
    // graph api request for user data
    $request = new FacebookRequest( $session, 'GET', '/me' );
    $response = $request->execute();
    // get response
    $graphObject = $response->getGraphObject();

    // print data
    echo  print_r( $graphObject, 1 );
} else {
    // show login url
    echo '<a href="' . $helper->getLoginUrl() . '">Login</a>';
}
