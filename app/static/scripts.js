function toggleNavbar() {
    var navbar = document.querySelector('.vertical-navbar');
    if (navbar.style.width === '200px') {
        navbar.style.width = '0';
    } else {
        navbar.style.width = '200px';
    }
}