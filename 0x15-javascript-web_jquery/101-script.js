$(document).ready(function (){
    function addItem() {
        $('ul.my_list').append('<li>Item</li>');
    }
    function removeItem() {
        $('ul.my_list li').remove('li:last-child');
    }
    function emptyList() {
        $('ul.my_list').empty();
    }
    $('#add_item').on("click", addItem);
    $('#remove_item').on("click", removeItem);
    $('#clear_list').on("click", emptyList);
})