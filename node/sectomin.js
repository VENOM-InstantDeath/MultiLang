//const prompt = require('prompt-sync')({sigint: true});
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout
});
readline.question('Input time in seconds: ', function(t) {
	if (isNaN(t)) {
		console.log("No se ha ingresado un número");
		process.exit(1);
	}
	t = Number(t);
	console.log(`${Math.trunc(t/60)}:${t%60}`);
	process.exit(0)
});
