function changeClass() {
    if ($('header').hasClass('red')) {
        $('header').removeClass('red');
        $('header').addClass('green');
    } else {
        $('header').removeClass('green');
        $('header').addClass('red');
    }
}
$("#toggle_header").on("click", changeClass);