function download() {
    let filename = "results.html";

    let style = "<style>.missing-char {    /* color: green; */    color: red;    font-weight: 900;}.extra-char {    background-color: red;    text-decoration: line-through;}</style>";


    let text = style + document.getElementById("results").innerHTML;

    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  }

  const resultDownloadt = document.querySelector('#dd');
    resultDownloadt.onclick = () => {
       download();
  }