$(document).ready(function () {
  // Updated URL to reflect the new domain
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
