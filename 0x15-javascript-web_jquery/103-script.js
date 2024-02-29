$(document).ready(function () {
    const languageInput = $('#language_code');
    const translateButton = $('#btn_translate');
    const helloDiv = $('#helloo');
    translateButton.click(function () {
      const languageCode = languageInput.val();
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
        const helloTranslation = data.hello;
        helloDiv.text(helloTranslation);
      });
    });
    languageInput.keypress(function (event) {
      if (event.which === 13) {
        translateButton.click();
      }
    });
  });