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

// TEAMS PAGE

function toggleDescription(id) {
    var desc = document.getElementById(id);
    var allDescriptions = document.querySelectorAll('.team-description');

    allDescriptions.forEach(function(description) {
        description.style.display = 'none';
    });

    if (desc.style.display === 'none' || desc.style.display === '') {
        desc.style.display = 'block';
    } else {
        desc.style.display = 'none';
    }
}


// function isElementInViewport(el) {
//     const rect = el.getBoundingClientRect();
//     return (
//         rect.top >= 0 &&
//         rect.left >= 0 &&
//         rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
//         rect.right <= (window.innerWidth || document.documentElement.clientWidth)
//     );
// }

// // Function to add the 'visible' class to portraits when they are in the viewport
// function handleScroll() {
//     const portraits = document.querySelectorAll('.portrait');
//     portraits.forEach(function(portrait) {
//         if (isElementInViewport(portrait)) {
//             portrait.classList.add('visible');
//         }
//     });
// }

// // Listen for scroll events
// window.addEventListener('scroll', handleScroll);

// // Initial check when the page loads
// window.addEventListener('load', handleScroll);