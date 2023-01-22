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

const revealButton = document.getElementById("Reveal_button")

// ponizsze nie zadziala bo poniewaz wczesniejsza funkcja to obsluguje

revealButton.addEventListener('onclick', function(){
    console.log("Reveal_button clicked!")
})

function changeBackground() {
        console.log("Reveal_button clicked!")
        document.body.style.backgroundImage = "url('/static/dungeon_entrance.jpg')";
        // dziala! great work!
    }




