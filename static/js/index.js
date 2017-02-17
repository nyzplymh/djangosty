/**
 * Created by lenovo on 2017/2/15.
 */
function del( obj) {
    $.ajax({
        url: '/delU/',
        method: 'POST',
        data: {em: obj},
        dataType:'json',
        success: function (data) {
            if (data.status == 'true') {
                alert(data.status);
                $("#em").val("");
                $("#pw").val("");
                window.location.reload();
            }
        }
    });
}