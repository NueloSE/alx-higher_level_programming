/* global $ */

document.addEventListener('DOMContentLoaded', function () {
  const myListEl = $('.my_list');
  $('#add_item').on('click', function () {
    myListEl.append('<li>Item</li>');
  });

  $('#remove_item').on('click', function () {
    $('.my_list li:last').remove();
  });

  $('#clear_list').on('click', function () {
    myListEl.empty();
  });
});
