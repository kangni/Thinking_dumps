var number = Math.floor(Math.random() * 100) + 1;
for (var i = 1; i <= 10; i++) {
	var guess = prompt("Enter guess #" + i + " (1, 100)");
	if (guess < number) {
		alert("Too small");
	} else if (guess > number) {
		alert("Too big");
	} else {
		alert("Got it");
		break;
	}
	if (i === 10) {
		alert("That's enough guessing");
	}
}