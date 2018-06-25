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


/**
Calendar
*/

$('#calendar').datepicker({
    inline: true,
    firstDay: 1,
    showOtherMonths: true,
    dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
});


/*Validator*/
function validateText(id) {
    if ($("#" + id).val() == null || $("#" + id).val() == "") {
        var div = $("#" + id).closest("div");
        div.removeClass("has-success");
        $("#glypcn" + id).remove();
        div.addClass("has-error has-feedback");
        div.append('<span id="glypcn' + id
           + '" class="glyphicon glyphicon-remove form-control-feedback"></span>');
        return false;
    } else {
        var div = $("#" + id).closest("div");
        div.removeClass("has-error");
        $("#glypcn" + id).remove();
        div.addClass("has-success has-feedback");
        div.append('<span id="glypcn' + id
               + '" class="glyphicon glyphicon-ok form-control-feedback"></span>');
        return true;
    }
}


function validateEmail(id)
{
    alert("hi");
    var email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
    if(!email_regex.test($("#"+id).val())) {
        var div = $("#"+id).closest("div");
        div.removeClass("has-success");
        $("#glypcn"+id).remove();
        div.addClass("has-error has-feedback");
        div.append('<span id="glypcn'+id+'" class="glyphicon glyphicon-remove form-control-feedback"></span>');
        return false;
        }
     else {
        var div = $("#"+id).closest("div");
        div.removeClass("has-error");
        $("#glypcn"+id).remove();
        div.addClass("has-success has-feedback");
        div.append('<span id="glypcn'+id+'" class="glyphicon glyphicon-ok form-control-feedback"></span>');
        return true;
    }

}


$(document).ready(function() {
    $("#scheduleMockInterview").click(function() {
        if (!validateText("email")) {
            return false;
        }
        /*
        if (!validateText("contactEmail")) {
            return false;
        }
        if (!validateText("contactMobile")) {
            return false;
        }
        if (!validateText("contactAddress1")) {
            return false;
        }
        if (!validateText("contactCity")) {
            return false;
        }*/
        $("form#scheduler").submit();
    }
);
});//var cardTab = '#card';
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


/**
Calendar
*/

$('#calendar').datepicker({
    inline: true,
    firstDay: 1,
    showOtherMonths: true,
    dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
});


/*Validator*/
//function validateText(id) {
//    if ($("#" + id).val() == null || $("#" + id).val() == "") {
//        var div = $("#" + id).closest("div");
//        div.removeClass("has-success");
//        $("#glypcn" + id).remove();
//        div.addClass("has-error has-feedback");
//        div.append('<span id="glypcn' + id
//           + '" class="glyphicon glyphicon-remove form-control-feedback"></span>');
//        return false;
//    } else {
//        var div = $("#" + id).closest("div");
//        div.removeClass("has-error");
//        $("#glypcn" + id).remove();
//        div.addClass("has-success has-feedback");
//        div.append('<span id="glypcn' + id
//               + '" class="glyphicon glyphicon-ok form-control-feedback"></span>');
//        return true;
//    }
//}


function validateEmail(id)
{
    var email_regex = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    if(!email_regex.test($("#"+id).val())) {
        $(".feedback").remove();
        $("<p class='feedback' style='color:#CC3300;'>Invalid email</p>").insertAfter( "#"+id );
        return false;
        }
     else {
        $(".feedback").remove();
        return true;
    }

}

$("form#scheduler").submit(function (e) {
   var validationFailed = false;
   // do your validation here ...
   if (!validateEmail("email")) {
      e.preventDefault();
      return false;
   }
});

$(document).ready(function() {
    $( "#calendar" ).datepicker({ dateFormat: "yy-mm-dd" });
    $("#calendar").on("change",function(){
        var date_selected = $(this).val();

        // Setting value of form input with id scheduleDate
        $('#scheduleDate').val(date_selected);

        // Call to get availability
        $.ajax({
            url: '/homefood/ajax/availability/',
            data: {
              'date': date_selected
            },
            dataType: 'json',
            success: function (data) {
                var availability = data.availability;
                var availability_length = availability.length
                $("#availability").empty();
                if (availability_length == 0) {
                    $("#availability").append("<h4 class=\"lead\"> Sorry there are no available slots for the date selected :( </h4>");
                } else {
                    $("#availability");
                    for (var i = 0; i < availability_length; i++) {
                        //<button type="button" class="btn btn-default">
                        $("#availability").append("<button id=\"timeButton" + i + "\" type=\"button\" class=\"btn btn-time\""

                                                    + "value=\"" + availability[i] +"\">"
                                                    + availability[i] + "</button>");
                    }
                }

            },
                    // handle a non-successful response
            error : function(xhr, errmsg, err) {
                alert("failure" + ": " + xhr.status + ": " + xhr.responseText);
            }
        });

    });
});

// on clicking on any button with id starting with timebutton - it should set scheduleTime value and
// change color. Rest should get back to 'deactivate color'
$("#availability").on("click", "button[id^='timeButton']", function(){
    var value = $(this).val();
    $('#scheduleTime').val(value);
    // Set all classes to deactivate-color
    $("button[id^='timeButton']").removeClass("btn-time-clicked");
    $(this).addClass("btn-time-clicked");
//    alert($('#scheduleTime').val());
//    alert($('#scheduleDate').val());
});

//$(function(){
//    $('#timeButton').click(function() {
//        alert("Hello");
//    });
//});
