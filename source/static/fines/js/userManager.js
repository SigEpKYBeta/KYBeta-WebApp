function totalSelectedFines() {
    var selectedFines = [];
    $('#fineTable tr').find('input[type="checkbox"]:checked').each(function(index, row) {
        selectedFines.push(row.id);
    });
}

var handler = StripeCheckout.configure({
    key: 'pk_test_5QJZJkQXysJq5Iz2Ewa0AjId',
    locale: 'auto',
    token: function(token) {
        console.log(token);
    }
});

$('#payFineButton').on('click', function(e) {
    var fineTotal = totalSelectedFines();
    handler.open({
        email: 'sheldon.burks@gmail.com',
        name: 'Paying 2 Fines ($20)',
        amount: 2000
    });
    e.preventDefault();
});

$(window).on('popstate', function() {
    handler.close()
});
