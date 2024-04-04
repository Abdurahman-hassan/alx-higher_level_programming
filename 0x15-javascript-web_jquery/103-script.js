/* global $ */
$('document').ready(function () {
  function getTranslation () {
    const langCode = $('INPUT#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?';

    $.get(url + $.param({ lang: langCode }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  }

  $('INPUT#btn_translate').click(getTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Check if "Enter" key is pressed
      getTranslation();
    }
  });
});
