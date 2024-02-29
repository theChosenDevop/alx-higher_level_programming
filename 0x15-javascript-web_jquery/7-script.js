$(() => {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
        const setCharacter = $('#character');
        setCharacter.text(data.name);
    })
})