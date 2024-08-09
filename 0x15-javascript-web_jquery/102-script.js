/* global $ */

document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + languageCode, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
