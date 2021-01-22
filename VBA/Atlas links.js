// The code does the following
// 1. Open the relevant atlas page as collection (you can recognise this based on : "VAD_C_" in the URL)
// 2. Expand all the hierarchies on the left (if you run the second time it will collapse, so first reload page)
// 3. Extract all the necessary information from the HTML objects
// 4. Include all the information in clipboard.
// For the GLA Helix this is: https://live.atlas.ey.com/#collection/VAD_C_408113430
// For the Helix Platform this is: https://live.atlas.ey.com/#collection/VAD_C_338381387
// 27 december 2020 - Jan-Jaap Loos

var i; //For the iterations
var text; //Temporary save variable
var textarea = document.createElement("textarea");
// Include logic to save all to 'text'
// Expand all levels of the hierarchy first
	try {
		for (i = 0; i < 100; i++) {
		  document.getElementsByClassName("atlas-icon expcol iconExpand")[i].click();
		}
	}
	catch (e) {
		// nothing
	}
	
// Find the necessary data links and titles
	try {
    	for (i = 0; i < 1000; i++) {
		if (document.getElementsByTagName('a')[i].hash.length == 8) {
			text = text + document.getElementsByTagName('a')[i].outerText + "\t" +
			document.getElementsByTagName('a')[i].href + "\t" +
			document.getElementsByTagName('a')[i].hash + "\t" +
			'none' + "\n"
			;
		} else if (document.getElementsByTagName('a')[i].hash.length == 20) {
			text = text + document.getElementsByTagName('a')[i].outerText + "\t" +
			document.getElementsByTagName('a')[i].href + "\t" +
			document.getElementsByTagName('a')[i].hash + "\t" +
			'#' + document.getElementsByTagName('a')[i].hash.substring(13, 20) + "\n"
			;
		} else {
		  //  If doesn't meet the conditions then no interest ;).
		};
		};
	}
	catch (e) {
		// nothing
	}
// move the items to copy to clipboard
textarea.textContent = text;
textarea.style.position = "fixed";  // Prevent scrolling to bottom of page in Microsoft Edge.
document.body.appendChild(textarea);
textarea.select();
document.execCommand("copy");  // Security exception may be thrown by some browsers.
document.body.removeChild(textarea)

alert("Links are copied to clipboard use CTRL + V to paste");