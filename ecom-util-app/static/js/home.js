$(function () {
    $("#bload").on("click", function () {
      var spinner = $("spinner")
      spinner.show()
      $.ajax({
        url: '/loadcache',
        type: 'GET',
        success: function (data) {
          
          if (data.result === 'Success') {
            alert('Cache loaded!')
          } else if (data.result === 'Failed') {
            alert('Unable to load cache!')
          } else {
            alert(data.result)
          }
          
          spinner.hide()
        },
        error: function () {
          spinner.hide()
          alert('Error Occured!')
        }
      })
    })
  })