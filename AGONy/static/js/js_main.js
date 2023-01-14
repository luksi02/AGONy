// button-clicker - one to click them all!

const clickedButtons = document.querySelectorAll(".btn")

clickedButtons.forEach(function (button) {
    button.addEventListener('click', function (event) {
        console.log('button was clicked!')
    //     rest of the magic should happen here!
    })
})

const mouseoveredButtons = document.querySelectorAll(".btn")

mouseoveredButtons.forEach(function (button) {
    button.addEventListener('mouseover', function (event) {
        console.log('button was mouseovered!')
    //     rest of the magic should happen here!
    })
})


