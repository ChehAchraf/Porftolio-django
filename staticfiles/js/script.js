
// Initialize AOS
AOS.init({
    duration: 800,
    once: true
});

// Vanta.js Background
VANTA.NET({
    el: "#vanta-bg",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    color: 0x8B5CF6,
    backgroundColor: 0x0F172A,
    points: 10.00,
    maxDistance: 25.00,
    spacing: 16.00
});

// Preloader
window.addEventListener('load', function() {
    const preloader = document.getElementById('preloader');
    setTimeout(function() {
        preloader.style.opacity = '0';
        setTimeout(function() {
            preloader.style.display = 'none';
        }, 500);
    }, 1000);
});

// Mobile Menu Toggle
const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

menuToggle.addEventListener('click', function() {
    mobileMenu.classList.toggle('hidden');
});

// Header Scroll Effect
const header = document.getElementById('header');

window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
        header.classList.add('bg-darker/80', 'backdrop-blur-md', 'shadow-md');
    } else {
        header.classList.remove('bg-darker/80', 'backdrop-blur-md', 'shadow-md');
    }
});

// Back to Top Button
const backToTopButton = document.getElementById('back-to-top');

window.addEventListener('scroll', function() {
    if (window.scrollY > 300) {
        backToTopButton.classList.remove('opacity-0', 'invisible');
        backToTopButton.classList.add('opacity-100', 'visible');
    } else {
        backToTopButton.classList.add('opacity-0', 'invisible');
        backToTopButton.classList.remove('opacity-100', 'visible');
    }
});

backToTopButton.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Current Year
document.getElementById('current-year').textContent = new Date().getFullYear();

// Progress Bar Animation
const progressBars = document.querySelectorAll('.progress-bar-fill');

const animateProgressBars = () => {
    progressBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
            bar.style.width = width;
        }, 100);
    });
};

// Animate progress bars when they come into view
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateProgressBars();
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

if (document.querySelector('#skills')) {
    observer.observe(document.querySelector('#skills'));
}

// Active Navigation Link
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', function() {
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (window.scrollY >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('text-primary');
        if (link.getAttribute('href').includes(current)) {
            link.classList.add('text-primary');
        }
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
            mobileMenu.classList.add('hidden');
        }
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});
