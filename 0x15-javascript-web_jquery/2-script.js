$(document).ready(function () {
	const redHeadElement = $('#red_header');
	redHeadElement.click(function () {
		const headerElement = $('header');
		headerElement.css('color', '#FF0000');
	});
});