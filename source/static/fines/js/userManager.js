$(function() {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });

  var handler = StripeCheckout.configure({
    key: 'pk_test_5QJZJkQXysJq5Iz2Ewa0AjId',
    locale: 'auto',
    token: function(token) {
      var selectedFines = getSelectedFines();
      $.ajax({
        type: 'POST',
        url: '/fines/manage/paid/',
        data: {fines: selectedFines}
      });
      location.reload();
    }
  });

  $(window).on('popstate', function() {
    handler.close()
  });

  $('#payFineButton').on('click', function(e) {
    var total = totalSelectedFines();
    handler.open({
      name: 'Fines Totaling $' + total,
      amount: total * 100
    });
    e.preventDefault();
  });

  $('#fineTable tr').click(function(e) {
    var total = totalSelectedFines();
    $('#total').html('$' + total);
  });

  function getSelectedFines() {
    var selectedFines = [];
    $('#fineTable tr').find('input[type="checkbox"]:checked').each(function(index, row) {
      selectedFines.push(row.id)
    });
    return selectedFines;
  }

  function totalSelectedFines() {
    var fineTotal = 0;    
    $('#fineTable tr').find('input[type="checkbox"]:checked').each(function(index, row) {
      fineTotal += +$(row).data('amount');
    });
    return fineTotal;
  }
});

