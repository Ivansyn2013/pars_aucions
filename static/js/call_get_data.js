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