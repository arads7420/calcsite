window.addEventListener('load', () => {
    const navSlide = () => {
        const navBurger = document.getElementById('burger');
        const navLinks = document.getElementById('navlinks');
        navBurger.addEventListener('click', () => {
            navLinks.classList.toggle('nav-active');
            //Burger animation
            navBurger.classList.toggle('toggle');
        });
    }


    navSlide();

    const headerBtns = document.querySelectorAll('.accordion-header');

    headerBtns.forEach(headerBtn => {
        headerBtn.addEventListener('click', (e) => {
            const panel = headerBtn.nextElementSibling;
            panel.classList.toggle('active');
        });
    })

});
