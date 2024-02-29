$(() => {
    const addItemElement = $('#add_item');
    addItemElement.click(() => {
        const newElement = '<li>Item</li>';
        const listElement = $('.my_list');
        listElement.append(newElement);
    })
});