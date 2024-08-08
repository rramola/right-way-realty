function toggleNavbar() {
    var navbarItems = document.getElementById('navbar_items');
    if (navbarItems.classList.contains('show')) {
        navbarItems.classList.remove('show');
        navbarItems.classList.add('hide');
    } else {
        navbarItems.classList.remove('hide');
        navbarItems.classList.add('show');
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