function changeText() {
    $('header').text("New Header!!!");
}
$('#update_header').on("click", changeText);