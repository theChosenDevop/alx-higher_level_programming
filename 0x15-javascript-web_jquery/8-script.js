$(() => {
    const movieListElement = $('#list_movies');
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
        const movieTitles = data.results.map(movie => movie.title);
        movieTitles.forEach(title => {
            const listItem = $('<li>').text(title);
            movieListElement.append(listItem)
        });
    })
})