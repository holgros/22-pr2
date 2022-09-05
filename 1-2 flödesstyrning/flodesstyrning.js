// truthy och falsy i JavaScript
console.log(0 == false);	// true, 0 är "falsy", dvs. tolkas som falskt i logiska utvärderingar
console.log("" == false);	// true, tom sträng är "falsy"
if ("false") console.log("Alla icke-tomma textsträngar är 'truthy'!");
if (false) console.log("Detta skrivs inte ut!");

// Skillnad mellan == och === i JavaScript
console.log(2 == "2");		// true, samma värde
console.log(2 === "2");		// false, olika datatyper
// kontrastera användning av == ovan
console.log(0 === false);	// false, olika datatyper
console.log("" === false);	// false, olika datatyper
console.log("false" === true);  // false, olika datatyper

// En paradox
console.log("" == "0");	// false, olika textsträngar
console.log(0 == "");	// true, både 0 och tom sträng är "falsy"
console.log("0" == 0);  // true, implicit omtypning av textsträngen "0" till heltalet 0

// Paradoxens upplösning
console.log("" === "0");    // false
console.log(0 === "");	    // false
console.log(0 === "0");	    // false
