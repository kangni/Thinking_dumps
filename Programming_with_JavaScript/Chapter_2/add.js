var report = function (number3) {
	document.getElementById("result").innerHTML = number3;
}

document.getElementById("a_add_b").onclick = function () {
	var a = document.getElementById("number_1").value;
	var b = document.getElementById("number_2").value;
	report(a+b);
};