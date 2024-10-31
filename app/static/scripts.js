
//////////////////////////// HOME PAGE FADE IN BANNER TEXT//////////////////////////////////
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



//////////////////////////About Dropdown//////////////////
function toggleDropdown() {
    const dropdownContent = document.querySelector('.dropdown-content');
    if (dropdownContent.classList.contains('show')) {
        dropdownContent.classList.remove('show');
    } else {
        dropdownContent.classList.add('show');
    }
}

document.querySelector('.dropbtn').addEventListener('click', function (e) {
    e.preventDefault();
    toggleDropdown();
});



//////////////////////////////// GOOGLE MAPS JAVA SCRIPT FOR FILTERING //////////////////////////////////
document.addEventListener('DOMContentLoaded', function () {
    // Toggle filter visibility
    document.getElementById('filter-button').addEventListener('click', function() {
        console.log('yay');
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


/////////////////////////////////////////////// RENTAL SCROLLING FUNCTIONALITY /////////////////////////////////

// Declare the slideIndices array in the global scope so it can be accessed in all functions
let slideIndices = [];

// Ensure DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    const carousels = document.querySelectorAll('.rental-image-carousel');
    
    // Initialize the slideIndices array and show the first image for each carousel
    carousels.forEach((carousel, index) => {
        slideIndices[index] = 0;  // Set initial index for each carousel
        showSlide(index, slideIndices[index]);  // Show the first image in each carousel
    });
});

// Function to show the slide based on carousel index and slide index
function showSlide(carouselIndex, slideIndex) {
    const carousels = document.querySelectorAll('.rental-image-carousel');
    const carousel = carousels[carouselIndex];  // Get the correct carousel
    const slides = carousel.querySelectorAll('img');  // Get all images in the carousel
    const totalSlides = slides.length;

    // Wrap around if the slideIndex is out of bounds
    if (slideIndex >= totalSlides) {
        slideIndices[carouselIndex] = 0;
    } else if (slideIndex < 0) {
        slideIndices[carouselIndex] = totalSlides - 1;
    } else {
        slideIndices[carouselIndex] = slideIndex;
    }

    // Hide all slides and show only the current slide
    slides.forEach((slide) => {
        slide.style.opacity = '0';
        slide.style.zIndex = '-1';
    });
    slides[slideIndices[carouselIndex]].style.opacity = '1';
    slides[slideIndices[carouselIndex]].style.zIndex = '1';
}

// Function to move to the next or previous slide
function moveSlide(carouselIndex, step) {
    showSlide(carouselIndex, slideIndices[carouselIndex] + step);
}





//////////////////////RYAN SCRIPTS////////////////////////////////

////////////////////////////////////// Mobile Navbar //////////////////////////////////////
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


//////////////////////////////////////////AGENT BIO COLLAPSIBLE////////////////////////////////////////////////////////////////
function toggleBio(btn, bioId) {
    const bioBtn = document.getElementById(btn);
    const bio = document.getElementById(bioId);
    bio.style.display = (bio.style.display === "none" || bio.style.display === "") ? "block" : "none";
    bioBtn.innerText = (bio.style.display === "none" || bio.style.display === "") ? "Read More" : "Read Less";
}


/////////////////////////////////////////////Property detail collapsible functions//////////////////////////////////////////////

function toggleCollapse(element, icon) {
    const content = element.nextElementSibling;
    const propertyIcon = document.getElementById(icon);
    content.style.display = (content.style.display === "block") ? "none" : "block";
    propertyIcon.innerText = (content.style.display === "block") ? "-" :"+";
  }


//////////////////////////////////////////////// MORTGAGE CALCULATOR //////////////////////////////////////////////////////////
function calculate(loanAmount, interestRate, loanTerm) {
    const monthlyRate = interestRate / 100 / 12; 
    const totalMonths = loanTerm * 12; 
    const monthlyPayment = (loanAmount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -totalMonths));
    console.log(monthlyPayment);
    return monthlyPayment;
    
}

// Get data needed to calculate
function calculateMortgage(loanAmountId, downPaymentPercentageId, interestRateId, loanTermId, paymentId) {
    const loanAmount = parseFloat(document.getElementById(loanAmountId).value);
    const downPaymentPercentage = parseFloat(document.getElementById(downPaymentPercentageId).value);
    const interestRate = parseFloat(document.getElementById(interestRateId).value);
    const loanTerm = parseFloat(document.getElementById(loanTermId).value);
    const payment = document.getElementById(paymentId);
    
    // Calculate the actual loan amount after the down payment
    const downPaymentAmount = loanAmount * (downPaymentPercentage / 100);
    const effectiveLoanAmount = loanAmount - downPaymentAmount;
    const monthlyPayment = calculate(effectiveLoanAmount, interestRate, loanTerm);
    
    // Display Payment
    if (!isNaN(monthlyPayment) && (monthlyPayment !== Infinity) && (monthlyPayment > 0)) {
        payment.innerText = `Monthly Payment: $${monthlyPayment.toFixed(2)}`;
    } else {
        payment.innerText = 'Please enter valid values';
    }
}
