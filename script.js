function translate() {
    const sourceText = document.getElementById("source").value;
    const targetLanguage = document.getElementById("target-language").value;
  
    // Call your preferred translation API and get the translated text
    const translatedText = "Translated text will appear here";
  
    document.getElementById("target").value = translatedText;
}
  
function clearText() {
    document.getElementById("source").value = "";
    document.getElementById("target").value = "";
}