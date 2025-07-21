document.querySelector("#toggle_header").addEventListener("click", toggleClass);

function toggleClass() {
    if (document.querySelector("header").classList.contains("red")) {
        document.querySelector("header").classList.toggle("green");
    }
    else if (document.querySelector("header").classList.contains("green")) {
        document.querySelector("header").classList.toggle("red");
    }
}