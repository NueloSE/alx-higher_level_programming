/* global $ */

document.addEventListener('DOMContentLoaded', function () {
  function setHello () {
    const languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + languageCode, function (data) {
      $('#hello').html(data.hello);
    });
  }

  $('#btn_translate').on('click', function () {
    setHello();
  });

  $('#language_code').keydown(function (event) {
    if (event.keydown === 'Enter' || event.keyCode === 13) {
      setHello();
    }
  });
});
