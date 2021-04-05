// ==UserScript==
// @name         Latin text selection and macron remover
// @namespace    https://www.clc.cambridgescp.com/
// @version      0.1
// @description  enables text selection in cambridge latin when you press f, removes macrons
// @author       Edward
// @match        https://www.clc.cambridgescp.com/web-book-*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    document.body.addEventListener('keypress', (event) => {
        if (event.code == 'KeyF') {
            for (let i of document.body.querySelectorAll("p, dd, dt, li")) {
                i.innerHTML = i.innerHTML.replace(/ō/g, 'o');
                i.innerHTML = i.innerHTML.replace(/ī/g, 'i');
                i.innerHTML = i.innerHTML.replace(/ē/g, 'e');
                i.innerHTML = i.innerHTML.replace(/ā/g, 'a');
                i.innerHTML = i.innerHTML.replace(/ū/g, 'u');
                i.innerHTML = i.innerHTML.replace(/ȳ/g, 'y');
                i.innerHTML = i.innerHTML.replace(/'/g, '"');
                i.style.userSelect = "text";
            }
        }
    });
})();
