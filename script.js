document.getElementById('translateButton').addEventListener('click', function() {
    translateText();
});

function translateText() {
    var inputText = document.getElementById('inputTextArea').value;
    var sourceLang = document.getElementById('sourceLanguage').value;
    var targetLang = document.getElementById('targetLanguage').value;
    
    fetch('https://api.mymemory.translated.net/get?q=' + inputText + '&langpair=' + sourceLang + '|' + targetLang)
        .then(response => response.json())
        .then(data => {
            document.getElementById('translatedTextArea').value = data.responseData.translatedText;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
