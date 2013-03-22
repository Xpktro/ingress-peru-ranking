$(document).ready(function() {

    function createAlert(message) {
        $('body').append('<div id="mini-notification"><p>' + message + '</p></div>');
    };

    var alertOptions = {
        closeButton: true,
        closeButtonText: '[cerrar]',
        effect: 'fade',
        time: 10000,
    };

    // The /intel endpoint could show a login screen so we make sure we're in the
    // correct view.
    if($('#player_stats').length > 0) {

        //jQuery madness!
        var nickname_element = $('#player_stats .player_nickname');

        var nickname = nickname_element.html();
        var faction = nickname_element.parent().attr('class');
        var level = $('#player_level').html();
        var ap = $('#ap .number').html();
        var email = $('#header_email').html();
        $.post(
            "http://127.0.0.1:8000/players/",
            {
                'nickname': nickname,
                'faction': faction,
                'level': level,
                'ap': ap,
                'email': email
            }
        ).done(function(data, status) {
            if(status == 'success') {
                position = data['position'];
                nickname_element.append(' (puesto ' + position + ')');
                createAlert('Datos actualizados en el ranking correctamente.');
                $('#mini-notification').miniNotification(alertOptions);
            }
        }).fail(function() {
            createAlert('No se pudo acceder al servicio de ranking. Intente nuevamente recargando la página.');
            $('#mini-notification').css('color', '#ff5555').miniNotification(alertOptions);
        });
    }
});
