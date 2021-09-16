(function() {
    "use strict";

    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
        el = el.trim()
        if (all) {
            return [...document.querySelectorAll(el)]
        } else {
            return document.querySelector(el)
        }
    }

    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all)
        if (selectEl) {
            if (all) {
                selectEl.forEach(e => e.addEventListener(type, listener))
            } else {
                selectEl.addEventListener(type, listener)
            }
        }
    }

    /**
     * Easy on scroll event listener 
     */
    const onscroll = (el, listener) => {
        el.addEventListener('scroll', listener)
    }

    /**
     * Navbar links active state on scroll
     */
    let navbarlinks = select('#navbar .scrollto', true)
    const navbarlinksActive = () => {
        let position = window.scrollY + 200
        navbarlinks.forEach(navbarlink => {
            if (!navbarlink.hash) return
            let section = select(navbarlink.hash)
            if (!section) return
            if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
                navbarlink.classList.add('active')
            } else {
                navbarlink.classList.remove('active')
            }
        })
    }
    window.addEventListener('load', navbarlinksActive)
    onscroll(document, navbarlinksActive)

    /**
     * Scrolls to an element with header offset
     */
    const scrollto = (el) => {
        let header = select('#header')
        let offset = header.offsetHeight

        let elementPos = select(el).offsetTop
        window.scrollTo({
            top: elementPos - offset,
            behavior: 'smooth'
        })
    }

    /**
     * Toggle .header-scrolled class to #header when page is scrolled
     */
    let selectHeader = select('#header')
    let selectTopbar = select('#topbar')
    if (selectHeader) {
        const headerScrolled = () => {
            if (window.scrollY > 100) {
                selectHeader.classList.add('header-scrolled')
                if (selectTopbar) {
                    selectTopbar.classList.add('topbar-scrolled')
                }
            } else {
                selectHeader.classList.remove('header-scrolled')
                if (selectTopbar) {
                    selectTopbar.classList.remove('topbar-scrolled')
                }
            }
        }
        window.addEventListener('load', headerScrolled)
        onscroll(document, headerScrolled)
    }

    /**
     * Back to top button
     */
    let backtotop = select('.back-to-top')
    if (backtotop) {
        const toggleBacktotop = () => {
            if (window.scrollY > 100) {
                backtotop.classList.add('active')
            } else {
                backtotop.classList.remove('active')
            }
        }
        window.addEventListener('load', toggleBacktotop)
        onscroll(document, toggleBacktotop)
    }

    /**
     * Mobile nav toggle
     */
    on('click', '.mobile-nav-toggle', function(e) {
        select('#navbar').classList.toggle('navbar-mobile')
        this.classList.toggle('bi-list')
        this.classList.toggle('bi-x')
    })

    /**
     * Mobile nav dropdowns activate
     */
    on('click', '.navbar .dropdown > a', function(e) {
        if (select('#navbar').classList.contains('navbar-mobile')) {
            e.preventDefault()
            this.nextElementSibling.classList.toggle('dropdown-active')
        }
    }, true)

    /**
     * Scroll with ofset on links with a class name .scrollto
     */
    on('click', '.scrollto', function(e) {
        if (select(this.hash)) {
            e.preventDefault()

            let navbar = select('#navbar')
            if (navbar.classList.contains('navbar-mobile')) {
                navbar.classList.remove('navbar-mobile')
                let navbarToggle = select('.mobile-nav-toggle')
                navbarToggle.classList.toggle('bi-list')
                navbarToggle.classList.toggle('bi-x')
            }
            scrollto(this.hash)
        }
    }, true)

    /**
     * Scroll with ofset on page load with hash links in the url
     */
    window.addEventListener('load', () => {
        if (window.location.hash) {
            if (select(window.location.hash)) {
                scrollto(window.location.hash)
            }
        }
    });

    /**
     * Preloader
     */
    let preloader = select('#preloader');
    if (preloader) {
        window.addEventListener('load', () => {
            preloader.remove()
        });
    }

    /**
     * Menu isotope and filter
     */
    window.addEventListener('load', () => {
        let menuContainer = select('.menu-container');
        if (menuContainer) {
            let menuIsotope = new Isotope(menuContainer, {
                itemSelector: '.menu-item',
                layoutMode: 'fitRows'
            });

            let menuFilters = select('#menu-flters li', true);

            on('click', '#menu-flters li', function(e) {
                e.preventDefault();
                menuFilters.forEach(function(el) {
                    el.classList.remove('filter-active');
                });
                this.classList.add('filter-active');

                menuIsotope.arrange({
                    filter: this.getAttribute('data-filter')
                });
                menuIsotope.on('arrangeComplete', function() {
                    AOS.refresh()
                });
            }, true);
        }

    });

    /**
     * Initiate glightbox 
     */
    const glightbox = GLightbox({
        selector: '.glightbox'
    });

    /**
     * Events slider
     */
    new Swiper('.events-slider', {
        speed: 700,
        loop: true,
        autoplay: {
            delay: 15000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true
        }
    });

    /**
     * Testimonials slider
     */
    new Swiper('.testimonials-slider', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20
            },

            1200: {
                slidesPerView: 3,
                spaceBetween: 20
            }
        }
    });

    /**
     * Initiate gallery lightbox 
     */
    const galleryLightbox = GLightbox({
        selector: '.gallery-lightbox'
    });

    /**
     * Animation on scroll
     */
    window.addEventListener('load', () => {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        })
    });

})()



// Add and Remove ingredient buttons:

const ingredientRow = document.querySelector(".ingredients-row");
const ingredientContainer = document.querySelector(".add-recipe-ingredients-field");
const addIngredientInput = document.getElementById("ingredient-input");
const addIngredientButton = document.querySelector(".add-ingredient-btn");
const extraIngredients = document.querySelector(".extra-ingredients");

let nextIngredientId = 1;

addIngredientButton.addEventListener("click", addIngredient);

function addIngredient(event) {
    event.preventDefault();
    let newIngredientContainer = document.createElement("div");
    newIngredientContainer.classList = "col-md-9 form-group mb-3";


    let newIngredientInputElement = document.createElement("input");
    newIngredientInputElement.id = `ingredient-input`;
    newIngredientInputElement.dataset.id = `${nextIngredientId}`;
    newIngredientInputElement.classList = "form-control";
    newIngredientInputElement.type = "text";
    newIngredientInputElement.value = addIngredientInput.value;
    newIngredientInputElement.value = "";
    newIngredientInputElement.placeholder = `Ingredient..`;
    newIngredientInputElement.name = "recipe_ingredients";

    let removeIngredientButton = document.createElement("button");
    removeIngredientButton.dataset.id = `${nextIngredientId}`;
    removeIngredientButton.classList = "col-md-3 col-sm-9 mx-auto mt-0 mb-3 remove-ingredient-btn ingredient-button";
    removeIngredientButton.innerText = "Remove Ingredient";

    removeIngredientButton.addEventListener("click", removeIngredient);

    newIngredientContainer.appendChild(newIngredientInputElement);
    ingredientContainer.appendChild(newIngredientContainer);
    ingredientContainer.appendChild(removeIngredientButton);
    nextIngredientId += 1;
}


function removeIngredient(event) {
    event.preventDefault();
    let removebtns = document.querySelectorAll(".remove-ingredient-btn");
    let inputs = document.querySelectorAll(`input[data-id]`);
    for (let i = 0; i < removebtns.length; i++) {
        removebtns[i].addEventListener("click", function(event) {
            if (this.dataset.id == inputs[i].dataset.id) {
                inputs[i].remove();
                this.remove();
            }
        });
    }
    nextIngredientId -= 1;
}


// Add and Remove ingredient buttons:
const methodContainer = document.querySelector(".add-method-field");
const addInstructionInput = document.getElementById("recipe_method");
const addInstructionButton = document.querySelector(".add-method-btn");

let nextInstructionId = 1;

addInstructionButton.addEventListener("click", addInstruction);

function addInstruction(event) {
    event.preventDefault();
    let newMethodContainer = document.createElement("div");
    newMethodContainer.classList = "col-md-9 form-group mb-3";


    let newMethodInputElement = document.createElement("input");
    newMethodInputElement.id = `recipe_method`;
    newMethodInputElement.dataset.instruction = `${nextInstructionId}`;
    newMethodInputElement.classList = "form-control";
    newMethodInputElement.type = "text";
    newMethodInputElement.value = addInstructionInput.value;
    newMethodInputElement.value = "";
    newMethodInputElement.placeholder = `Instruction..`;
    newMethodInputElement.name = "recipe_method";

    let removeInstructionButton = document.createElement("button");
    removeInstructionButton.dataset.instruction = `${nextInstructionId}`;
    removeInstructionButton.classList = "col-md-3 col-sm-9 mx-auto mt-0 mb-3 remove-method-btn";
    removeInstructionButton.innerText = "Remove Instruction";

    removeInstructionButton.addEventListener("click", removeInstruction);

    newMethodContainer.appendChild(newMethodInputElement);
    methodContainer.appendChild(newMethodContainer);
    methodContainer.appendChild(removeInstructionButton);
    nextInstructionId += 1;
}


function removeInstruction(event) {
    event.preventDefault();
    let removebtns = document.querySelectorAll(".remove-method-btn");
    let inputs = document.querySelectorAll(`input[data-instruction]`);
    for (let i = 0; i < removebtns.length; i++) {
        removebtns[i].addEventListener("click", function(event) {
            if (this.dataset.instruction == inputs[i].dataset.instruction) {
                inputs[i].remove();
                this.remove();
            }
        });
    }
    nextInstructionId -= 1;
}


// EmailJS
(function () {
    emailjs.init("user_yu6FXmAZKAhYkMOild236");
})();

function sendMail(params){
    let temporaryParameters = {
        subject: document.getElementById("subject").value,
        email: document.getElementById("email").value,
        from_name: document.getElementById("name").value,
        message: document.getElementById("message").value
    };

    emailjs.send("service_puljn4s", "template_p2it8zs", temporaryParameters)
    .then(function(res){
        console.log("success", res.status);
    })
}
