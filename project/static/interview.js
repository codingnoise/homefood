//var cardTab = '#card';
//var paytmTab = "#paytm";
//var instamojoTab = "#instamojo";
//var paypalTab = "#paypal";
//
//$(cardTab).on('click', function(){
//    $('.payment-method-card').show();
//    $('.payment-method-paytm').hide();
//    $('.payment-method-instamojo').hide();
//    $('.payment-method-paypal').hide();
//});
//
//$(paytmTab).on('click', function(){
//    $('.payment-method-card').hide();
//    $('.payment-method-paytm').show();
//    $('.payment-method-instamojo').hide();
//    $('.payment-method-paypal').hide();
//});
//
//$(instamojoTab).on('click', function(){
//    $('.payment-method-card').hide();
//    $('.payment-method-paytm').hide();
//    $('.payment-method-instamojo').show();
//    $('.payment-method-paypal').hide();
//});
//
//$(paypalTab).on('click', function(){
//    $('.payment-method-card').hide();
//    $('.payment-method-paytm').hide();
//    $('.payment-method-instamojo').hide();
//    $('.payment-method-paypal').show();
//});
//
//// A $( document ).ready() block.
//$( document ).ready(function() {
//    $('.payment-method-card').show();
//    $('.payment-method-paytm').hide();
//    $('.payment-method-instamojo').hide();
//    $('.payment-method-paypal').hide();
//});


//$(document).ready(function(){
//    alert("hi");
//    $(".lead").fadeIn(3000);
//});


/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
   $(window).scroll(function() {

    if ($(this).scrollTop()>0)
     {
        $('.nav').fadeOut();
        $('.masthead-brand').fadeOut();
     }
    else
     {
      $('.nav').fadeIn();
      $('.masthead-brand').fadeIn();
     }
 });