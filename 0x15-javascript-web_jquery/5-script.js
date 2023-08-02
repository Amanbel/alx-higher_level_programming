function addElement() {
    $('ul.my_list').append('<li>Item</li>');
}

$('#add_item').on("click", addElement);