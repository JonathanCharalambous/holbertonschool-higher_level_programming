fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        const list = document.querySelector("#list_movies");

        movies.forEach(val => {
            const movie = document.createElement("li");
            movie.textContent += val.title;
            list.appendChild(movie);
        });
    });
