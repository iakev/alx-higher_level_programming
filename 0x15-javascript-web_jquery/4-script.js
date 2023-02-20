$('DIV#toggle_header').click(() => {
  if ($('HEADER').hasClass('green')) {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  } else {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  }
});
