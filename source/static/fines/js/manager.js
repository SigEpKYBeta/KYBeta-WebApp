$(function() {
    $('tr').dblclick(function() {
        var id = $(this).attr('id');
        window.location.href = '/fines/manage/' + id + '/';
    });
});