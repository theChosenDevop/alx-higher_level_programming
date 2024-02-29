$(() => {
    const displayHello = $('#hello');
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
       displayHello.text(data.hello)
    })
})