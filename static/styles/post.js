var field = document.querySelector('input');
var backup = field.getAttribute('placeholder');


field.onfocus = function(){
    this.setAttribute('placeholder', '');
    this.style.borderColor = '#333'
}

field.onblur = function(){
    this.setAttribute('placeholder',backup)
}
