function add_to_table() {
    const exercise_name = document.getElementById("exercise_name").value;
    const exercise_type = document.getElementById("exercise_type").value;
    const duration = document.getElementById("exercise_minute").value;
    const exercise_notes = document.getElementById("exercise_notes").value;
    
    add_row(exercise_name, exercise_type, duration, exercise_notes);
    
}
/*function to add table items*/
function add_row(date, exercise, duration, type, notes) {
    const full_table = document.getElementById("output_table")
    
    const curr_row = document.createElement('tr');
    
    const date_input = document.createElement('td');
    const exercise_input = document.createElement('td');
    const duration_input = document.createElement('td');
    const type_input = document.createElement('td');
    const notes_input = document.createElement('td');
    
    date_input.innerText = date;
    exercise_input.innerText = exercise;
    duration_input.innerText = duration;
    type_input.innerText = type;
    notes_input.innerText = notes;

    curr_row.appendChild(date_input);
    curr_row.appendChild(exercise_input);
    curr_row.appendChild(duration_input);
    curr_row.appendChild(type_input);
    curr_row.appendChild(notes_input);
    
    full_table.appendChild(curr_row);
    
}

function populate_table(){
    console.log("heyo1");

    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
        console.log("heyo");
        if(xmlhttp.readyState == XMLHttpRequest.DONE){
            if(xmlhttp.status == 200){
                //if returned fine
                console.log("hurray");
                let rows = JSON.parse(xmlhttp.responseText);
                for (row of rows){
                    console.log(row);
                    add_row(row[0],row[1],row[2],row[3],row[4]);
                }
            }
            else if(xmlhttp.status == 400){
                // if bad wrong
                console.log('boo! (╯°□°）╯︵ ┻━┻');
            }
            else{
                console.log("return status: ", xmlhttp.status);
            }
        }
    }

    xmlhttp.open("GET", "/populate_table");
    xmlhttp.send();
}

