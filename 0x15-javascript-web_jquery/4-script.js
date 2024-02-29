$(() => {
    const redHeadElement = $('DIV#toggle_header');
    redHeadElement.click(() => {
        $('header').toggleClass('red green');
    });
});