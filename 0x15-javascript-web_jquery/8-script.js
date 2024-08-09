/* global $ */

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, datum) {
    $('#list_movies').append('<li>' + datum.title + '</li>');
  });
});
