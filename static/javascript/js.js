window.onload = function onload() {
    let mainURL = 'http://127.0.0.1:8000/'
    console.log(window.location.href)
    if (window.location.href === mainURL + 'about/') {
        document.querySelectorAll('.nav-list-item a')[0].setAttribute('id', 'active');

    }
    if (window.location.href === mainURL) {
        document.querySelectorAll('.nav-list-item a')[1].setAttribute('id', 'active');
    }
    if (window.location.href === mainURL + 'for_sale/') {
        document.querySelectorAll('.nav-list-item a')[2].setAttribute('id', 'active');
    }
    if (window.location.href === mainURL + 'for_rent/') {
        document.querySelectorAll('.nav-list-item a')[3].setAttribute('id', 'active');
    }
    if (window.location.href === mainURL + 'search_for_client/') {
        document.querySelectorAll('.nav-list-item a')[4].setAttribute('id', 'active');
    }
    if (window.location.href === mainURL + 'manage_ads/') {
        document.querySelectorAll('.nav-list-item a')[5].setAttribute('id', 'active');
    }

    if (window.location.href === mainURL + 'rules/') {
        document.querySelectorAll('.nav-list-item a')[6].setAttribute('id', 'active');
    }

}
