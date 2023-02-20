$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done((data) => {
    const movies = data.results;
    $.each(movies, (index, movie) => {
      const movieTitle = $('<li></li>').text(movie.title);
      $('UL#list_movies').append(movieTitle);
    });
  });
