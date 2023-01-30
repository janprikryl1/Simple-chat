$(document).ready(function (event) {
$('#send').on('submit', function (event) {
    event.preventDefault();
           $.ajax({
               type:'POST',
               url:'upload_msg/',
               data:{
                   'user':$.cookie("name"),
                   'msg': $('#msg').val(),
                   'csrfmiddlewaretoken':'{{ csrf_token }}'
               },
            success: function (data) {
                   if (data.Status == "OK")
                   {
                       alert("Přidáno");
                   }
                    if (data.Status == "A")
                    {
                        alert("A");
                    }
            },
               error: function (edata) {
                   alert("Chyba");
               }
           })
});
});