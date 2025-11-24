document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener('scroll', () => {
        let current = '';
        document.querySelectorAll('section').forEach(sec => {
            if (window.scrollY >= sec.offsetTop - 200) current = sec.id;
        });
        document.querySelectorAll('nav a').forEach(a => {
            a.classList.remove('active');
            if (a.getAttribute('href') === `#${current}`) a.classList.add('active');
        });
    });
});