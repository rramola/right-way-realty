function toggleNavbar() {
    var navbar = document.querySelector('.vertical-navbar');
    if (navbar.style.width === '200px') {
        navbar.style.width = '0';
    } else {
        navbar.style.width = '200px';
    }
}


document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");

    const options = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("in-view");
                observer.unobserve(entry.target);
            }
        });
    }, options);

    sections.forEach(section => {
        observer.observe(section);
    });
});