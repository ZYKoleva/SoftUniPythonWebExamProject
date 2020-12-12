window.onload = function onload() {
    let mainURL = 'http://localhost:8000/'
    if (window.location.href === mainURL + 'about/') {
        document.querySelector('.nav-link-about').setAttribute('id', 'active');
    }
    if (window.location.href === mainURL) {
        document.querySelector('.nav-link-rent-sale').setAttribute('id', 'active');

    }
    if (window.location.href.includes('http://localhost:8000/?page')) {
        document.querySelector('.nav-link-rent-sale').setAttribute('id', 'active');
    }
    if (window.location.href === mainURL + 'general_rules/') {
        document.querySelector('.nav-link-general-rules').setAttribute('id', 'active');
    }
    if (window.location.href.includes(mainURL + 'district/')) {
        document.querySelector('.nav-link-rent-sale').setAttribute('id', 'active');
    }
    if (window.location.href.includes(mainURL + 'area/')) {
        document.querySelector('.nav-link-rent-sale').setAttribute('id', 'active');
    }
    if (window.location.href.includes(mainURL + 'city/')) {
        document.querySelector('.nav-link-rent-sale').setAttribute('id', 'active');
    }
}
