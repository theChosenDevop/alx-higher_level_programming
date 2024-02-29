$(document).ready(function () {
    const redHeaderElement = $('DIV#red_header');
    redHeaderElement.click(() => {
        $('header').addClass('red');
    })
})