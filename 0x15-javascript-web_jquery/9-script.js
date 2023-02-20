$.( document ).ready(() => {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr?callback=?',
    type: 'GET',
    dataType: 'json'
  })
    .done((data) => {
      $('DIV#hello').text(data.hello);
    });
});
