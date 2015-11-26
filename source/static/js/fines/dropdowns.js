$(function() {
    var addSelectUsers = function() {
        $('#id_users').prepend("<option value='' disabled selected>Select users</option>");
    };

    var initSelectDropdown = function() {
        $('select').material_select();
    };

    $('#id_amount').blur(function() {
        var amountVal = parseInt($('#id_amount').val());
        $('#id_amount').val(amountVal.toFixed(2));
    });
    addSelectUsers();
    initSelectDropdown();
});
