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


// HOME PAGE FADE IN BANNER TEXT
document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll('#home_page_banner_text .content');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target); // Stop observing once the animation is triggered
            }
        });
    }, {
        threshold: 0.1 // Trigger when 10% of the element is visible
    });

    sections.forEach(section => {
        observer.observe(section);
    });
});