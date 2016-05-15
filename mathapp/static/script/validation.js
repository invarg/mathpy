/**
 * Created by ales on 5/8/16.
 */
$(document).ready(function(){
//log in validation
    $('#login').click(function (){
        var unm = $('#user_name').val();
        var ps = $('#password').val();
        $.post('/user_check/',{'user_name': unm, 'password': ps}, function(data){
            //alert(data.res);
            $('#summary').html(data.res);
            if (data.res == "") $('#user-form').submit();
        })
        .done(function() {
            //alert( "second success" );
        })
        .fail(function() {
            //alert( "error" );
        })
        .always(function() {
            //alert("finished");
        });
        return false;
    });
});