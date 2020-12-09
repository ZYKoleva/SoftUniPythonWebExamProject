window.onload = function onload() {
    let mainURL = 'http://127.0.0.1:8000/'
    console.log(window.location.href)
    if (window.location.href === mainURL + 'about/') {
        console.log(document.querySelectorAll('.nav-list-item a'))
        document.querySelectorAll('.nav-list-item a')[1].setAttribute('id', 'active');

    }
    if (window.location.href === mainURL) {
        document.querySelectorAll('.nav-list-item a')[2].setAttribute('id', 'active');
    }
    if (window.location.href === mainURL + 'general_rules/') {
        document.querySelectorAll('.nav-list-item a')[3].setAttribute('id', 'active');
    }
}
