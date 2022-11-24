
//GET COOKIE
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function AJAXPromise(method, URL) {
    let data = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : null;
    let processData = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : true;
    let contentType = arguments.length > 4 && arguments[4] !== undefined ? arguments[4] : 'application/x-www-form-urlencoded; charset=UTF-8';
    
    let csrftoken = getCookie('csrftoken');
    return new Promise(function (resolve,completed) {
        $.ajax({
            type: method,
            url: URL,
            headers: {'X-CSRFToken': csrftoken},
            data: data,
            processData: processData,
            contentType: contentType,
            success: function success(data)
            {
                resolve(data);
            },
            complete: function complete(data)
            {
                completed(data);
            }
        });
    });
}


function approveDiable(id)
{
    if(!$('#feescheckbox'+id).is(':checked'))
    {
        $('#appprove_btn'+id).attr( "disabled", true );
    }
    else
    {
        $('#appprove_btn'+id).attr( "disabled", false );
    }
}



//================================LOGIN SECTION
$("#submit").click(function(){
    var email = $('#login-email').val();
    var password = $('#login-password').val();

    data = { 'email' : email, 'password': password  };

    AJAXPromise("POST", "/API/check/", data).then((success_data) => {
        if(success_data.type == "admin"){
            window.location.replace("admin/");
        }
        else if(success_data.type == "student"){
            window.location.replace("student/");
        }
        else{
            $("#loginfailed").css('visibility','visible');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
});
//===============================LOGOUT SECTION
$('#logout').click( () => {
    AJAXPromise("GET", "/API/logout/").then((success_data) => {
        window.location.replace("/");
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
    
} );

//===============================ADMIN SECTION

application_count = () => {
    AJAXPromise("GET", "/API/newApplications/").then((success_data) => {
        
        $('#total-admission-count').html(success_data['data'].length);
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });

    type = 'new'
    let data = { 'type': type  } 
    
    AJAXPromise("GET", "/API/fetchGrieveance/", data).then( (success_data) => {
        
        if ( success_data.message == 'ok'){
            $('#total-grieveance-count').html(success_data['data'].length);
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
}

getStudentCount = () => {
    
    AJAXPromise("GET", "/API/getStudentDetails/").then((success_data) => {
        
        datas = {
            labels: ['Students Joined', 'Total Available Rooms'],
            datasets: [{
                label: '# of Votes',
                data: [success_data.data.length, 60],
                backgroundColor: [
                    'rgba(0, 124, 199, 0.8)',
                    'rgba(77, 168, 218, 0.7)'
                ],
                borderWidth: 1
            }]
        }
        options={
            cutoutPercentage: 50,
            rotation: 2.5,
            circumference: 4.4

        }
        
        //$('#total-student-count').html(success_data.data.length);
        var ctx = $('#myChart');
        var myDoughnutChart = new Chart(ctx, {
            type: 'doughnut',
            data: datas,
            options: options
        });


    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
}

getStudentDetails = () => {
    //console.log('student details called');
    AJAXPromise("GET", "/API/getStudentDetails/").then((success_data) => {
        //console.log(success_data);
        //console.log(success_data.data[0].name);
        $('#student_name').val(success_data.data[0].name);
        $('#intro_student_name').html(success_data.data[0].name);
        $('#student_dob').val(success_data.data[0].dob);
        $('#student_department').val(success_data.data[0].dept);
        $('#student_roll_no').val(success_data.data[0].rollno);
        $('#student_father_name').val(success_data.data[0].fathers_name);
        $('#student_mother_name').val(success_data.data[0].mothers_name);
        $('#student_phone').val(success_data.data[0].phone);
        $('#student_email').val(success_data.data[0].email);
        $('#student_address').val(success_data.data[0].address);
        $('#student_food_type').val(success_data.data[0].food_type);
        $('#student_room_no').val(success_data.data[0].rooms_id);
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
}

initializeCalendar = () => {
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth'
    });
}

getRoomsDetails = () => {
    console.log('student details called');
    AJAXPromise("GET", "/API/getRoomsDetails/").then((success_data) => {
        console.log(success_data);
        for(var i=0;i<success_data.data.length;i++)
        {
            if(success_data.data[i]['present']==0)
            {
                $("#"+success_data.data[i]['rooms_id']).addClass('btn btn-outline-success');
            }
            else if(success_data.data[i]['present']<success_data.data[i]['capacity'])
            {
                $("#"+success_data.data[i]['rooms_id']).addClass('btn btn-outline-warning');
            }
            else if(success_data.data[i]['present']==success_data.data[i]['capacity'])
            {
                $("#"+success_data.data[i]['rooms_id']).addClass('btn btn-outline-danger');
            }
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
}



var date;
loadcalendar = () => {
    var calendarEl = document.getElementById('calendar');
    
    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        initialView: 'dayGridMonth',
        dateClick: function(info) {
                    date = info.dateStr;
                    data = {'date': date};
                    AJAXPromise("POST", "/API/FetchDailyItem/", data).then( (success_data) => {
                        if ( success_data.message == 'ok'){
                            //console.log(success_data.data['lunch']);
                            $('#breakfast').selectpicker('val',success_data.data['breakfast'] ); 
                            $('#lunch').selectpicker('val',success_data.data['lunch'] );
                            $('#dinner').selectpicker('val',success_data.data['dinner'] );
                        }
                    },(error)=>
                    {
                      alert(JSON.stringify(error["responseJSON"],null, 1));
                    });
        }
    });
    calendar.render();
}

var date1;
loadstudentcalendar = () => {
    var calendarEl = document.getElementById('calendar');
    
    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        initialView: 'dayGridMonth',
        dateClick: function(info) {
                    date1 = info.dateStr;
                    data = {'date': date1};
                    AJAXPromise("POST", "/API/FetchDailyItem/", data).then( (success_data) => {
                        if ( success_data.message == 'ok'){
                            console.log('Success');
                            if(success_data.data['breakfast'] == ''){
                                $('#breakfast').val('Not Confirmed'); 
                                $('#lunch').val('Not Confirmed');
                                $('#dinner').val('Not Confirmed');
                                return;
                            }
                            //console.log(success_data.data['lunch']);
                            $('#breakfast').val(success_data.data['breakfast'] ); 
                            $('#lunch').val(success_data.data['lunch'] );
                            $('#dinner').val(success_data.data['dinner'] );
                        }
                    },(error)=>
                    {
                      alert(JSON.stringify(error["responseJSON"],null, 1));
                    });
        }
    });
    calendar.render();
}




capitalize = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
}

$('#add_item').click( () => {
    let meal = $("#add_meal").val();
    if(meal == ""){
        alert('Enter an Item Name');
        return;
    }
    
    meal = capitalize(meal);

    let data = {'item': meal }
    AJAXPromise("POST", "/API/addMenuItem/", data).then( (success_data) => {
        console.log(success_data);
        if ( success_data.message == 'ok'){
            window.location.reload();
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
    
});

$('#select_food').click( () => {
    var breakfast = $('#breakfast').val().join('&&') ;
    var lunch = $('#lunch').val().join('&&') ;
    var dinner = $('#dinner').val().join('&&') ;

    if(date == undefined){
        alert('pick a date');
        return ;
    }
    if(breakfast == ''){
        alert('Please select an item for breakfast');
        return;
    }
    if(lunch == ''){
        alert('Please select an item for lunch');
        return;
    }
    if(dinner == ''){
        alert('Please select an item for dinner');
        return;
    }

    data = { 'date': date, 'breakfast': breakfast, 'lunch':lunch, 'dinner':dinner }
    
    AJAXPromise("POST", "/API/addDailyItem/", data).then( (success_data) => {
        if ( success_data.message == 'ok'){
            alert('success');
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });


});

doApprove = (email, id) => {
    let room = $('#selection_room' + id ).val();
    console.log(room);
    console.log(email);
    if(room=="")
    {
        alert("Select a room");
        return;
    }
    data = {'rooms_id':room,'email':email}
    AJAXPromise("POST", "/API/setApprove/", data).then( (success_data) => {
        if ( success_data.message == 'ok'){
            window.location.reload();
        }
        
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });

}


//===================ADMISSION FORM SUBMIT
$("#admission_formsubmit").click( ( ) => {
    let mailid   = $('#form-email').val();
    let name         =  $('#name').val();
    let rollno       = $('#rollno').val();
    let dept     = $('#dept').val();
    let father      = $('#father_name').val();
    let mother      = $('#mother_name').val();
    let address1    = $('#address1').val();
    let address2     = $('#address2').val();
    let food_type   = $('input[name="food"]:checked').val();
    let password     = $('#password').val();
    let gender      = $('input[name="gender"]:checked').val();
    let dob         = $('#birth-date').val();
    let phone        = $('#phone').val();
    let city         = $('#city').val(); 
    let state       = $('#state').val(); 
    let pincode         = $('#pincode').val();
    
    if (mailid == undefined || name == undefined || rollno == undefined ||
        dept == undefined ||
        father == undefined ||
        mother == undefined ||
        address1 == undefined ||
        address2 == undefined ||
        food_type == undefined ||
        password == undefined ||
        gender == undefined ||
        dob == undefined ||
        phone == undefined ||
        city == undefined ||
        state == undefined ||
        pincode == undefined) {
        alert('Please Fill All Details');
    }
       
 
    
    if (address2 == undefined){
        address2 = null;
    }

    let address = address1 + ' ' + address2 + ' ' + city +' '+ state +' '+ pincode ;
    
    let info = { 'email': mailid, 
    'name': name, 'rollno' : rollno, 'dept': dept,
    'fathers_name': father, 'mothers_name': mother,
    'address':   address,   'food_type': food_type,
    'password': password ,   'gender': gender, 
    'dob': dob,       'phone': phone} ;

    var data = { 'data': JSON.stringify(info) };


    console.log(data);
    
    AJAXPromise("POST", "/API/newStudent/", data).then( (success_data) => {
        if ( success_data.message == 'ok'){
            alert('success');
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
    
});



//============================================GRIEVEANCE SECTION==========================================//

$('#grieveance_submit').click(newgrieveance = () => {
    if($('#grieveance_option').selectpicker().val() == '' ){ alert('Please Select a Title'); return; }
    if($('#student_grieveance_box').selectpicker().val() == '' ){ alert('Please Type your complaints'); return; }

    let title = $('#grieveance_option').selectpicker().val();
    let body = $('#student_grieveance_box').selectpicker().val();

    let data = {'title': title, 'body':body}

    AJAXPromise("POST", "/API/newGrieveance/", data).then( (success_data) => {
        
        if ( success_data.message == 'ok'){
            alert('success');
            window.location.reload();
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
        

})

fetchgrieveance = () => {
    type = 'new'
    let data = { 'type': type  } 
    console.log('uc');
    AJAXPromise("GET", "/API/fetchGrieveance/", data).then( (success_data) => {
        
        if ( success_data.message == 'ok'){
            console.log(success_data);
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
}


setGrieveance = () => {
    id = ""
    AJAXPromise("GET", "/API/setGrieveance/", data).then( (success_data) => {
        
        if ( success_data.message == 'ok'){
            console.log(success_data);
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });

}



