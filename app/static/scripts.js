
//// MOBILE NAVBAR ///////

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

document.addEventListener('click', function(event) {
    var navbarItems = document.getElementById('navbar_items');
    var hamburgerMenu = document.getElementById('hamburger_menu');

    if (!navbarItems.contains(event.target) && !hamburgerMenu.contains(event.target)) {
        navbarItems.classList.remove('show');
        navbarItems.classList.add('hide');
    }
});

///////////////////////////////



document.addEventListener("DOMContentLoaded", function () {
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
document.addEventListener("DOMContentLoaded", function () {
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



// CAROUSEL
const carouselSlide = document.getElementById('carouselSlide');
const images = carouselSlide.getElementsByTagName('img');
const totalImages = images.length;
let counter = 0;

document.getElementById('nextBtn').addEventListener('click', () => {
    if (counter >= totalImages - 1) {
        counter = 0;
    } else {
        counter++;
    }
    updateCarousel();
    updateMainImage(images[counter].src);
});

document.getElementById('prevBtn').addEventListener('click', () => {
    if (counter <= 0) {
        counter = totalImages - 1;
    } else {
        counter--;
    }
    updateCarousel();
    updateMainImage(images[counter].src);
});

function updateCarousel() {
    const size = images[0].clientWidth;
    carouselSlide.style.transform = `translateX(${-size * counter}px)`;
}

function updateMainImage(src) {
    document.getElementById('mainImage').src = src;
}

