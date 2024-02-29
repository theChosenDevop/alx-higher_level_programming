$(() => {
    const updateHeaderElement = $('DIV#update_header');
    updateHeaderElement.click(() => {
        $('header').text('New Header!!!')
    })
})