function callGetData(event) {

    const myForm = event.target.parentNode;
    const formData = new FormData(myForm);

    fetch("/execute_get_data/", {
        method: "POST",
        headers: {
                    "Content-Type": "application/json",
                },
        body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.result);

        }).catch(error => {
            console.log(error)
    })
}


function addTableRow() {
  // Get the input value
  var inputNumber = document.getElementById("input-claim_number").value;
  let firstRow = document.getElementsByTagName("table")[0].rows[0];
  // Send the input value to the Flask endpoint
  fetch('/execute_get_data', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({"claim_number": inputNumber}),
  })
  .then(response => response.json())
  .then(data => {
    // Create a new table row

      var newRow = document.createElement("tr");


    for (let i =0; i < firstRow.cells.length; i++){
        newRow.innerHTML = newRow.innerHTML + "<td>" + data[firstRow.cells[i].textContent] + "</td>"
    }  ;
    newRow.innerHTML = newRow.innerHTML + '<button onClick="sendDataToBack(event);" type="button" class="btn btn-secondary">Добавить в базу</button>';

    // Append the new row to the table
    var tableBody = document.getElementById("auction-table");
    tableBody.appendChild(newRow);

  })
  .catch(error => {
    console.log(error)
  });
}








function saveAuction_indb(claim_number, event) {

    console.log((claim_number))
}

function sendDataToBack(event) {
    let tableData = [];
    let tableRows = event.target.parentNode;
    let firstRow = document.querySelector('#auction-table tbody tr');
    let row = tableRows;
    let rowData = {};
    for (let collumn_number = 0; collumn_number < firstRow.cells.length ; collumn_number++) {
        rowData[firstRow.cells[collumn_number].textContent] = [row.cells[collumn_number].textContent];

        }
        tableData.push(rowData)



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