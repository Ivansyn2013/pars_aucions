function callGetData() {
    fetch('/execute_get_data', {
        method: "POST",
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.result);
            addTableRow(data.result);
        })
}

function addTableRow(data) {
    console.log(data)
}

function saveAuction_indb(claim_number, event) {

    console.log((claim_number))
}

function sendDataToBack(event) {
    let tableData = [];
    let tableRows = document.querySelectorAll('#auction-table tbody tr');
    for (let row_number =0; row_number < tableRows.length; row_number++) {
        let firstRow = tableRows[0];
        let row = tableRows[row_number];
        let rowData = {};
        for (let collumn_number = 0; collumn_number < firstRow.cells.length ; collumn_number++) {
            rowData[firstRow.cells[collumn_number].textContent] = [row.cells[collumn_number].textContent];

        }
        tableData.push(rowData)
    }

    tableData.shift()
    console.log(tableData)

    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/table/get_auction/', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('data send');
            event.target.disabled=true;
        }
    };

    xhr.send(JSON.stringify(tableData))
}