
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
    
    // const video = document.querySelector('video').playbackRate = 0.5;
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


////////////////////// CAROUSEL //////////////////////////////////////

let currentSlide = 0;
const itemsPerPage = 1 // Number of images to show per view

function moveCarousel(direction) {
    const items = document.querySelectorAll('.grid-item');
    const totalSlides = Math.ceil(items.length / itemsPerPage); // Total number of slides based on items per page

    // Update the current slide index
    currentSlide += direction;

    // Loop the carousel
    if (currentSlide < 0) {
        currentSlide = totalSlides -1; // Prevent going to negative slide index
    } else if (currentSlide >=totalSlides) {
        currentSlide = 0; // Prevent going beyond the last slide
    }

    // Move the carousel
    const carouselInner = document.querySelector('.carousel-inner');
    const offset = -currentSlide * (itemsPerPage * (100 / itemsPerPage)); // Calculate offset based on itemsPerPage
    carouselInner.style.transform = `translateX(${offset}%)`;
}


let currentCarouselSlide = currentSlide;
const carouselItemsPerPage = 5// Number of images to show per view

function moveCarouselSlider(direction) {
    const items = document.querySelectorAll('.grid-item-scroll');
    const totalSlides = Math.ceil(items.length / carouselItemsPerPage); // Total number of slides based on items per page

    // Update the current slide index
    currentCarouselSlide += direction;

    // Loop the carousel
    if (currentCarouselSlide < 0) {
        currentCarouselSlide = totalSlides -1; // Prevent going to negative slide index
    } else if (currentCarouselSlide >= totalSlides) {
        currentCarouselSlide = 0; // Prevent going beyond the last slide
    }

    // Move the carousel
    const carouselInner = document.querySelector('.carousel-inner-scroll');
    const offset = -currentCarouselSlide * (carouselItemsPerPage * (100 / carouselItemsPerPage)); // Calculate offset based on itemsPerPage
    carouselInner.style.transform = `translateX(${offset}%)`;
}

function changeMainImage(imageUrl) {
    document.getElementById("mainImage").src = imageUrl;
  }


////////////////////// MORTGAGE CALCULATOR ///////////////////////////////
function calculateMortgage(loanAmount, interestRate, loanTerm) {
    const monthlyRate = interestRate / 100 / 12; // Monthly interest rate
    const totalMonths = loanTerm * 12; // Total loan term in months

    const monthlyPayment = (loanAmount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -totalMonths));

    return monthlyPayment;
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('mortgage-form');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const loanAmount = parseFloat(document.getElementById('loanAmount').value);
            const downPaymentPercentage = parseFloat(document.getElementById('downPaymentPercentage').value);
            const interestRate = parseFloat(document.getElementById('interestRate').value);
            const loanTerm = parseInt(document.getElementById('loanTerm').value);

            // Calculate the actual loan amount after the down payment
            const downPaymentAmount = loanAmount * (downPaymentPercentage / 100);
            const effectiveLoanAmount = loanAmount - downPaymentAmount;

            const monthlyPayment = calculateMortgage(effectiveLoanAmount, interestRate, loanTerm);
            
            if (!isNaN(monthlyPayment) && (monthlyPayment !== Infinity) && (monthlyPayment > 0)) {
                document.getElementById('monthlyPayment').innerText = `Monthly Payment: $${monthlyPayment.toFixed(2)}`;
            } else {
                document.getElementById('monthlyPayment').innerText = 'Please enter valid values';
            }
        });
    }
});



// ////////////////////////////// GOOGLE MAPS JAVA SCRIPT FOR FILTERING //////////////////////////////////

document.addEventListener('DOMContentLoaded', function () {
    // Toggle filter visibility
    document.getElementById('filter-button').addEventListener('click', function() {
        const filters = document.getElementById('filters');
        if (filters.classList.contains('filters-visible')) {
            filters.classList.remove('filters-visible');
            this.textContent = 'Show Filters';
        } else {
            filters.classList.add('filters-visible');
            this.textContent = 'Hide Filters';
        }
    });

    window.resetFilters = function() { 
        const mlsId = document.getElementById('mls-listing-id');
        const locate = document.getElementById('location');
        const minPrice = document.getElementById('min-price');
        const maxPrice = document.getElementById('max-price');
        const minBeds = document.getElementById('min-beds');
        const minBaths = document.getElementById('min-baths');
        const propertyItems = document.querySelectorAll('.property-item');

        propertyItems.forEach(item => { 
            item.style.display = 'block';
        })

        document.getElementById('filters').classList.remove('filters-visible');
        mlsId.value = null;
        locate.value = null;
        minPrice.value = null;
        maxPrice.value = null;
        minBeds.value = null;
        minBaths.value = null;
        document.getElementById('filter-button').textContent = 'Show Filters';
    };

    // Apply filters and hide filter options
    window.applyFilters = function() {
        const mlsId = document.getElementById('mls-listing-id').value || null;
        const locate = document.getElementById('location').value || null;;
        const minPrice = parseFloat(document.getElementById('min-price').value)|| 0;
        const maxPrice = parseFloat(document.getElementById('max-price').value) || Infinity;
        const minBeds = parseInt(document.getElementById('min-beds').value)|| null;
        const minBaths = parseFloat(document.getElementById('min-baths').value)|| null;
        const propertyItems = document.querySelectorAll('.property-item')|| null;

        propertyItems.forEach(item => {
            const price = parseFloat(item.getAttribute('data-price'));
            const beds = parseInt(item.getAttribute('data-beds'));
            const fullBaths = parseFloat(item.getAttribute('data-full-baths'));
            const halfBaths = parseFloat(item.getAttribute('data-half-baths'));
            const location = item.getAttribute('data-location');
            const mlsNumber = item.getAttribute('data-mls-number');

            let baths = fullBaths +(halfBaths / 2);
            let priceFlag = true;
            let bedsFlag = true;
            let bathsFlag = true;
            let locationFlag = true;
            let mlsFlag = true;
            let mlschecked = false;

            if (mlsId != null){
                mlschecked = true;
            }

            if (mlschecked == true){
                if (mlsId != mlsNumber){
                    mlsFlag = false;
                }
                priceFlag =false;
                bedsFlag = false;
                bathsFlag = false;
                locationFlag = false;
                if (mlsFlag == true){
                    item.style.display = 'block';
                }else{
                    item.style.display = 'none';
                };
            }else if(mlschecked == false){
                
                if (locate != null && location.toUpperCase() != locate.toUpperCase()) {
                    locationFlag = false;
                }
            
                if (price < minPrice || price > maxPrice){
                    priceFlag = false;
                }

                if (beds != null && beds < minBeds){
                    bedsFlag = false;
                }

                if (baths != null && baths < minBaths){
                    bathsFlag = false;
                }
                
                if (priceFlag == true && locationFlag == true && bedsFlag == true && bathsFlag == true){
                    item.style.display = 'block';
                }else{
                    item.style.display = 'none';
                };

            }
        });

        // Hide filters after applying
        document.getElementById('filters').classList.remove('filters-visible');
        document.getElementById('filter-button').textContent = 'Show Filters';
    };
});

// Get commas in infowindow on maps for price, REGEX is dumb
function formatPriceWithCommas(price) {
    return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }

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

function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to add the 'visible' class to portraits when they are in the viewport
function handleScroll() {
    const portraits = document.querySelectorAll('.portrait');
    portraits.forEach(function(portrait) {
        if (isElementInViewport(portrait)) {
            portrait.classList.add('visible');
        }
    });
}

// Listen for scroll events
window.addEventListener('scroll', handleScroll);

// Initial check when the page loads
window.addEventListener('load', handleScroll);




let currentPage = 0;
const propertiesPerPage = 3;

document.addEventListener('DOMContentLoaded', () => {
  showProperties(currentPage);

  document.getElementById('next-button').addEventListener('click', nextPage);
  document.getElementById('prev-button').addEventListener('click', prevPage);
});

function showProperties(page) {
  const allProperties = document.querySelectorAll('.property-item');
  const totalPages = Math.ceil(allProperties.length / propertiesPerPage);
  
  allProperties.forEach((property, index) => {
    if (index >= page * propertiesPerPage && index < (page + 1) * propertiesPerPage) {
      property.style.display = 'block'; // Show the properties for the current page
    } else {
      property.style.display = 'none'; // Hide the rest
    }
  });

  // Disable buttons at the edges
  document.getElementById('prev-button').disabled = page === 0;
  document.getElementById('next-button').disabled = page >= totalPages - 1;
}

function nextPage() {
  const allProperties = document.querySelectorAll('.property-item');
  const totalPages = Math.ceil(allProperties.length / propertiesPerPage);
  
  if (currentPage < totalPages - 1) {
    currentPage++;
    showProperties(currentPage);
  }
}

function prevPage() {
  if (currentPage > 0) {
    currentPage--;
    showProperties(currentPage);
  }
}



// Property detail collapsible functions

function toggleCollapse(element) {
    const content = element.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  }
  
  // Optional: Hide collapsible content by default
  document.querySelectorAll('.content').forEach(content => {
    content.style.display = "none";
  });


  