
/* Variable Declarations
 * size selection input
 */

const gridHeight = document.getElementById('inputHeight');
const gridWidth = document.getElementById('inputWidth');
const submitButton = document.getElementById('submitInput')
const container = document.getElementById('pixelCanvas');
const colorSelect = document.getElementById('colorPicker');

// Event Listeners
submitButton.addEventListener('click', submitFunc);



/*Functions Declaration
 * Reset the table with values that can change
 */

function resetTable() {
    container.innerHTML = '';   
}

// Submit Function
function submitFunc(g) {
    resetTable()
    g.preventDefault();
    const rows = gridHeight.value;

    const cols = gridWidth.value
    // makeGrid()
    makeGrid(rows, cols);
}

// When size is submitted by the user, call makeGrid()
function makeGrid(rows, cols) {
    let n = 1
    let r = rows
    for (; n <= r; n++) {
        const tableRow = document.createElement('tr')
        container.appendChild(tableRow).classList.add(`tr`)
        tableRow.setAttribute('id', `${n}`)
        let s = 1
	let c = cols
	for (; s <= c; s++) {
            const tableCols = document.createElement('td')
            tableRow.appendChild(tableCols).classList.add(`td`)
            tableCols.setAttribute('id', `${n}x${s}`)
            tableCols.addEventListener('click', function(g){
                tableCols.style.backgroundColor = colorSelect.value;
                });
        }
    }
}


