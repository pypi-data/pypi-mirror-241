// const checked = JSON.parse(localStorage.getItem("chkboxDarkMode"));
// let checkbox = null;
//
// $(document).ready(function() {
//     checkbox = $('#chkboxDarkMode')[0];
//
//     if (checked === true) {
//         checkbox.checked = true;
//         document.documentElement.setAttribute('data-bs-theme','dark')
//         document.getElementById('dark-mode-icon').classList.add("bi-sun-fill")
//     }
//
// });
//
// function darkmode() {
//     if (document.documentElement.getAttribute('data-bs-theme') === 'dark') {
//         checkbox.checked = false;
//         localStorage.setItem("chkboxDarkMode", checkbox.checked);
//         document.documentElement.setAttribute('data-bs-theme', 'light')
//         document.getElementById('dark-mode-icon').classList.add("bi-moon-fill")
//         document.getElementById('dark-mode-icon').classList.remove("bi-sun-fill")
//     } else {
//         checkbox.checked = true;
//         localStorage.setItem("chkboxDarkMode", checkbox.checked);
//         document.documentElement.setAttribute('data-bs-theme', 'dark')
//         document.getElementById('dark-mode-icon').classList.remove("bi-moon-fill")
//         document.getElementById('dark-mode-icon').classList.add("bi-sun-fill")
//     }
// }

function setTheme(theme) {
    var body = document.body;
    document.getElementById('themeIcon').className = '';
    var iconClasses = 'bi ';

    var themeOtions = document.getElementsByClassName('theme-dd-option');
    for (var i = 0; i < themeOtions.length; i++) {
        themeOtions.item(i).classList.remove('active');
    }

    if (theme == 'dark') {
        iconClasses += 'bi-moon-stars-fill';
        body.dataset.bsTheme = theme;
        document.getElementById('darkThemeOption').classList.add('active');
    } else if (theme == 'light') {
        iconClasses += 'bi-brightness-high-fill';
        body.dataset.bsTheme = theme;
        document.getElementById('lightThemeOption').classList.add('active');
    } else if (theme == 'os') {
        iconClasses += 'bi-circle-half';
        body.dataset.bsTheme = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)
            ? 'dark'
            : 'light';
        document.getElementById('osThemeOption').classList.add('active');
    }

    document.getElementById('themeIcon').className = iconClasses;
    localStorage.setItem('theme', theme);
}

var siteTheme = (localStorage.getItem('theme') != null)
    ? localStorage.getItem('theme')
    : 'os';
setTheme(siteTheme);