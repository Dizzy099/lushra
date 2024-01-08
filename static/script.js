function changeColor(link) {
    // Remove the 'active' class from all links
    var links = document.getElementsByTagName('a');
    for (var i = 0; i < links.length; i++) {
        links[i].classList.remove('active');
    }

    // Add the 'active' class to the clicked link
    link.classList.add('active');
}
